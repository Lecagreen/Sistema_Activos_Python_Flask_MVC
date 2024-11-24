from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.usuarios import Usuarios
from flask_login import login_user

class LoginController(FlaskController):
    @app.route('/login', methods=['POST','GET'])
    def login():
        if request.method == 'POST':
            usuario = request.form.get('usuario')
            contrasena = request.form.get('contrasena')
            usuario_valido = Usuarios.validar_usuario(usuario, contrasena)
            if usuario_valido:
                login_user(usuario_valido)
                return redirect(url_for('index'))
            return redirect(url_for('login'))
        return render_template('formulario_login.html', titulo_pagina = 'Login')