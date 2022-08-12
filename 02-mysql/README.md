# Install the required databases

1.	Command to enter the mysql pod:
		
		kubectl exec -it <name of mysql pod> -- mysql -uroot -proot
		
2.	source the files:
		
		source 1-privilege.sql;
		source employeedocumentdetails;
		source websecurity.sql;
		
3.	Check databases:
		
		show databases;
		
4.	Check tables:
		
		show tables;