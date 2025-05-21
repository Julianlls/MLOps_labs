# Official Alpine Python image from Docker Hub                         
FROM python:3.12-alpine3.21

# Set the working directory to /app and copy current dir
# WORKDIR will set the working directory inside the container. It's gonna cr    eate a "app" folder.

WORKDIR /app
# COPY will copy the directory of where the docker file (the first ".") is i    n the computer and the second "." means to the current working directory ins    ide the container, which is "app"
COPY . .

#RUN -> during docker build; it would be the one that we'd use if we want to install packages or anything.
  
# Run hello_world.p when the container launches through the command "docker run"
CMD ["python", "hello_world.py"]
