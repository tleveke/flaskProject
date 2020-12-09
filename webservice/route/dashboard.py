from flask import render_template, Blueprint
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json


dashboard_api = Blueprint('dashboard_api', __name__)


@dashboard_api.route('/')
def index():

    bar = create_plot()
    return render_template('index.html', plot=bar)


def create_plot():


    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

