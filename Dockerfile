# Gunakan image Python resmi
FROM python:3.10.9-slim

# Set working directory
WORKDIR /app

# Copy semua file ke container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port untuk aplikasi Flask
EXPOSE 3000

# Command untuk menjalankan aplikasi
CMD ["python", "app.py"]
