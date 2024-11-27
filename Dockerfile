FROM python:3.10.9-slim

# Set working directory
WORKDIR /app

# Salin file requirements.txt terlebih dahulu
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh aplikasi setelah dependensi diinstall
COPY . /app/

# Expose port untuk aplikasi Flask
EXPOSE 5000

# Command untuk menjalankan aplikasi Flask
CMD ["python", "app.py"]
