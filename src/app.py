from flask import Flask, render_template, request, redirect, url_for
from src.models import Base, engine
from src.models.activos import Activos
from src.models.marcas import Marcas
from src.models.modelos import Modelos
from src.models.ubicaciones import Ubicaciones
from src.models.usuarios import Usuarios
from src.models.categorias import Categorias
from src.models.divisiones import Divisiones
from src.models.tipos import Tipos

app = Flask(__name__)

app.secret_key = "mi llaveria"
app.debug

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_activo', methods=['POST','GET'])
def crear_activo():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        tipo = request.form.get('tipo')
        categoria = request.form.get('categoria')
        caracteristicas = request.form.get('caracteristicas')
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        serial = request.form.get('serial')
        largo = request.form.get('largo')
        ancho = request.form.get('ancho')
        alto = request.form.get('alto')
        diametro = request.form.get('diametro')
        division = request.form.get('division')
        ubicacion = request.form.get('ubicacion')
        activo = Activos(codigo,tipo,categoria,caracteristicas,marca,modelo,serial,largo,ancho,alto,diametro,division,ubicacion)
        Activos.agregar_activo(activo)
        return redirect(url_for('ver_activos'))
    return render_template('formulario_crear_activo.html', titulo_pagina = 'Crear Activo')

@app.route('/modificar_activo')
def modificar_activo():
    return render_template('formulario_modificar_activo.html')

@app.route('/ver_activo')
def ver_activo():
    activos = Activos.obtener_activos()
    return render_template('tabla_activos.html', titulo_pagina = 'Ver Activos', activos=activos)

@app.route('/crear_usuario', methods=['POST','GET'])
def crear_usuario():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        usuario = Usuarios(usuario)
        Usuarios.agregar_usuario(usuario)
        return redirect(url_for('ver_usuarios'))
    return render_template('formulario_crear_usuario.html', titulo_pagina = 'Crear Usuario')

@app.route('/modificar_usuario')
def modificar_usuario():
    return render_template('formulario_modificar_usuario.html')

@app.route('/ver_usuario')
def ver_usurio():
    usuarios = Usuarios.obtener_usuarios()
    return render_template('tabla_usuarios.html', titulo_pagina = 'Ver Usuarios', usuarios=usuarios)

@app.route('/crear_asignacion')
def crear_asignacion():
    return render_template('formulario_asignacion.html')

@app.route('/crear_categoria', methods=['POST','GET'])
def crear_categoria():
    if request.method == 'POST':
        categoria = request.form.get('categoria')
        categoria = Categorias(categoria)
        Categorias.agregar_categoria(categoria)
        return redirect(url_for('ver_categorias'))
    return render_template('formulario_crear_categoria.html', titulo_pagina = 'Crear Categoria')

@app.route('/modificar_categoria')
def modificar_categoria():
    return render_template('formulario_modificar_categoria.html')

@app.route('/ver_categoria')
def ver_categoria():
    categorias = Categorias.obtener_categorias()
    return render_template('tabla_categorias.html', titulo_pagina = 'Ver Categorias', categorias=categorias)

@app.route('/crear_division', methods=['POST','GET'])
def crear_division():
    if request.method == 'POST':
        division = request.form.get('division')
        division = Divisiones(division)
        Divisiones.agregar_division(division)
        return redirect(url_for('ver_divisiones'))
    return render_template('formulario_crear_division.html', titulo_pagina = 'Crear Division')

@app.route('/modificar_division')
def modificar_division():
    return render_template('formulario_modificar_division.html')

@app.route('/ver_division')
def ver_division():
    divisiones = Divisiones.obtener_divisiones()
    return render_template('tabla_divisiones.html', titulo_pagina = 'Ver Divisiones', divisiones=divisiones)

@app.route('/crear_marca', methods=['POST','GET'])
def crear_marca():
    if request.method == 'POST':
        marca = request.form.get('marca')
        marca = Marcas(marca)
        Marcas.agregar_marca(marca)
        return redirect(url_for('ver_marcas'))
    return render_template('formulario_crear_marca.html', titulo_pagina = 'Crear Marca')

@app.route('/modificar_marca')
def modificar_marca():
    return render_template('formulario_modificar_marca.html')

@app.route('/ver_marca')
def ver_marca():
    marcas = Marcas.obtener_marcas()
    return render_template('tabla_marcas.html', titulo_pagina = 'Ver Marcas', marcas=marcas)

@app.route('/crear_modelo', methods=['POST','GET'])
def crear_modelo():
    if request.method == 'POST':
        modelo = request.form.get('modelo')
        modelo = Modelos(modelo)
        Modelos.agregar_modelo(modelo)
        return redirect(url_for('ver_modelos'))
    return render_template('formulario_crear_modelo.html', titulo_pagina = 'Crear Modelos')

@app.route('/modificar_modelo')
def modificar_modelo():
    return render_template('formulario_modificar_modelo.html')

@app.route('/ver_modelo')
def ver_modelo():
    modelos = Modelos.obtener_modelos()
    return render_template('tabla_modelos.html', titulo_pagina = 'Ver Modelos', modelos=modelos)

@app.route('/crear_tipo', methods=['POST','GET'])
def crear_tipo():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        tipo = Tipos(tipo)
        Tipos.agregar_tipo(tipo)
        return redirect(url_for('ver_tipos'))
    return render_template('formulario_crear_tipo.html', titulo_pagina = 'Crear Tipo')

@app.route('/modificar_tipo')
def modificar_tipo():
    return render_template('formulario_modificar_tipo.html')

@app.route('/ver_tipo')
def ver_tipo():
    tipos = Tipos.obtener_tipos()
    return render_template('tabla_tipos.html', titulo_pagina = 'Ver Tipos', tipos=tipos)

@app.route('/crear_ubicacion', methods=['POST','GET'])
def crear_ubicacion():
    if request.method == 'POST':
        ubicacion = request.form.get('ubicacion')
        ubicacion = Ubicaciones(ubicacion)
        Ubicaciones.agregar_ubicacion(ubicacion)
        return redirect(url_for('ver_ubicaciones'))
    return render_template('formulario_crear_ubicacion.html', titulo_pagina = 'Crear Ubicacion')

@app.route('/modificar_ubicacion')
def modificar_ubicacion():
    return render_template('formulario_modificar_ubicacion.html')

@app.route('/ver_ubicacion')
def ver_ubicacion():
    ubicaciones = Ubicaciones.obtener_ubicaciones()
    return render_template('tabla_ubicaciones.html', titulo_pagina = 'Ver Ubicaciones', ubicaciones=ubicaciones)