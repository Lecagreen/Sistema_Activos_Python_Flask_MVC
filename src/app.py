from flask import Flask, request, redirect, url_for
from flask.templating import render_template
from src.models import Base, engine
from src.models.usuarios import Usuarios
from flask_controller import FlaskControllerRegister
from flask_login import LoginManager

from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.secret_key = "mi llaveria"
app.debug

register = FlaskControllerRegister(app)

register.register_package('src.controllers')

Base.metadata.create_all(engine)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(idUsuario):
    return Usuarios.obtener_usuario_por_id(idUsuario)

if __name__ == '__main__':
    app.run(debug=True)
