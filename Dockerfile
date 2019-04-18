FROM python:latest                                                                                                       
WORKDIR /usr/src/app                                                                                                      
COPY ./OMDBAPI.py /usr/src/app                                                                                           
ENTRYPOINT ["/usr/local/bin/python"]
RUN pip install requests                                                                                                 
CMD ["OMDBAPI.py","Bahubali"]
