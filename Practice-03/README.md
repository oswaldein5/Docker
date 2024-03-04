# Docker - Practice-03

## Use Dockerfile for create Backend and Frontend

- Create file.yml in directory Practice-03
- `docker build -t billingapp:prod --no-cache --build-arg JAR_FILE=target/*.jar .`: Create image
- `docker run -d -p 80:80 -p 7080:7080 --name ct-billing billingapp:prod`: Create & execute CT
- Check this:
	- (http://localhost:80)
	- (http://localhost:7080/swagger-ui/swagger-ui/index.html)
- `docker stop ct-billing`: Stop CT
- `docker rm ct-billing`: Delete CT
- If you want delete, first stop and then delete
- Or use: `docker rm -f ct-billing`