
# Gunakan image Python resmi
FROM python:3.10.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask, pandas, TensorFlow, and scikit-learn
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
