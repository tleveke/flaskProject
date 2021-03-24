CREATE TABLE IF NOT EXISTS 'etat' (
    'vitesse' INTEGER,
    'distance' INTEGER,
    'nbPanneau' INTEGER,
    'date' INTEGER,
    'nbDemarrage' INTEGER,
    'nbArret' INTEGER,
    'nbDetecSuccess' INTEGER,
    'nbDetecError' INTEGER,
    'temperature' INTEGER,
    'hygrometrie' INTEGER,
    'luminosite' INTEGER,
    'proximite' INTEGER
);

DROP TABLE IF EXISTS 'etat';
    CREATE TABLE 'etat'(
        'vitesse' INTEGER,
        'distance' INTEGER,
        'nbPanneau' INTEGER,
        'date' INTEGER,
        'nbDemarrage' INTEGER,
        'nbArret' INTEGER,
        'nbDetecSuccess' INTEGER,
        'nbDetecError' INTEGER,
        'temperature' INTEGER,
        'hygrometrie' INTEGER,
        'luminosite' INTEGER,
        'proximite' INTEGER
    );
