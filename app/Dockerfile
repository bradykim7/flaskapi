# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /home/app

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# Add and install Python dependencies
COPY app /home/app
RUN pip install --no-cache-dir -r requirements.txt


# Run the application:
# CMD ["python", "your-app.py"]
# CMD ['ls']
