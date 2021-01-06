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

