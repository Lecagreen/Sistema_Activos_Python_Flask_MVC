from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.usuarios import Usuarios

class UsuariosController(FlaskController):
    @app.route("/usuarios")
    def usuarios():
        usuarios = Usuarios.obtener_usuarios()
        return render_template('tabla_usuarios.html', titulo="Lista de Usuarios", usuarios=usuarios)    
    
    @app.route("/usuarios/<idUsuario>")
    def usuario_por_idUsuario(idUsuario):
        usuario = Usuarios.obtener_por_idUsuario(idUsuario)        
        return usuario

    @app.route("/crear_usuario", methods=['GET','POST'])
    def crear_usuario():
        if request.method == 'POST':
            usuario = request.form.get('usuario')
            contrasena = request.form.get('contrasena')
            rol = request.form.get('rol')
                  
            if not usuario:
                flash('El usuario es un campo obligatorio')   
            elif not contrasena:
                flash('La contraseña es un campo obligatorio') 
            elif not rol:
                flash('El rol en stock es un campo obligatorio')   
            else:          
                usuario = Usuarios(
                usuario,contrasena,rol)
                Usuarios.agregar(usuario)
                return redirect(url_for('usuarios'))    
        return render_template('formulario_crear_usuario.html', titulo="Formulario de Usuario")