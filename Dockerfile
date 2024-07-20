# Use the official Ubuntu image as the base image
FROM vin1989/mlimage

WORKDIR /app
# Copy your application code
COPY . /app

# Expose any necessary ports
EXPOSE 5000

# Default command
CMD ["python3", "app.py"]

