1.	the machine type can be mentioned using **spec.domain.machine.type** property

		spec:
		  domain:
			machine:
			  # This value indicates QEMU machine type.
			  type: pc-q35-2.10
	  
2.	It is possible to utilize UEFI/OVMF by setting a value via **spec.domain.firmware.bootloader**
		
		spec:
		  domain:
			firmware:
			  # this sets the bootloader type
			  bootloader:
				efi: {}
				
3.	In order to provide a consistent view on the virtualized hardware for the guest OS, \
	the SMBIOS UUID can be set to a constant value via **spec.domain.firmware.uuid**
		
		spec:
		  domain:
			firmware:
			  # this sets the UUID
			  uuid: 5d307ca9-b3ef-428c-8861-06e72d69f223
			  serial: e4686d2c-6e8d-4335-b8fd-81bee22f4815

4.	Setting the number of CPU cores is possible via **spec.domain.cpu.cores**
		
		spec:
		  domain:
			cpu:
			  # this sets the cores
			  cores: 3

5.	Setting the CPU model is possible via **spec.domain.cpu.model**
		
		spec:
		  domain:
			cpu:
			  # this sets the CPU model
			  model: Conroe
			  
	To enable the default cpu model, user may add the cpuModel field in the **KubeVirt CR**
		
		apiVersion: kubevirt.io/v1alpha3
		kind: KubeVirt
		metadata:
		  name: kubevirt
		  namespace: kubevirt
		spec:
		  ...
		  configuration:
			cpuModel: "EPYC"
			
	Default CPU model is set when vmi doesn't have any cpu model. When vmi has cpu model set, then vmi's cpu model is preferred. 
	
	As special cases you can set spec.domain.cpu.model equals to: **host-passthrough** to passthrough CPU from the node to the VM
		
		spec:
		  domain:
			cpu:
			  # this passthrough the node CPU to the VM
			  model: host-passthrough

	or set to **host-model** to get CPU on the VM close to the node one
		
		spec:
		  domain:
			cpu:
			  # this set the VM CPU close to the node one
			  model: host-model
			  
6.	Setting CPU features is possible via **spec.domain.cpu.features**
		
		spec:
		  domain:
			cpu:
			  # this sets the CPU features
			  features:
			  # this is the feature's name
			  - name: "apic"
			  # this is the feature's policy
			   policy: "require"
			   
	Policy attribute can either be omitted or contain one of the following policies: force, require(default), optional, disable, forbid.
	
7.	An optional resource request can be specified by the users to allow the scheduler to make a better decision \
	in finding the most suitable Node to place the VM
		
		spec:
		  domain:
			resources:
			  requests:
				memory: "1Gi"
				cpu: "1"
			  limits:
				memory: "2Gi"
				cpu: "2"