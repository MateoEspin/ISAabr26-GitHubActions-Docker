from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Pasamos el título a la plantilla
    titulo = "Mateo Espin en Python con Flask"
    return render_template('index.html', titulo=titulo)

if __name__ == '__main__':
    # Ejecutar en el puerto 5000
    app.run(debug=True, host='0.0.0.0', port=5000)