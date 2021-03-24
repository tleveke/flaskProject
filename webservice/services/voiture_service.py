import sqlite3
from datetime import datetime

from webservice.model.voiture_model import VoitureModel


class Voiture_service:
    conn = None

    def __init__(self):
        self.conn = sqlite3.connect('voiture.db', check_same_thread=False)
        self.conn.row_factory = self.dict_factory

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def convertVoiture(self, voiture):
        return VoitureModel(voiture)

    # Function Select

    def get_voiture_all(self):
        c = self.conn.cursor()
        voiture_all = c.execute('SELECT * FROM etat order by date').fetchall()
        c.close()
        return map(self.convertVoiture, voiture_all)

    # Function Insert

    def insert_voiture(self, voiture_json):
        c = self.conn.cursor()
        voiture_json['date'] = datetime.today()
        voiture = VoitureModel(voiture_json)
        c.execute(''' Insert into etat(vitesse, distance, nbPanneau,date,nbDemarrage,nbArret,
        nbDetecError,nbDetecSuccess, temperature, hygrometrie, luminosite) 
        values(?,?,?,?,?,?,?,?,?,?,?)''', voiture.serialized_add)

        self.conn.commit()

        c.close()
