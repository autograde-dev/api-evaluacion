# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file initially to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port your Flask app will run on
EXPOSE 5000

# Set environment variables (optional)
ENV FLASK_APP=run.py
#Change to 'production' in production
ENV FLASK_ENV=development

# Run the Flask app
CMD ["python", "run.py"]