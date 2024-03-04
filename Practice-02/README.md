# Docker - Practice-02

## Use Dockerfile to create server nginx, copy index.html and check if it works

- `docker run -p 80:80 --name srv-nginx -d nginx`
- `docker cp index.html srv-nginx:/usr/share/nginx/html`
- Check: `http://localhost`
- `docker logs -n1 srv-nginx`: Show last line file log
- `docker logs -f srv-nginx`: Show logs in real time
