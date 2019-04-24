FROM python:3
RUN pip install requests    
WORKDIR /usr/src/app                                                                                                      
COPY ./omdbapi.py /usr/src/app                                                                                           
ENTRYPOINT ["/usr/local/bin/python"]                                                                                               
CMD ["omdbapi.py","Titanic"]
