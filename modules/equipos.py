from flask import Blueprint, Flask, request, jsonify
from models import db
from models.equipos import getequipos as modelGetequipos
from models.equipos import getListequipo as modelGetequiposLista
from models.equipos import createPatient
from models.equipos import deletePatientDocument
from models.equipos import editarequipo as modelEditarequipo

bp = Blueprint('equipos', __name__, url_prefix='/equipos')


@bp.route('/', methods=['GET'])
def list():
    print(db.get_connection())
    return {'message': 'Este es el servicio que lista de equipos'}, 200


@bp.route('/equipos', methods=['GET'])
def getequipos():
    return modelGetequipos()


@bp.route('/equipos_lista', methods=['GET'])
def getequiposLista():
    respuesta = modelGetequiposLista()
    return respuesta, respuesta.status


@bp.route('/crear_equipo', methods=['POST'])

# {
# 	"nombre": "Andres Felipe Castro Londoño",
# 	"edad": 25,
# 	"genero": 1,
# 	"numero_contacto": "1234567",
# 	"documento": "123456789"
# }

def createNewPatient():
    data = request.get_json()
    respuesta = createPatient(data)
    print(respuesta)
    return respuesta, respuesta.status


@bp.route('/eliminar_equipo_documento', methods=['DELETE'])
# {
# 	"documento": "987654321"
# }
def deletePatientDocumento():
    data = request.get_json()
    respuesta = deletePatientDocument(data['documento'])
    print(respuesta)
    return respuesta, respuesta.status

@bp.route('/editar_equipo', methods=['PUT'])
# {
# 	"documento": "123456789",
# 	"data": {
# 		"edad": 23
# 	}
# }
def editarequipo():
    data = request.get_json()
    respuesta = modelEditarequipo(data)
    print(respuesta)
    return respuesta, respuesta.status
