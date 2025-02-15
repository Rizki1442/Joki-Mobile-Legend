from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/layanan')
def layanan():
    return render_template('layanan.html')

@app.route('/paket_harga')
def paket_harga():
    return render_template('paket_harga.html')

@app.route('/erd')
def erd():
    return render_template('erd.html')

if __name__ == '__main__':
    app.run(debug=True)