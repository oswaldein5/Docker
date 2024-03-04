# Docker - Practice-01

## Use Dockerfile to run an App (myscript.py) inside a container

- `docker network create mired`: Create network
- `docker network ls`: List networks
- `docker build -t miapp2:1 .`
- `docker create -p 5432:5432 --name postg --network mired -e POSTGRES_PASSWORD=prueba postgres`
- `docker create --name ct-app2 --network mired miapp2:1`
- `docker start postg`
- `docker start ct-app2`
- `docker run --name ct-app2 --network mired miapp2:1`