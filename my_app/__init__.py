from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import os


#app = Flask(__name__, static_url_path="/static", static_folder='/my_app/visualizacaoD3/static>',  template_folder='templates')
app = Flask(__name__)
app.debug = True
app._static_folder = os.path.abspath("static/")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/appCovid19.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#api = Api(app)

from my_app.visualizacaoD3.views import catalog
db = SQLAlchemy(app)

#print('Print {}'.format(app.static_folder))

app.register_blueprint(catalog)

db.create_all()