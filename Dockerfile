FROM python:latest                                                                                                       
WORKDIR /usr/src/app                                                                                                      
COPY ./omdbapi.py /usr/src/app                                                                                           
ENTRYPOINT ["/usr/local/bin/python"]
RUN pip install requests                                                                                                 
CMD ["omdbapi.py","Bahubali"]
