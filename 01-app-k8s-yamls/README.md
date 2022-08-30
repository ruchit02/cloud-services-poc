# Set up the documents upload microservice based application in kubernetes

1.	Install all configmaps first:
		
		kubectl apply -f auth-map.yaml
		kubectl apply -f doc-upload-map.yaml
		kubectl apply -f gateway-map.yaml
		kubectl apply -f mysql-map.yaml
		kubectl apply -f rabbitmq-map.yaml
		
2.	Install all services:
		
		kubectl apply -f auth-service.yaml
		kubectl apply -f doc-upload-service.yaml
		kubectl apply -f gateway-service.yaml
		kubectl apply -f mysql-service.yaml
		kubectl apply -f rabbitmq-service.yaml
		
	