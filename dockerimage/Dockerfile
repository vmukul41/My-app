FROM ubuntu

WORKDIR /root/

RUN apt update && apt install python3 pip -y &&  \
apt-get install libmysqlclient-dev -y  &&  apt install vim -y 

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY templates  ./templates
COPY  app.py ./

EXPOSE 8000

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]

