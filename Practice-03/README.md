## Practice-03 - Use Dockerfile for create Backend and Frontend

** Create file.yml in directory Practice-03

docker build -t billingapp:prod --no-cache --build-arg JAR_FILE=target/*.jar . [create image]

docker run -d -p 80:80 -p 7080:7080 --name ct-billing billingapp:prod [create & execute ct]

Check this:
	- (http://localhost:80)
	- (http://localhost:7080/swagger-ui/swagger-ui/index.html)

docker stop ct-billing 
docker rm ct-billing 
[if you want delete, first stop and then delete]

or use:

docker rm -f ct-billing