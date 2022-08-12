# Installing ElasticSearch & Kibana

1.	create namespace **elastic-system**:
		
		kubectl create ns elastic-system

2.	execute the following commands:

		kubectl apply -f pv.yaml
		kubectl create -f https://download.elastic.co/downloads/eck/1.8.0/crds.yaml -n elastic-system
		kubectl apply -f https://download.elastic.co/downloads/eck/1.8.0/operator.yaml -n elastic-system
		kubectl apply -f elastic-search.yaml
		kubectl apply -f kibana.yaml