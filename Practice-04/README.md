# Practice-04 - Docker Compose
	1. Backend
	2. Frontend
	3. Adminer BD
	4. BD using volume data persistance

## Create file.yml in directory Practice-04

docker compose -f stack-billing.yml up -d

[check adminer] (http://localhost:9090)

docker inspect id-container [check containers setup]

Rewrite stack-billing.yml breaking down and building each component as a service.:
	services:
		## Database engine service
		postgres_db:
		
		## Database admin service
		adminer:
 
		## Billing App Backend service
		billingapp-back:
		
		## Billing App Frontend service
		billingapp-front:

create Dockerfile for Java
create Dockerfile for Angular

docker compose -f stack-billing.yml stop [stopping previous container created by compose]

docker compose -f stack-billing.yml rm [delete previous container created by compose]

docker rm -f ct-billing [stop and delete another containter]

docker compose -f stack-billing.yml up -d [create container using Docker compose]

docker compose -f stack-billing.yml build [probe building]


## Checking data persistance

docker system prune --all
docker volume prune
[delete containers, images, volumes]

docker compose -f stack-billing.yml up -d [Making compose again and the data must persist, check it!]

docker exec -it billingApp-back sh [modo terminal inside billingApp-back]