# Install docker, kubectl, oc, helm on Amazon Linux 2

1.	Install docker:
		
		yum update -y
		yum install docker -y
		systemctl start docker
		systemctl enable docker
		usermod -a -G docker ec2-user
		chmod 666 /var/run/docker.sock
		
2.	Install kubectl:

		curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
		sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
		chmod +x kubectl
		mkdir -p ~/.local/bin
		mv ./kubectl ~/.local/bin/kubectl
		kubectl version --client --output=yaml
		
3.	Install helm:

		wget https://get.helm.sh/helm-v3.7.1-linux-amd64.tar.gz
		tar -zxvf helm-v3.7.1-linux-amd64.tar.gz
		mv linux-amd64/helm /usr/local/bin/helm
		rm -rf linux-amd64
		rm helm-v3.7.1-linux-amd64.tar.gz
		export PATH="/usr/local/bin:$PATH"
		helm version
		
4.	Install oc:
		
		scp -i poc-key-pair.pem oc-4.11.0-linux.tar.gz ec2-user@54.235.226.250:/home/ec2-user
		tar -xvf oc-4.11.0-linux.tar.gz
		sudo mv oc /usr/local/bin
		oc version
		
		
		
		
to quickly create a daemonset, create a deployment then change the kind to daemonset and remove a few other properties