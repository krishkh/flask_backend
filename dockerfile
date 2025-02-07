# Use a base image with Python
FROM python:3.12

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc

# Create a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (if using Flask)
EXPOSE 5000

# Run the app (modify based on your framework)
CMD ["python", "app.py"]
