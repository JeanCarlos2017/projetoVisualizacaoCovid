from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/appCovid19.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#api = Api(app)

from my_app.visualizacaoD3.views import catalog
db = SQLAlchemy(app)

app.register_blueprint(catalog)

db.create_all()