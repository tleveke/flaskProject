from flask import Flask, redirect, url_for
from webservice.route.voiture import voiture_api
from webservice.route.dashboard import dashboard_api

app = Flask(__name__,static_url_path='/static')


@app.route('/')
def index():
    return redirect('dashboard')


app.register_blueprint(dashboard_api, url_prefix='/dashboard')
app.register_blueprint(voiture_api, url_prefix='/api/voiture')
if __name__ == '__main__':
    app.run()
