from sqlalchemy import Column, Integer, String, Enum
from src.models import session, Base
from flask_login import UserMixin

class Usuarios(Base, UserMixin):    
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    usuario = Column(String(20), unique=True, nullable=False)    
    contrasena = Column(String(20), nullable=False)    
    rol = Column(String(50), nullable=False)
    estado = Column(Enum('SI', 'NO', name='estado_enum'), default='SI', nullable=False)
    
    def __init__(self,usuario,contrasena,rol, estado = 'SI'):
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol =rol
        self.estado = estado

    def get_id(self):
        return str(self.idUsuario)
        
    def obtener_usuarios():
        usuarios = session.query(Usuarios).all()              
        return usuarios
        
    def obtener_usuario_por_id(idUsuario):
        usuario = session.query(Usuarios).get(idUsuario)
        return usuario

    def agregar(usuario):
        usuario = session.add(usuario)        
        session.commit()
        return usuario
    
    def validar_usuario(usuario, contrasena):
        usuario_valido = session.query(Usuarios).filter_by(usuario=usuario).first()
        if usuario_valido:
            if usuario_valido.contrasena == contrasena:
                return usuario_valido
        return False
    
    def eliminar_usuario(idUsuario):
        usuario = session.query(Usuarios).filter(Usuarios.idUsuario == idUsuario).first()
        if usuario:
            usuario.estado = 'NO'
            session.commit()
        return usuario