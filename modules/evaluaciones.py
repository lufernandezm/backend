from flask import Blueprint, Flask, request, jsonify
from models import db
from models.evaluaciones import getMusculos as modelGetMusculos

bp = Blueprint('evaluaciones', __name__, url_prefix='/evaluaciones')

@bp.route('/', methods=['GET'])
def list():
    print(db.get_connection())
    return "EServicio para listar los equipos"

@bp.route('/evaluaciones', methods=['GET'])
def getMusculos():
    documento = request.args.get('documento')
    return modelGetMusculos(documento)