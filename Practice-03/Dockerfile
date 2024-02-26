# Frontend
FROM nginx:stable-alpine

# Use a volume is more efficient
VOLUME /tmp

# Install Web App on nginx server
RUN rm -rf /usr/share/nginx/html/*

COPY nginx.conf /etc/nginx/nginx.conf
COPY dist/billingApp /usr/share/nginx/html
COPY mime.types /etc/nginx/mime.types

# Backend
# Install OpenJDK 17
RUN apk add --no-cache openjdk17

# Set environment variables
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk
ENV PATH $JAVA_HOME/bin:$PATH

# check the installation
RUN java -version

# Install Java Microservice
ENV JAVA_OPTS=""
ARG JAR_FILE
ADD ${JAR_FILE} app.jar

# Copy Init Script
COPY appshell.sh appshell.sh

# Backend:7080, Frontend:80
EXPOSE 80 7080

ENTRYPOINT [ "sh", "/appshell.sh" ]