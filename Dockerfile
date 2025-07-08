# Use official Python runtime as the base image
FROM python:3.11-slim

# Set a directory inside the container for your app
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# Expose a port if your app runs a server (e.g., Streamlit default port)
EXPOSE 8501

# Command to run your app (adjust as needed)
CMD ["streamlit", "run", "app/main.py"]
