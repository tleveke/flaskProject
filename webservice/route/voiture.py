from flask import Blueprint, jsonify, request

from webservice.model.voiture import Voiture

voiture_api = Blueprint('voiture_api', __name__)
vitesseKmH = 0
distanceKm = 0
nbPanneau = 0
dbVoiture = Voiture()


# ---------- Method GET -----
@voiture_api.route('/', methods=['GET'])
def getVoiture():
    voitureData = dbVoiture.getVoiture()
    vitesse = {
        'type': 'vitesse',
        'value': voitureData[1]
    }
    distance = {
        'type': 'distance',
        'value': voitureData[2]
    }
    panneau = {
        'type': 'panneau',
        'value': voitureData[3]
    }
    dictionnaire = [vitesse, distance, panneau]
    return jsonify(dictionnaire)


@voiture_api.route('/vitesse', methods=['GET'])
def getVitesse():
    vitesseKmH = dbVoiture.getVoitureVitesse()
    dictionnaire = {
        'type': 'vitesse',
        'value': vitesseKmH
    }
    return jsonify(dictionnaire)


@voiture_api.route('/distance', methods=['GET'])
def getDistance():
    distanceKm = dbVoiture.getVoitureDistance()
    dictionnaire = {
        'type': 'distance',
        'value': distanceKm
    }
    return jsonify(dictionnaire)


@voiture_api.route('/panneau', methods=['GET'])
def getNbPanneau():
    nbPanneau = dbVoiture.getVoitureNbPanneau()
    dictionnaire = {
        'type': 'nbPanneau',
        'value': nbPanneau
    }
    return jsonify(dictionnaire)


# ---------- Method PUT --------

@voiture_api.route('/', methods=['PUT'])
def setVoiture():
    voitureRequest = request.json

    dbVoiture.setVoiture((voitureRequest['vitesse'], voitureRequest['distance']
                          , voitureRequest['nbPanneau'], voitureRequest['id']))

    return voitureRequest


@voiture_api.route('/vitesse', methods=['PUT'])
def setVitesse():
    voitureRequest = request.json

    dbVoiture.setVoiture((voitureRequest['vitesse'], voitureRequest['id']))

    return voitureRequest


@voiture_api.route('/distance', methods=['PUT'])
def setDistance():
    voitureRequest = request.json

    dbVoiture.setVoiture((voitureRequest['distance'], voitureRequest['id']))

    return voitureRequest


@voiture_api.route('/nbPanneau', methods=['PUT'])
def setNbPanneau():
    voitureRequest = request.json

    dbVoiture.setVoiture((voitureRequest['nbPanneau'], voitureRequest['id']))

    return voitureRequest
