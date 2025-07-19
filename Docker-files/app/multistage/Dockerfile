FROM maven:3.9.9-eclipse-temurin-21-jammy AS BUILD_IMAGE

# Clone the repo
RUN git clone https://github.com/hkhcoder/vprofile-project.git

# Set heap size for Maven (this solves the error)
ENV MAVEN_OPTS="-Xmx2048m"

# Run mvn install with heap increased
RUN cd vprofile-project && git checkout docker && mvn clean install

# Second stage
FROM tomcat:10-jdk21

# Clean webapps
RUN rm -rf /usr/local/tomcat/webapps/*

# Copy built WAR from builder stage
COPY --from=BUILD_IMAGE vprofile-project/target/vprofile-v2.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080
CMD ["catalina.sh", "run"]
