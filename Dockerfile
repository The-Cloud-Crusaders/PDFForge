FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Install GCC and C++ build libraries
RUN apk add --no-cache gcc g++ make

# Add your additional instructions here
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy the current folder to the container
COPY . /app

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python", "main.py"]
