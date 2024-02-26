# Practice-05 - Docker Compose
	1. Backend
	2. Frontend
	3. Adminer BD
	4. BD using volume data persistance
	5. Resources (Limits, reservations)
	6. Networks

## Update file.yml in directory Practice-05

docker stats

docker compose -f stack-billing.yml start|stop

deploy:
      resources:
        limits:
          cpus: "0.15"
          memory: 250M
        reservations:
          cpus: "0.1"
          memory: 128M
[Add in Backend for limit resources:]

docker compose -f stack-billing.yml up -d --force-recreate

networks:
  ### Network PROD
  env_prod:
    driver: bridge
    driver_opts:
      com.docker.networl.enable_ipv6: "true"
    ### Ip Address Manager
    ipam:
      driver: default
      config:
        - subnet: 172.16.232.0/24
          gateway: 172.16.232.1
        - subnet: "2001:db8::/64"
          gateway: "2001:db8::1"
[Add networks for both enviroments prod and prep]

docker stop $(docker ps -a -q) [it effectively stops all running containers by passing the list of container IDs (obtained from docker ps -a -q) to the docker stop command.]

docker system prune --all
docker volume prune

docker compose -f stack-billing.yml up -d --force-recreate