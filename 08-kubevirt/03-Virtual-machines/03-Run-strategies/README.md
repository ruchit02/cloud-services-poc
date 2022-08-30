1.	VirtualMachines have a **Running** setting that determines whether or not there should be a guest running or not
2.	To allow for greater variation of user states, the **RunStrategy** field has been introduced. \
	This is **mutually exclusive** with Running as they have somewhat overlapping conditions.
3.	There are currently four RunStrategies defined:
	-	**Always**: A VirtualMachineInstance will always be present. If the VirtualMachineInstance crashed, a new one will be spawned. 
	-	**RerunOnFailure**: A VirtualMachineInstance will be respawned if the previous instance failed in an error state. It will not be re-created if the guest stopped successfully
	-	**Manual**: The presence of a VirtualMachineInstance or lack thereof is controlled exclusively by the start/stop/restart VirtualMachine subresource endpoints
	-	**Halted**: No VirtualMachineInstance will be present. If a guest is already running, it will be stopped.
4.	Example:
		
		apiVersion: kubevirt.io/v1alpha3
		kind: VirtualMachine
		metadata:
		  labels:
			kubevirt.io/vm: vm-cirros
		  name: vm-cirros
		spec:
		  runStrategy: Always
		  template:
			metadata:
			  labels:
				kubevirt.io/vm: vm-cirros
			spec:
			  domain:
				devices:
				  disks:
				  - disk:
					  bus: virtio
					name: containerdisk
			  terminationGracePeriodSeconds: 0
			  volumes:
			  - containerDisk:
				  image: kubevirt/cirros-container-disk-demo:latest
				name: containerdisk