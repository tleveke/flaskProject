import sqlite3


class VoitureModel():
    def __init__(self, voiture):
        self.vitesse = voiture.get('vitesse',None)
        self.distance = voiture.get('distance',None)
        self.nbPanneau = voiture.get('nbPanneau',None)
        self.date = voiture.get('date',None)
        self.nbDemarrage = voiture.get('nbDemarrage',None)
        self.nbArret = voiture.get('nbArret',None)
        self.nbDetecError = voiture.get('nbDetecError',None)
        self.nbDetecSuccess = voiture.get('nbDetecSuccess',None)
        self.temperature = voiture.get('temperature',None)
        self.hygrometrie = voiture.get('hygrometrie',None)
        self.luminosite = voiture.get('luminosite',None)

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        return {
            "vitesse": self.vitesse,
            "distance": self.distance,
            "nbPanneau": self.nbPanneau,
            "date": self.date,
            "nbDemarrage": self.nbDemarrage,
            "nbArret": self.nbArret,
            "nbDetecError": self.nbDetecError,
            "nbDetecSuccess": self.nbDetecSuccess,
            "temperature": self.temperature,
            "hygrometrie": self.hygrometrie,
            "luminosite": self.luminosite,
        }

    @property
    def serialized_add(self):
        """Return object data in serializeable format for Insert/Update in Sqlite3"""
        return (
            self.vitesse,
            self.distance,
            self.nbPanneau,
            self.date,
            self.nbDemarrage,
            self.nbArret,
            self.nbDetecError,
            self.nbDetecSuccess,
            self.temperature,
            self.hygrometrie,
            self.luminosite
        )
