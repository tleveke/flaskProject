from flask import Flask, redirect, url_for
from webservice.route.voiture_route import voiture_api
from webservice.route.dashboard import dashboard_api
from flask_cors import CORS

app = Flask(__name__,static_url_path='/static')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})



@app.route('/')
def index():
    return redirect('dashboard')


app.register_blueprint(dashboard_api, url_prefix='/dashboard')
app.register_blueprint(voiture_api, url_prefix='/api/voiture')
if __name__ == '__main__':
    app.run(host="0.0.0.0")
