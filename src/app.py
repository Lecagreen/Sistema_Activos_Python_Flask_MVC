from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_activo')
def crear_activo():
    return render_template('formulario_crear_activo.html')

@app.route('/modificar_activo')
def modificar_activo():
    return render_template('formulario_modificar_activo.html')

@app.route('/ver_activo')
def ver_activo():
    return render_template('tabla_activos.html')

@app.route('/crear_usuario')
def crear_usuario():
    return render_template('formulario_crear_usuario.html')

@app.route('/modificar_usuario')
def modificar_usuario():
    return render_template('formulario_modificar_usuario.html')

@app.route('/ver_usuario')
def ver_usuario():
    return render_template('tabla_usuarios.html')