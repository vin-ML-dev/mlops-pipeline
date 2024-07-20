# Use the official Ubuntu image as the base image
FROM vin1989/ml-image:1.2

WORKDIR /app
# Copy your application code
COPY . /app

RUN pip install -r requirements.txt

# Expose any necessary ports
EXPOSE 5000

# Default command
CMD ["python3", "app.py"]

