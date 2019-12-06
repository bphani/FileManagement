# FROM ubuntu:18.04

# EXPOSE 3005

# RUN apt-get update -y && \
#     apt-get install -y python3 python3-dev python3-pip


# RUN apt-get install -y sudo curl wget locales
# RUN locale-gen en_CA.UTF-8
# ENV LC_ALL=en_CA.UTF-8
# ENV LANG=en_CA.UTF-8
# ENV LANGUAGE=en_CA.UTF-8

# # We copy just the requirements.txt first to leverage Docker cache
# COPY ./requirements.txt ./app/requirements.txt

# COPY . ./app



# WORKDIR /app


# RUN pip3  install -r requirements.txt
# RUN pip3 install uvicorn
# RUN pip3 install fastapi
# RUN pip3 install fastapi[all]
# RUN pip3 install email-validator
# RUN pip3 install pymongo





#CMD ["python3","-u","app.py"]
#CMD ["/usr/local/bin/gunicorn", "--config", "gunicorn_config.py" , "app:app","uvicorn.workers.UvicornWorker"]
#CMD ["/usr/local/bin/uvicorn","--host","0.0.0.0" ,"app:app","--port","3005"]
# CMD ["uvicorn","--host","0.0.0.0" ,"app:app","--port","3005"]

#FROM tiangolo/uvicorn-gunicorn:python3.7
#EXPOSE 80
#RUN pip3 install fastapi
#RUN pip3 install fastapi[all]
#RUN pip3 install email-validator
#RUN pip3 install pymongo
#
#COPY . /app
#WORKDIR /app
#RUN pip  install -r requirements.txt
#FROM includeamin/ubuntu_fastapi:latest
FROM includeamin/ubuntu_fastapi:v2
EXPOSE 3005
RUN mkdir app
COPY . ./app
RUN cd app && ls
WORKDIR app
CMD ["/usr/local/bin/gunicorn" , "app:app","-w","2", "-k", "uvicorn.workers.UvicornWorker","--bind","0.0.0.0:3005","--log-level","debug","--threads=2"]
