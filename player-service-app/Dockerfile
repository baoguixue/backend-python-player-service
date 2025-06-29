# Use official Python image as base
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements first for better cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 8000

# Set environment variables (optional, for Flask best practice)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Run the Flask app
CMD ["python", "app.py"] 