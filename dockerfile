# Use an official Python runtime as a parent image
FROM python:3.12-bookworm

#Install stunnel
RUN apt-get update && \
    apt-get install -y stunnel && \
    rm -rf /var/lib/apt/lists/*

#RUN apt-get install python3-pip
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./flask_app.py /app
COPY ./requirements.txt /app
COPY ./stunnel_server.conf /app
COPY ./psk.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 54321 available to the world outside this container
EXPOSE 54321

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
#CMD ["python", "flask_app.py"]
