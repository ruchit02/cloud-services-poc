import boto3
import json
import csv
import os

env_vars_keys = []
env_vars_vals = []

def analyse(response):
	ec2_list = []
	ec2_dict = {}
	account_id = boto3.client('sts').get_caller_identity().get('Account')
	arn = boto3.client('sts').get_caller_identity().get('Arn')
	#reservation correspondes to a launch request
	#for a specific launch request, there could be a single instance OR many
	#hence Reservations field is an array
	for reservation in (response['Reservations']):
		#iterating through the instances for a specific reservation
		for instance in (reservation['Instances']):
			#extracting all tags for a specific instance
			tags = instance['Tags']
		
		#put all your tags into a dictonary
		for tag in tags:
			current_tag = tag['Key']
			current_value = tag['Value']
			ec2_dict[current_tag] = current_value
		
		ec2_dict_keys = list(ec2_dict.keys())
		#crosscheck each env variable with every item of the dictonary
		for i in range(len(env_vars_keys)):
			
			counter = 0
			
			for j in range(len(ec2_dict_keys)):
				counter=counter+1
				if env_vars_keys[i] == ec2_dict_keys[j]:
					break
					
			#if this condition is satisfied then the provided ENV_VAR isnt present in the dictonary
			#hence, add it to the dictonary
			print(counter)
			if counter == len(ec2_dict_keys):
				ec2_dict[env_vars_keys[i]] = env_vars_vals[i]
		
		if bool(ec2_dict):
			ec2_list.append(ec2_dict)
			ec2_dict = {}
	
	return ec2_list
		
def write_csv(instances, file_name):
	keys = instances[0].keys()
	with open('/tmp/' + file_name , 'w') as out:
		dict_writer = csv.DictWriter(out, keys)
		dict_writer.writeheader()
		dict_writer.writerows(instances)
		
def write_to_s3(bucket_name, file_name):
	s3=boto3.client('s3')
	with open('/tmp/' + file_name, 'rb') as f:
		s3.upload_fileobj(f,bucket_name, file_name)
		
def lambda_handler(event, context):
	cwd = os.getcwd()
	print("Current working directory:", cwd)
	bucket_name = 'lambda-ec2-tags-editor'
	file_name = 'ec2_instance.csv'
	for i, j in os.environ.items():
		env_vars_keys.append(i)
		env_vars_vals.append(j)
	
	#AWS_REGION environment variable is predefined in the lambda execution environment
	ec2 = boto3.client("ec2", region_name = os.environ["AWS_REGION"])
	response = ec2.describe_instances()
	instances = analyse(response)
	write_csv(instances, file_name)
	write_to_s3(bucket_name, file_name)
	return instances