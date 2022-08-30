1.	In order to start a VirtualMachineInstance, you just need to create a VirtualMachineInstance object using kubectl:
		
		kubectl create -f vmi.yaml
		
2.	To stop the VirtualMachineInstance, you just need to delete the corresponding VirtualMachineInstance object using kubectl:
		
		kubectl delete -f vmi.yaml
		
		OR
		
		kubectl delete vmis testvmi
	
**Note:** *Stopping a VirtualMachineInstance implies that it will be deleted from the cluster.* \
*You will not be able to start this VirtualMachineInstance object again.*

## Pausing and unpausing a virtual machine

1.	The process is frozen without further access to CPU resources and I/O but the memory used by the domain at the hypervisor level will stay allocated
2.	To pause a virtual machine, you need the virtctl command line tool:
		
		virtctl pause vm testvm
		
		OR 
		
		virtctl pause vmi testvm
		
3.	Unpausing works similar to pausing:
		
		virtctl unpause vm testvm