# Use an official Python runtime as a parent image but it is 1 GB...
FROM python:3.12-bookworm

# This to make the docker container lighter but it is not tested
# FROM ubuntu:20.04

RUN apt-get upgrade && \
    apt-get update

# in order to install python on the ligher version
# RUN apt-get install -y python3.10 # AT LEAST 3.10 for the project
#     apt-get install python3-pip
#     pip3 install --upgrade pip

#Install stunnel and nano
RUN apt-get install -y stunnel && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get install -y nano

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# YOU NEED TO CREATE THE psk.txt FILE
COPY ./flask_app.py /app
COPY ./requirements.txt /app
COPY ./stunnel_server.conf /app
COPY ./psk.txt /app

# Install any needed packages specified in requirements.txt (for the moment just flask)
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 9999 available to the world outside this container
# for the SKIP protocol
EXPOSE 9999

# Run app.py when the container launches
#CMD ["python", "flask_app.py"]
