from models import db
from flask import Flask, request, jsonify
from bson.json_util import dumps


def getequipos():
    con = db.get_connection()
    dbevaluaciones = con.Modeloevaluaciones
    try:
        equipos = dbevaluaciones.equipos
        retorno = dumps(equipos.find({}))
        return jsonify(retorno)
    finally:
        con.close()
        print('coneccion cerrada')


def getListequipo(parametro='documento'):
    con = db.get_connection()
    dbevaluaciones = con.Modeloevaluaciones

    try:
        equipos = dbevaluaciones.equipos
        retorno = list(equipos.find({}))
        lista = [d[parametro] for d in retorno]
        return jsonify({'data': lista, 'status': 200})
    finally:
        con.close()
        print('coneccion cerrada')


def createPatient(data):
    con = db.get_connection()
    dbevaluaciones = con.Modeloevaluaciones

    try:
        equipos = dbevaluaciones.equipos
        equipos.insert(data)
        return jsonify({'message': 'equipo insertado', 'status': 200})
    except:
        return jsonify({'message': 'fallo en la insercion', 'status': 500})
    finally:
        con.close()
        print('coneccion cerrada')

def deletePatientDocument(documento):
    con = db.get_connection()
    dbevaluaciones = con.Modeloevaluaciones

    try:
        equipos = dbevaluaciones.equipos
        equipos.delete_many({'documento': documento})
        return jsonify({'message': 'equipo eliminado', 'status': 200})
    except:
        return jsonify({'message': 'fallo al eliminar equipo', 'status': 500})

    finally:
        con.close()
        print('coneccion cerrada')

def editarequipo(data):

    con = db.get_connection()
    dbevaluaciones = con.Modeloevaluaciones

    try:
        equipos = dbevaluaciones.equipos
        print(data['data'])
        equipos.find_one_and_update({'documento': data['documento']}, {'$set': data['data']})
        return jsonify({'message': 'equipo editado', 'status': 200})
    except:
        return jsonify({'message': 'fallo al editar un equipo', 'status': 500})

    finally:
        con.close()
        print('coneccion cerrada')