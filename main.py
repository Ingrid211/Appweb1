# Importar librerias
from flask import Flask, render_template
# creacion de objeto de tipo flask
app = Flask(__name__)
# Creacion de ruta raiz para la pagina principal
@app.route('/')
# Creacion de funcion para mostrar index
def index(): return render_template('index.html')
# Archivo principal de ejecucion


if __name__ == '__main__':
    # Configuracion del puerto que escucha del servidor
    app.run(port=3000, debug=True)
