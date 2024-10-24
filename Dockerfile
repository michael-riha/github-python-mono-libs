# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install git and other dependencies
RUN apt-get update && apt-get install -y git

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# # Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements/requirements.txt


# Expose the debugpy port
EXPOSE 5678

# Run the app.py script
CMD ["python", "app.py"]
