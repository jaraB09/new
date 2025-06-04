#Aileen Jara    p
#03/06/2025
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>¡Hola desde Flask!” </h1>'

@app.route('/ruta')
def ruta():
    return '<h1>¿Qué ruta estás buscando?</h1>'

@app.route('/bienvenido/<username>')
def profile(username):
    return f'bienvenid@ a esta ruta {username}'

@app.route('/repite/<int:numero>')
def repite(numero):
    return f"Repite después de mi: {numero*numero}</h1>"

@app.route('/repite/<int:repite>/<palabra>')
def repite2(repite, palabra):
    resultado = (palabra + ' ') * repite
    return f"<h1>Repite después de mi: {resultado}</h1>"




if __name__ == '__main__':
    app.run(debug=True)
