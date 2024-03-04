# Docker Compose - Practice-05
	## 1. Backend
	## 2. Frontend
	## 3. Adminer BD
	## 4. BD using volume data persistance
	## 5. Resources (Limits, reservations)
	## 6. Networks

- Update file.yml in directory Practice-05
- `docker stats`
- `docker compose -f stack-billing.yml start|stop`
- Add in Backend for limits and reservations resources:
```
deploy:
      resources:
        limits:
          cpus: "0.15"
          memory: 250M
        reservations:
          cpus: "0.1"
          memory: 128M
```
- `docker compose -f stack-billing.yml up -d --force-recreate`
- Add networks for both enviroments prod and prep:
```
networks:
  env_prod:
    driver: bridge
    driver_opts:
      com.docker.networl.enable_ipv6: "true"
    ipam:
      driver: default
      config:
        - subnet: 172.16.232.0/24
          gateway: 172.16.232.1
        - subnet: "2001:db8::/64"
          gateway: "2001:db8::1"
```
- `docker stop $(docker ps -a -q)`: It effectively stops all running containers by passing the list of container IDs (obtained from docker ps -a -q) to the docker stop command.
- `docker system prune --all` : Delete ALL
- `docker volume prune`: Delete all volumes
- `docker compose -f stack-billing.yml up -d --force-recreate`