# Docker Swarm - Practice-06
### Database engine | Database admin
### App Backend with replicas | App Frontend with replicas
	
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
