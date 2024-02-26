## Practice-02 - Docker

** Use Dockerfile to create server nginx, copy index.html and check if it works

docker run -p 80:80 --name srv-nginx -d nginx
docker cp index.html srv-nginx:/usr/share/nginx/html

[check] (http://localhost)

docker logs -n1 srv-nginx [show last line file log]

docker logs -f srv-nginx [show logs in real time]
