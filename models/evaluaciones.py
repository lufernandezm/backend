from models import db
from flask import Blueprint, Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

def getMusculos(documento):
    con = db.get_connection()
    dbevaluaciones = con.Modeloevaluaciones
    try:
        equipos = dbevaluaciones.equipos
        datos_ejercio = dbevaluaciones.datos_evaluacion
        evaluaciones = dbevaluaciones.evaluaciones
        musculos = dbevaluaciones.musculos

        equipo = dict(equipos.find_one({'documento': documento}))
        capturasequipo = list(datos_ejercio.find({'equipo': str(equipo['_id'])}))
        respuesta = []
        if (len(capturasequipo) > 0):
            for registro in capturasequipo:
                evaluacionRealizado = evaluaciones.find_one({'_id': ObjectId(registro['evaluacion'])})
                musculoRealizado = musculos.find_one({'_id': ObjectId(registro['musculo'])})

                del registro['evaluacion'], registro['musculo'], registro['equipo'], registro['_id']
                del evaluacionRealizado['_id'], musculoRealizado['_id']

                evaluacionDatos = {**registro , **evaluacionRealizado, **musculoRealizado}
                respuesta.append(evaluacionDatos)

            return {'message': 'evaluaciones del equipo', 'status': 200, 'data': respuesta}
        else:
            return jsonify({'message': 'equipo no tiene registros en la base de datos', 'status': 404})
    finally:
        con.close()
        print('coneccion cerrada')