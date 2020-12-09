import sqlite3


class Voiture:
    conn = None

    def __init__(self):
        self.conn = sqlite3.connect('voiture.db', check_same_thread=False)

    # Function Select

    def getVoiture(self):
        c = self.conn.cursor()
        voiture = c.execute('SELECT * FROM voiture').fetchone()
        print(voiture)
        return voiture

    def getVoitureVitesse(self):
        c = self.conn.cursor()
        vitesse = c.execute('SELECT vitesse FROM voiture').fetchone()
        return vitesse[0]

    def getVoitureDistance(self):
        c = self.conn.cursor()
        distance = c.execute('SELECT distance FROM voiture').fetchone()
        return distance[0]

    def getVoitureNbPanneau(self):
        c = self.conn.cursor()
        nbPanneau = c.execute('SELECT nbPanneau FROM voiture').fetchone()
        return nbPanneau[0]

    # Function Update

    def setVoiture(self, voiture):
        c = self.conn.cursor()

        c.execute(''' UPDATE voiture
              SET vitesse = ? ,
                  distance = ? ,
                  nbPanneau = ?
              WHERE id = ?''', voiture)

        self.conn.commit()

        c.close()

    def setVitesse(self, voiture):
        c = self.conn.cursor()

        c.execute(''' UPDATE voiture
              SET vitesse = ?
              WHERE id = ?''', voiture)

        self.conn.commit()

        c.close()

    def setDistance(self, voiture):
        c = self.conn.cursor()

        c.execute(''' UPDATE voiture
              SET distance = ?
              WHERE id = ?''', voiture)

        self.conn.commit()

        c.close()

    def setNbPanneau(self, voiture):
        c = self.conn.cursor()

        c.execute(''' UPDATE voiture
              SET nbPanneau = ?
              WHERE id = ?''', voiture)

        self.conn.commit()

        c.close()
