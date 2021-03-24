from flask import render_template, Blueprint

dashboard_api = Blueprint('dashboard_api', __name__)


@dashboard_api.route('/')
def index():
    return render_template('index.html')


@dashboard_api.route('/vitesse')
def vitesse():
    return render_template('detail.html', typeChart='vitesse')


@dashboard_api.route('/distance')
def distance():
    return render_template('detail.html', typeChart='distance')


@dashboard_api.route('/panneau')
def panneau():
    return render_template('detail.html', typeChart='nbPanneau')


@dashboard_api.route('/demarrage')
def demarrage():
    return render_template('detail.html', typeChart='nbDemarrage')


@dashboard_api.route('/arret')
def arret():
    return render_template('detail.html', typeChart='nbArret')


@dashboard_api.route('/succes')
def succes():
    return render_template('detail.html', typeChart='nbDetecSuccess')


@dashboard_api.route('/erreur')
def erreur():
    return render_template('detail.html', typeChart='nbDetecError')

@dashboard_api.route('/temperature')
def temperature():
    return render_template('detailsIOT.html', typeChart='temperature')

@dashboard_api.route('/hygrometrie')
def hygrometrie():
    return render_template('detailsIOT.html', typeChart='hygrometrie')

@dashboard_api.route('/lumiere')
def lumiere():
    return render_template('detailsIOT.html', typeChart='luminosite')
