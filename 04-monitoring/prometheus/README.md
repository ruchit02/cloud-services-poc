# Add the HELM repo and install prometheus and grafana in your kubernetes cluster

		helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
		helm repo update
		helm install prometheus prometheus-community/kube-prometheus-stack --namespace prometheus-system

# Create the provided servicemonitors (optional)

		kubectl apply -f authServiceMonitor.yaml
		kubectl apply -f docServiceMonitor.yaml
		kubectl apply -f gatewayServiceMonitor.yaml
		kubectl apply -f fluentdServiceMonitor.yaml

# Access the Prometheus dashboard

1.	Port-forward prometheus

		kubectl port-forward --address 0.0.0.0 -n prometheus-system prometheus-prometheus-kube-prometheus-prometheus-0 9090:9090

# Access the Grafana dashboard

1.	Port-forward Grafana

		kubectl port-forward --address 0.0.0.0 -n prometheus-system service/prometheus-grafana 3000:80
	
# Uninstall Prometheus

		helm uninstall prometheus-community -n prometheus-system