from flask import Blueprint
from my_app.visualizacaoD3.views import HelloWorld

#rotas para helloworld
bp = Blueprint("bp", __name__, template_folder="templates")
bp.static_folder(__name__, static_folder='static')
#bp = Blueprint("bp", __name__, static_folder='static')





