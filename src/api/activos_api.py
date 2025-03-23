from flask_restful import Resource
from flask import request
from flask_cors import cross_origin

from src.models.activos import Activos
from src.models.marcas import Marcas
from src.models.modelos import Modelos
from src.models.categorias import Categorias
from src.models.divisiones import Divisiones
from src.models.tipos import Tipos

class ActivosApi(Resource):

    @cross_origin()
    def post(self):
        activo = Activos (codigo=request.json["codigo"]
                            ,categoria = request.json["categoria"]
                            ,tipo = request.json["tipo"]
                            ,caracteristicas = request.json["caracteristicas"]
                            ,marca = request.json["marca"]
                            ,modelo = request.json["modelo"]
                            ,serial = request.json["serial"]
                            ,largo = request.json["largo"]
                            ,ancho = request.json["ancho"]
                            ,alto = request.json["alto"]
                            ,diametro = request.json["diametro"]
                            ,division = request.json["division"])
        Activos.agregar_activo(activo)
        return "activo guardado"