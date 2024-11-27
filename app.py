
from flask import Flask

# Membuat objek Flask
app = Flask(__name__)

# Route utama untuk halaman beranda


@app.route('/')
def hello_world():
    return 'Hello, World!'


# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

