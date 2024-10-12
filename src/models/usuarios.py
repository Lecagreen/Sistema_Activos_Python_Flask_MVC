from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from src.models import session, Base

class Usuarios(Base):
    __tablename__ = 'usuarios'

    idUsuario = Column(Integer, primary_key=True)
    usuarioAdv = Column(String(10), unique=True, nullable=True)
    nombres = Column(String(50), nullable=True)
    apellidos = Column(String(50), nullable=True)
    fechaCreacion = Column(Date, nullable=True)
    correoElectronico = Column(String(20), unique=True, nullable=True)
    division = Column(String(50), nullable=False)

    def __init__(self, usuarioAdv, nombres, apellidos, fechaCreacion, correoElectronico, division):
        self.usuarioAdv = usuarioAdv
        self.nombres = nombres
        self.apellidos = apellidos
        self.fechaCreacion = fechaCreacion
        self.correoElectronico = correoElectronico
        self.division = division

    def obtener_usuarios():
        usuarios = session.query(Usuarios).all()
        return usuarios
        
    def agregar_usuarios():
        usuario = session.add(usuario)
        session.commit()
        return usuario