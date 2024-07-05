# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project files into the container
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to start Gunicorn and serve the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "src.eventManagementAPI.wsgi:application"]

