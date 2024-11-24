from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from src.models import session, Base
from sqlalchemy_serializer import SerializerMixin
from src.models.divisiones import Divisiones

class Empleados(Base, SerializerMixin):
    __tablename__ = 'empleados'
    idEmpleado = Column(Integer, primary_key=True)
    usuarioAdv = Column(String(10), unique=True, nullable=True)
    division = Column(Integer, ForeignKey('divisiones.idDivision'), nullable=False)
    nombres = Column(String(50), nullable=True)
    apellidos = Column(String(50), nullable=True)
    correoElectronico = Column(String(40), unique=True, nullable=True)

    def __init__(self, usuarioAdv,division, nombres, apellidos, correoElectronico ):
        self.usuarioAdv = usuarioAdv
        self.division = division
        self.nombres = nombres
        self.apellidos = apellidos
        self.correoElectronico = correoElectronico

    def obtener_empleados():
        empleados = session.query(Empleados, Divisiones).join(Divisiones, Empleados.division == Divisiones.idDivision).all()
        return empleados
    
    @staticmethod
    def obtener_empleados_asignacion():
        empleados = session.query(Empleados).all()
        return empleados
    
    @staticmethod
    def obtener_empleado_por_id(idEmpleado):
        try:
            empleado = (
                session.query(Empleados, Divisiones)
                .join(Divisiones, Empleados.division == Divisiones.idDivision)
                .filter(Empleados.idEmpleado == idEmpleado)
                .first()
            )
            if empleado:
                empleado_info, division_info = empleado
                return {
                    'idEmpleado': empleado_info.idEmpleado,
                    'usuarioAdv': empleado_info.usuarioAdv,
                    'nombres': empleado_info.nombres,
                    'apellidos': empleado_info.apellidos,
                    'correoElectronico': empleado_info.correoElectronico,
                    'divisionEmpleado': division_info.division
                }
            else:
                return None
        except Exception as e:
            print(f"Error al obtener empleado por ID {idEmpleado}: {e}")
            return None
          
    def agregar_empleado(empleado):
        empleado = session.add(empleado)
        session.commit()
        return empleado
    
    @staticmethod
    def editar_empleado(empleado):
        session.merge(empleado)
        session.commit()
        return empleado