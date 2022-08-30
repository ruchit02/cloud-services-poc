1.	Expressing the desired amount of VMI's vCPUs can be done by either setting the guest topology in \
	spec.domain.cpu (sockets, cores, threads) or \
	spec.domain.resources.[requests/limits].cpu to a whole number integer ([1-9]+) \
	indicating the number of vCPUs requested for the VMI. \
	Number of vCPUs is counted as sockets \* cores \* threads or if spec.domain.cpu is empty then \
	it takes value from spec.domain.resources.requests.cpu or spec.domain.resources.limits.cpu.

**NOTE:** *Users should not specify both spec.domain.cpu and spec.domain.resources.[requests/limits].cpu.* \
*Also, spec.domain.resources.requests.cpu must be equal to spec.domain.resources.limits.cpu* \
*Additionally, using spec.domain.cpu.sockets instead of spec.domain.cpu.cores has a significant performance advantage*

2.	spec.domain.cpu example:
		
		apiVersion: kubevirt.io/v1alpha3
		kind: VirtualMachineInstance
		spec:
		  domain:
			cpu:
			  sockets: 2
			  cores: 1
			  threads: 1
			  dedicatedCpuPlacement: true
			  
3.	spec.domain.resources.[requests/limits].cpu example:
		
		apiVersion: kubevirt.io/v1alpha3
		kind: VirtualMachineInstance
		spec:
		  domain:
			resources:
			  limits:
				cpu: 2
				memory: 2Gi
			  requests:
				cpu: 2
				memory: 2Gi