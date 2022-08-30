1.	VirtualMachineInstancePresets are an extension to general VirtualMachineInstance configuration \
	behaving much like PodPresets from Kubernetes.
2.	When a VirtualMachineInstance is created, any applicable VirtualMachineInstancePresets will be applied \
	to the existing spec for the VirtualMachineInstance
3.	Once a VirtualMachineInstancePreset is successfully applied to a VirtualMachineInstance, \
	the VirtualMachineInstance will be marked with an annotation to indicate that it was applied.
4.	If a VirtualMachineInstancePreset is modified, changes will not be applied to existing VirtualMachineInstances
5.	VirtualMachineInstancePresets are namespaced resources, so should be created in the same namespace as the VirtualMachineInstances that will use them


# Create a VirtualMachineInstancePreset

1.	Example:
		
		apiVersion: kubevirt.io/v1
		kind: VirtualMachineInstancePreset
		metadata:
		  name: small-qemu
		spec:
		  selector:
			matchLabels:
			  kubevirt.io/size: small
		  domain:
			resources:
			  requests:
				memory: 64M
				

**NOTE:** *It is strongly recommended to include a Selector in the spec section,* \
*otherwise a VirtualMachineInstancePreset will match all VirtualMachineInstances in a namespace*

# Matching Multiple VirtualMachineInstances

1.	There are two ways:
	-	matchLabels: Each VirtualMachineInstance can use a specific label shared by all instances
	-	matchExpressions: Logical operators for sets can be used to match multiple labels
	
2.	matchLabel example:
		
		selector:
		  matchLabels:
			kubevirt.io/memory: large
			
	this would match:
	
		metadata:
		  labels:
			kubevirt.io/memory: large
			kubevirt.io/os: win10
			
	OR
	
		metadata:
		  labels:
			kubevirt.io/memory: large
			kubevirt.io/os: fedora27
			
3.	matchExpressions example:
		
		selector:
		  matchExpressions:
			- {key: kubevirt.io/os, operator: In, values: [fedora27, fedora26]}
	
	this would match instances with both labels:
	
		metadata:
		  labels:
			kubevirt.io/os: fedora26

		metadata:
		  labels:
			kubevirt.io/os: fedora27
			
## Exclusions

1.	Since VirtualMachineInstancePresets use Selectors that indicate which VirtualMachineInstances their settings should apply to, \
	there needs to exist a mechanism by which VirtualMachineInstances can opt out of VirtualMachineInstancePresets altogether. 
	**This is done using an annotation:**
			
			kind: VirtualMachineInstance
			version: v1
			metadata:
			  name: myvmi
			  annotations:
				virtualmachineinstancepresets.admission.kubevirt.io/exclude: "true"
			  ...
