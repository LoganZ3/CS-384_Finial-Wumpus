#Used AI
# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the current folder into the Docker image
COPY . /app

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the game
CMD ["python", "main.py"]
