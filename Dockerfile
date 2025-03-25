
# Use official Python runtime as base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . .



# Command to run the application
CMD ["python3", "main.py"]
