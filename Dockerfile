FROM ubutu:xenial
RUN apt-get update && apt-get install python3 -y && apt-get install pip-python -y && pip install requests    
WORKDIR /usr/src/app                                                                                                      
COPY ./omdbapi.py /usr/src/app                                                                                                                                                                                       
CMD ["python","omdbapi.py","Titanic"]
