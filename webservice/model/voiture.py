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

    def getVoitureTemperature(self):
        c = self.conn.cursor()
        temperature = c.execute('SELECT temperature FROM etat order by date desc').fetchone()
        return temperature[0]


    def getVoitureHygrometrie(self):
        c = self.conn.cursor()
        hygrometrie = c.execute('SELECT hygrometrie FROM etat order by date desc').fetchone()
        return hygrometrie[0]


    def getVoitureLuminosite(self):
        c = self.conn.cursor()
        luminosite = c.execute('SELECT luminosite FROM etat order by date desc').fetchone()
        return luminosite[0]


    def get_voiture_all_temperature(self):
        c = self.conn.cursor()
        temperature = c.execute('SELECT temperature, date   FROM etat order by date desc').fetchall()
        return temperature

    def getVoiture_all_hygrometrie(self):
        c = self.conn.cursor()
        hygrometrie = c.execute('SELECT hygrometrie , date FROM etat order by date desc').fetchall()
        return hygrometrie

    def getVoiture_all_luminosite(self):
        c = self.conn.cursor()
        luminosite = c.execute('SELECT luminosite, date FROM etat order by date desc').fetchall()
        return luminosite

    # Function Insert

    def insertVoiture(self, voiture):
        c = self.conn.cursor()

        print(voiture)
        c.execute(''' Insert into etat(vitesse, distance, nbPanneau,date,nbDemarrage,nbArret,nbDetecError,nbDetecSuccess, temperature, hygrometrie, luminosite) 
        values(?,?,?,?,?,?,?,?,?,?,?)''', voiture)

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