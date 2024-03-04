# Docker Swarm - Practice-06
	## 1. Database engine
	## 2. Database admin
	## 3. App Backend with replicas
	## 4. App Frontend wirh replicas
	
## Initialize
`docker swarm init`

## check status
`docker info`

## Build images for back and front
`docker compose -f file.yml build`

## Add replicas and modify file.yml (go to deploy section)
```
deploy:
      replicas: 3
```
## Comment all lines with "container_name"

## Define image (first deploy images for back and front)
`image: image_name front|back`: Add this line for back and front

## Execute
- `docker stack deploy -c file.yml my-stack`

## Check status
- `docker service ls`
- `docker stack ps billing`
- `docker stats`

## delete stack
- `docker stack rm billing`

## Leave Docker Swarm
- `docker swarm leave --force`
