FROM python

#Deault workdir

COPY . /neumonia

WORKDIR /neumonia

RUN apt-get update -y
RUN apt-get install python3-opencv -y


COPY requirements.txt /neumonia/requirements.txt


#ADD . /neumonia

# Update
RUN pip3 install --upgrade pip

# Install
RUN pip3 install -r requirements.txt

#RUN apt-get install docker-scan-plugin

# Run the application
CMD ["./Mi_App.py"]
ENTRYPOINT ["python"]
