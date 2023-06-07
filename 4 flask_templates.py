from flask import Flask, render_template
# Vinculando Flask a un html y dandole uso
#Jinja permite cargar o renderizar archivos html desde python
# https://jinja.palletsprojects.com/en/3.1.x/
app = Flask(__name__)

@app.route("/inicio")
def inicio():
    return render_template('inicio.html', nombre ='Rafael', edad = 35)

app.run(debug=True)