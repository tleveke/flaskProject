from flask import render_template, Blueprint
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json

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
