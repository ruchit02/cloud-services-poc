
## Stack

1.	[kubevirt archiecture](1.JPG)
2.	Users requiring virtualization services are speaking to the **Virtualization API** \
	which in turn is speaking to the **Kubernetes cluster** to schedule requested Virtual Machine Instances
3.	**Scheduling, networking, and storage** are all delegated to Kubernetes, \
	while KubeVirt provides the virtualization functionality
	
## Additional Services

1.	KubeVirt provides **additional functionality** to your Kubernetes cluster, to perform virtual machine management
2.	KubeVirt delivers three things to provide the new functionality:
	-	Additional types - so called Custom Resource Definition (CRD) - are added to the Kubernetes API
	-	**Additional controllers** for cluster wide logic associated with these new types
	-	**Additional daemons** for node specific logic associated with new types
3.	Once all three steps have been completed, you are able to:
	-	create new objects of these new types in Kubernetes (VMIs in our case)
	-	the new controllers take care to get the VMIs scheduled on some host
	-	a daemon(the **virt-handler**): is taking care of a host, alongside the kubelet, to launch the VMI and configure it until it matches the required state
4.	One final note; both controllers and daemons are running as Pods on top of the Kubernetes cluster, and are not installed alongside it.

## Application Layout¶

1.	VirtualMachineInstance (VMI) is the custom resource that represents the basic ephemeral building block of an instance.
2.	In a lot of cases this object won't be created directly by the user but by a high level resource. These High level resources for VMI can be:
	-	VirtualMachine (VM) - StateFul VM that can be stopped and started while keeping the VM data and state.
	-	VirtualMachineInstanceReplicaSet (VMIRS) - Similar to pods ReplicaSet, a group of ephemeral VMIs with similar configuration defined in a template

## VirtualMachine

1.	A VirtualMachine provides additional management capabilities to a VirtualMachineInstance inside the cluster. 
2.	It focuses on a 1:1 relationship between the controller instance and a virtual machine instance.
3.	A VirtualMachine will make sure that a VirtualMachineInstance object with an identical name will be present in the cluster, if spec.running is set to true. \
	Further it will make sure that a VirtualMachineInstance will be removed from the cluster if spec.running is set to false.
	
## Starting and stopping

1.	After creating a VirtualMachine it can be switched on or off like this:
		
		# Start the virtual machine:
		virtctl start vm

		# Stop the virtual machine:
		virtctl stop vm
		
2.	kubectl can be used too:

		# Start the virtual machine:
		kubectl patch virtualmachine vm --type merge -p '{"spec":{"running":true}}'

		# Stop the virtual machine:
		kubectl patch virtualmachine vm --type merge -p '{"spec":{"running":false}}'

## Controller status¶

1.	Once a VirtualMachineInstance is created, its state will be tracked via status.created and status.ready fields of the VirtualMachine.

## Restarting

1.	A VirtualMachineInstance restart can be triggered by deleting the VirtualMachineInstance.
		
		# Restart the virtual machine (you delete the instance!):
		kubectl delete virtualmachineinstance vm
		
	This would perform a normal restart for the VirtualMachineInstance and would reschedule the VirtualMachineInstance on a new virt-launcher Pod
	
## Example

1.	[start the VM instance](3.JPG)
2.	Save this manifest into vm.yaml and submitting it to Kubernetes will create the controller instance:
		
		$ kubectl create -f vm.yaml
		virtualmachine "vm-cirros" created
		
3.	Since spec.running is set to false, no vmi will be created:
		
		$ kubectl get vmis
		No resources found
		
4.	Let's start the VirtualMachine:
		
		$ virtctl start vm vm-cirros
		
	As expected, a VirtualMachineInstance called vm-cirros will get created