# Procrastinator Dockerfile

# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install a package that helps with procrastination
RUN apt-get update && apt-get install -y cowsay

# Make a funny message
CMD ["cowsay", "I'll do it tomorrow!"]
