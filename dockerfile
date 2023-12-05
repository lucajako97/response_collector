# Use an official Python runtime as a parent image
FROM python:3.10-bookworm

#Install stunnel
RUN apt-get update && \
    apt-get install -y stunnel && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# Make port 22 and 443 available to the world outside this container
EXPOSE 443, 22, 2222

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
#CMD ["python", "flask_app.py"]
