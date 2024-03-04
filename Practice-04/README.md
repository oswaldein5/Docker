# Docker Compose - Practice-04
##	- Backend
##	- Frontend
##	- Adminer BD
##	- BD using persistance

- Create file.yml in directory Practice-04
- `docker compose -f stack-billing.yml up -d`
- [check adminer] (http://localhost:9090)
- `docker inspect id-container`: check containers setup
- Rewrite stack-billing.yml breaking down and building each component as a service.:
```
services:
	postgres_db:
	adminer:
	billingapp-back:
	billingapp-front:
```
- create Dockerfile for Java
- create Dockerfile for Angular
- `docker compose -f stack-billing.yml stop`: stopping previous container created by compose
- `docker compose -f stack-billing.yml rm`: delete previous container created by compose
- `docker rm -f ct-billing`: stop and delete another containter
- `docker compose -f stack-billing.yml up -d`: create container using Docker compose
- `docker compose -f stack-billing.yml build`: probe building
- Checking data persistance
`docker system prune --all`: delete all
`docker volume prune`: delete volumes
`docker compose -f stack-billing.yml up -d`: Making compose again and the data must persist, check it!
`docker exec -it billingApp-back sh`: modo terminal inside billingApp-back