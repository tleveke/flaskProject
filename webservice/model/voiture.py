import sqlite3


class Voiture:
    conn = None

    def __init__(self):
        self.conn = sqlite3.connect('voiture.db', check_same_thread=False)

    # Function Select

    def getVoitureAll(self):
        c = self.conn.cursor()
        voiture = c.execute('SELECT * FROM etat order by date').fetchall()
        return voiture

    def getVoiture(self):
        c = self.conn.cursor()
        voiture = c.execute('SELECT * FROM etat order by date desc').fetchone()
        print(voiture)
        return voiture

    def getVoitureVitesse(self):
        c = self.conn.cursor()
        vitesse = c.execute('SELECT vitesse FROM etat order by date desc').fetchone()
        return vitesse[0]

    def getVoitureDistance(self):
        c = self.conn.cursor()
        distance = c.execute('SELECT distance FROM etat order by date desc').fetchone()
        return distance[0]

    def getVoitureNbPanneau(self):
        c = self.conn.cursor()
        nbPanneau = c.execute('SELECT nbPanneau FROM etat order by date desc').fetchone()
        return nbPanneau[0]

    # Function Insert

    def insertVoiture(self, voiture):
        c = self.conn.cursor()

        print(voiture)
        c.execute(''' Insert into etat(vitesse, distance, nbPanneau,date,nbDemarrage,nbArret,nbDetecError,nbDetecSuccess) 
        values(?,?,?,?,?,?,?,?)''', voiture)

        self.conn.commit()

        c.close()

    def insertVoitureDetection(self, voiture):
        c = self.conn.cursor()

        print(voiture)
        c.execute(''' Insert into etat(date,nbDetecError,nbDetecSuccess) 
        values(?,?,?)''', voiture)

        self.conn.commit()

        c.close()

    # Function Update

    def setVitesse(self, voiture):
        c = self.conn.cursor()

        c.execute(''' UPDATE etat
              SET vitesse = ?
              WHERE id = ?''', voiture)

        self.conn.commit()

        c.close()

    def setDistance(self, voiture):
        c = self.conn.cursor()

        c.execute(''' UPDATE etat
              SET distance = ?
              WHERE id = ?''', voiture)

        self.conn.commit()

        c.close()

    def setNbPanneau(self, voiture):
        c = self.conn.cursor()

        c.execute(''' UPDATE etat
              SET nbPanneau = ?
              WHERE id = ?''', voiture)

        self.conn.commit()

        c.close()
