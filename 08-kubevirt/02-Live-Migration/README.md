1.	Live migration is a process during which a running Virtual Machine Instance moves to another compute node \
	while the guest workload continues to run and remain accessible.

##  Requirements:

1.	Live migration must be enabled in the feature gates to be supported. The feature gates field in the KubeVirt CR must be expanded by adding the LiveMigration to it.
2.	Virtual machines using a PersistentVolumeClaim (PVC) must have a shared **ReadWriteMany (RWX) access mode** to be live migrated
3.	Live migration requires ports 49152, 49153 to be available in the virt-launcher pod.

## ways to initiate live migration

1.	post a VirtualMachineInstanceMigration (VMIM) object to the cluster:
		
		apiVersion: kubevirt.io/v1alpha3
		kind: VirtualMachineInstanceMigration
		metadata:
		  name: migration-job
		spec:
		  vmiName: vmi-fedora
		  
2.	Live migration can also be initiated using virtctl

		virtctl migrate vmi-fedora
		
## available migration methods

1.	BlockMigration indicates that some of the VMI disks require copying from the source to the destination.
2.	LiveMigration means that only the instance memory will be copied.
		
		Status:
		  Conditions:
			Status: True
			Type: LiveMigratable
		  Migration Method: BlockMigration
		  
## cancelling live migration

1.	command:
		
		virtctl migrate-cancel vmi-fedora