from sqlalchemy import Column, Integer, String
from src.models import session, Base
from sqlalchemy_serializer import SerializerMixin

class Usuarios(Base, SerializerMixin):    
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    usuario = Column(String(20), unique=True, nullable=False)    
    contrasena = Column(String(20), nullable=False)    
    rol = Column(String(50), nullable=False)
    
    def __init__(self,usuario,contrasena,rol):
        self.usuario=usuario
        self.contrasena=contrasena
        self.rol=rol
        
    def obtener_usuarios():
        usuarios = session.query(Usuarios.idUsuario, Usuarios.usuario, Usuarios.rol).all()              
        return usuarios
        
    def obtener_por_idUsuario(idUsuario):
        usuario = session.query(Usuarios).get(idUsuario)
        return usuario.to_dict()

    def agregar(usuario):
        usuario = session.add(usuario)        
        session.commit()
        return usuario