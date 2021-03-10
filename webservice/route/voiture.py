from flask import Blueprint, jsonify, request
import datetime

from webservice.model.voiture import Voiture

voiture_api = Blueprint('voiture_api', __name__)
vitesseKmH = 0
distanceKm = 0
nbPanneau = 0
dbVoiture = Voiture()


# ---------- Method GET -----
@voiture_api.route('/', methods=['GET'])
def getVoiture():  # Permet d'obtenir le dernier état de la voiture
    voitureData = dbVoiture.getVoiture()
    status = {
        'vitesse': voitureData[1],
        'distance': voitureData[3],
        'nbPanneau': voitureData[4],
        'date': voitureData[2]
    }
    dictionnaire = [status]
    return jsonify(dictionnaire)


@voiture_api.route('/all', methods=['GET'])
def getVoitureAll():  # Permet d'obtenir tous les états de la voiture
    voitureData = dbVoiture.getVoitureAll()
    dictionnaire = []
    for voiture in voitureData:
        status = {
            'vitesse': voiture[1],
            'distance': voiture[3],
            'nbPanneau': voiture[4],
            'date': voiture[2],
            'nbDemarrage': voiture[5],
            'nbArret': voiture[6],
            'nbDetecSuccess': voiture[7],
            'nbDetecError': voiture[8],
        }
        dictionnaire.append(status)

    response = jsonify(dictionnaire)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@voiture_api.route('/vitesse', methods=['GET'])
def getVitesse():  # Permet d'obtenir la vitesse du dernier état de la voiture
    vitesseKmH = dbVoiture.getVoitureVitesse()
    dictionnaire = {
        'type': 'vitesse',
        'value': vitesseKmH
    }
    return jsonify(dictionnaire)


@voiture_api.route('/distance', methods=['GET'])
def getDistance():  # Permet d'obtenir la distance du dernier état de la voiture
    distanceKm = dbVoiture.getVoitureDistance()
    dictionnaire = {
        'type': 'distance',
        'value': distanceKm
    }
    return jsonify(dictionnaire)


@voiture_api.route('/panneau', methods=['GET'])
def getNbPanneau():  # Permet d'obtenir le nb pannrau du dernier état de la voiture
    nbPanneau = dbVoiture.getVoitureNbPanneau()
    dictionnaire = {
        'type': 'nbPanneau',
        'value': nbPanneau
    }
    return jsonify(dictionnaire)


# ---------- Method POST --------

@voiture_api.route('/', methods=['POST'])
def addStatusVoiture():  # Pour ajouter un status de la voiture dans la bdd avec une datetime
    voitureRequest = request.json
    print(voitureRequest);
    dbVoiture.insertVoiture((voitureRequest['vitesse'], voitureRequest['distance']
                             , voitureRequest['nbPanneau'], datetime.datetime.now(),voitureRequest['nbDemarrage'],
                             voitureRequest['nbArret'],voitureRequest['nbDetecError'],voitureRequest['nbDetecSuccess'] ))

    return voitureRequest


@voiture_api.route('/detec', methods=['POST'])
def addDetecVoiture():  # Pour ajouter un status de la voiture dans la bdd avec une datetime
    voitureRequest = request.json
    print(voitureRequest);
    dbVoiture.insertVoitureDetection((datetime.datetime.now(), voitureRequest['nbDetecError'],voitureRequest['nbDetecSuccess'] ))

    return voitureRequest


# ---------- Method PUT --------

@voiture_api.route('/vitesse', methods=['PUT'])
def setVitesse():  # Pour modifier la vitesse d'un status
    voitureRequest = request.json

    dbVoiture.setVoiture((voitureRequest['vitesse'], voitureRequest['id']))

    return voitureRequest


@voiture_api.route('/distance', methods=['PUT'])
def setDistance():  # Pour modifier la distance d'un status
    voitureRequest = request.json

    dbVoiture.setVoiture((voitureRequest['distance'], voitureRequest['id']))

    return voitureRequest


@voiture_api.route('/nbPanneau', methods=['PUT'])
def setNbPanneau():  # Pour modifier le nb de panneaux d'un status
    voitureRequest = request.json

    dbVoiture.setVoiture((voitureRequest['nbPanneau'], voitureRequest['id']))

    return voitureRequest


@voiture_api.route('/mock', methods=['POST'])
def mockStatus():  # Pour ajouter un status de la voiture dans la bdd avec une datetime
    voitureRequest = [{
        "vitesse": 29.9,
        "distance": 12,
        "nbPanneau": 87,
        "date": "2020-12-10 17:51:47"
    }, {
        "vitesse": 12.3,
        "distance": 75,
        "nbPanneau": 6,
        "date": "2020-12-16 13:33:28"
    }, {
        "vitesse": 29.2,
        "distance": 52,
        "nbPanneau": 84,
        "date": "2020-12-23 17:47:04"
    }, {
        "vitesse": 17.6,
        "distance": 88,
        "nbPanneau": 32,
        "date": "2020-12-24 17:04:17"
    }, {
        "vitesse": 15.8,
        "distance": 71,
        "nbPanneau": 74,
        "date": "2020-12-23 00:52:29"
    }, {
        "vitesse": 27.7,
        "distance": 42,
        "nbPanneau": 11,
        "date": "2020-12-28 00:37:55"
    }, {
        "vitesse": 16.0,
        "distance": 20,
        "nbPanneau": 51,
        "date": "2020-12-15 20:22:18"
    }, {
        "vitesse": 38.5,
        "distance": 74,
        "nbPanneau": 24,
        "date": "2020-12-21 06:48:03"
    }, {
        "vitesse": 30.0,
        "distance": 26,
        "nbPanneau": 85,
        "date": "2020-12-02 20:48:22"
    }, {
        "vitesse": 12.7,
        "distance": 53,
        "nbPanneau": 25,
        "date": "2020-12-01 14:33:06"
    }, {
        "vitesse": 13.4,
        "distance": 86,
        "nbPanneau": 41,
        "date": "2020-12-21 09:41:16"
    }, {
        "vitesse": 28.5,
        "distance": 63,
        "nbPanneau": 79,
        "date": "2020-12-19 10:34:28"
    }, {
        "vitesse": 29.0,
        "distance": 67,
        "nbPanneau": 26,
        "date": "2020-12-25 23:41:00"
    }, {
        "vitesse": 14.7,
        "distance": 72,
        "nbPanneau": 7,
        "date": "2021-01-02 15:44:20"
    }, {
        "vitesse": 30.7,
        "distance": 43,
        "nbPanneau": 74,
        "date": "2020-12-26 12:42:18"
    }, {
        "vitesse": 15.2,
        "distance": 74,
        "nbPanneau": 39,
        "date": "2020-12-03 08:46:46"
    }, {
        "vitesse": 33.7,
        "distance": 40,
        "nbPanneau": 23,
        "date": "2020-12-07 09:50:42"
    }, {
        "vitesse": 19.4,
        "distance": 21,
        "nbPanneau": 28,
        "date": "2020-12-31 17:05:33"
    }, {
        "vitesse": 22.4,
        "distance": 83,
        "nbPanneau": 81,
        "date": "2020-12-06 20:50:20"
    }, {
        "vitesse": 35.4,
        "distance": 66,
        "nbPanneau": 11,
        "date": "2020-12-08 14:37:55"
    }, {
        "vitesse": 21.9,
        "distance": 15,
        "nbPanneau": 77,
        "date": "2020-12-25 21:59:37"
    }, {
        "vitesse": 34.7,
        "distance": 100,
        "nbPanneau": 82,
        "date": "2020-12-16 19:39:21"
    }, {
        "vitesse": 25.1,
        "distance": 42,
        "nbPanneau": 6,
        "date": "2020-12-20 12:24:50"
    }, {
        "vitesse": 23.1,
        "distance": 16,
        "nbPanneau": 57,
        "date": "2020-12-28 22:49:12"
    }, {
        "vitesse": 29.4,
        "distance": 12,
        "nbPanneau": 81,
        "date": "2020-12-27 19:16:37"
    }, {
        "vitesse": 31.9,
        "distance": 58,
        "nbPanneau": 42,
        "date": "2021-01-04 06:39:05"
    }, {
        "vitesse": 27.2,
        "distance": 99,
        "nbPanneau": 62,
        "date": "2020-12-02 19:48:50"
    }, {
        "vitesse": 31.3,
        "distance": 61,
        "nbPanneau": 93,
        "date": "2020-12-20 23:00:30"
    }, {
        "vitesse": 32.2,
        "distance": 71,
        "nbPanneau": 44,
        "date": "2020-12-30 07:08:56"
    }, {
        "vitesse": 25.2,
        "distance": 3,
        "nbPanneau": 19,
        "date": "2020-12-20 14:23:47"
    }]

    for voiture in voitureRequest:
        print(voiture)
        dbVoiture.insertVoiture((voiture['vitesse'], voiture['distance']
                                 , voiture['nbPanneau'], voiture['date']))
    return "Fait"
