# VirtualMachineInstancetype

1.	**Instancetypes and preferences provide a way** to define a set of resource, performance and other runtime characteristics, \
	allowing users **to reuse these definitions across multiple VirtualMachines**
2.	KubeVirt provides two Instancetype based CRDs:
	-	a cluster wide VirtualMachineClusterInstancetype and
	-	a namespaced VirtualMachineInstancetype
3.	These CRDs encapsulate the following resource related characteristics of a VirtualMachine through a shared VirtualMachineInstancetypeSpec:
	-	**CPU** : Required number of vCPUs presented to the guest
	-	**Memory** : Required amount of memory presented to the guest
	-	**GPUs** : Optional list of vGPUs to passthrough
	-	**HostDevices** : Optional list of HostDevices to passthrough
	-	**IOThreadsPolicy** : Optional IOThreadsPolicy to be used
	-	**LaunchSecurity** : Optional LaunchSecurity to be used

**NOTE:** *Anything provided within an instancetype cannot be overridden within the VirtualMachine*

# VirtualMachinePreference

1.	KubeVirt also provides two Preference based CRDs:
	-	a cluster wide VirtualMachineClusterPreference
	-	a namespaced VirtualMachinePreference
2.	Unlike instancetypes, preferences only represent the preferred values and as such **can be overridden** by values in the VirtualMachine provided by the user
