In here having the OMDB python program that will query the OMDB Web Api
TO see the output of the program run python omdbapi.py 'Titanic'
For Dockerize the program we will write the Dockerfile
In Dockerfile mentioned FROM python:latest   this for taking the base image from docker hub
WORKDIR /usr/src/app this is for when container created defaulty work from that Directory
COPY ./omdbapi.py /usr/src/app  this will copy the omdbapi. py to container 
ENTRYPOINT ["/usr/local/bin/python"] sets the default application that is used every time a container is created using the image.
RUN pip install requests This will install python module inside the image 
CMD ["omdbapi.py","Bahubali"] can be used for executing a specific command


first we create image out of Dockerfile for that rum command docker build -t (imagename) (path of Dockerfile) if Dockerfile present in the same directory just give .
After creating the image create the container out of image 
Run the command docker run (imagename)
   
