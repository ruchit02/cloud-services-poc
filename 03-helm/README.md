# Installing HELM

1.	commands to install helm:

		wget https://get.helm.sh/helm-v3.7.1-linux-amd64.tar.gz
		tar -zxvf helm-v3.7.1-linux-amd64.tar.gz
		mv linux-amd64/helm /usr/local/bin/helm
		rm -rf linux-amd64
		rm helm-v3.7.1-linux-amd64.tar.gz
		
## Remove read permissions from others and group

1.	Isolate access to the kubeconfig file

		chmod o-r /root/.kube/config
		chmod g-r /root/.kube/config