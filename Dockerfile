# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application script
COPY app.py .

# Expose the port the web server will run on
EXPOSE 80

# Run the status checker in the background and start the web server
CMD python app.py & python -m http.server 80 --directory /app/html --bind 0.0.0.0