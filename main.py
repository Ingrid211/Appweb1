import psycopg2
# Importar librerias
from flask import Flask, render_template, request,url_for, redirect
# creacion de objeto de tipo flask
#from flaskext.mysql import MySQL#
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_url_path='/static')
# Creacion de ruta raiz para la pagina principal
#conexion con mysql
db = SQLAlchemy(app)
conn = psycopg2.connect(

    host="ec2-44-196-250-191.compute-1.amazonaws.com",
    database="d1gad0alen3ls3",
    user="fjnabzvmjtmfzq",
    password="8ddd72698d227ac95f09aa100deb3bf30bcfc4a24f6c96278cca2337360c9a05"
)

@app.route('/')
# Creacion de funcion para mostrar index
def index(): return render_template('index.html')
# Archivo principal de ejecucion
@app.route("/regilla")
def regilla_html():
 return render_template("html_regilla.html")
@app.route("/formulario")
def formulario():

    conect = conn.cursor()
    conect.execute("SELECT * FROM productos")

    datos = conect.fetchall()

    print(datos)
    conect.close()
    return render_template("formulario.html", productos=datos)

@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    nombre = request.form["nombre"]
    descrip = request.form["descrip"]
    precio = request.form["precio"]
#abrimos conexion

#crea una interaccion a la conexion de la db
    conect = conn.cursor()
    conect.execute("INSERT INTO productos(nombre,descrip,precio) VALUES (%s,%s,%s)",
                    (nombre, descrip, precio))
    conn.commit()

    conect.close()

    return redirect("/formulario")

@app.route("/eliminar_producto/<string:id>")
def eliminar_producto(id):

    conect = conn.cursor()
    conect.execute("DELETE FROM productos where id={0}".format(id))
    conn.commit()
    conect.close()

    return redirect("/formulario")

@app.route("/consultar_producto/<id>")
def obtener_producto(id):


    conect = conn.cursor()
    conect.execute("select *  FROM productos where id= %s", (id))
    dato=conect.fetchone()
    print(dato)
    conect.close()

    return render_template("form_editar_producto.html", producto=dato)

@app.route("/editar_producto/<id>", methods=['POST'])
def editar_producto(id):
    nombre = request.form["nombre"]
    descripcion = request.form["descrip"]
    precio = request.form["precio"]


    conect = conn.cursor()
    conect.execute("UPDATE productos SET nombre=%s, descrip=%s, precio=%s WHERE id=%s",
                   (nombre, descripcion, precio, id))
    conn.commit()
    conect.close()
    return redirect("/formulario")

@app.route("/bootstrap")
def bootstrap_htm():
    return render_template('/Bootstrap.html')

if __name__ == '__main__':
    # Configuracion del puerto que escucha del servidor
    app.run(port=3000, debug=True)
