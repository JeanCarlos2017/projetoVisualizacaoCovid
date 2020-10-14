from flask import Flask, render_template, make_response, Blueprint,jsonify
from flask.views import MethodView
from my_app import app
from APICovid.APICovid import APICovid
import os


#catalogo de visualizacao
catalog = Blueprint("catalog", 'visualizacaoD3', template_folder='templates', static_folder='static')


@app.errorhandler(404)
def page_not_found(error):
    return "erro, página não encontrada"


@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."


@catalog.route('/worldGeoJson')
def WorldGeoJson():
    with app.open_resource('static/datasets/world.geojson') as f:
       return f.read()


@catalog.route('/brazilGeoJson')
def BrasilGeoJson():
    with app.open_resource('static/datasets/brasil.geojson') as f:
        return f.read()


class HelloWorld(MethodView):
    def get(self):
        return 'hello world'


class BubbleChart(MethodView):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('testModel.html'), 200, headers)


class Home(MethodView):
    def get(self):
        apiCovid = APICovid()
        apiCovid.retornaInfectadosEMortos()
        apiCovid.buscaDadosDiaDia()
        dados_covid_semanal = apiCovid.buscaDadosTodasSemana() #dicionário a quantidade de infectados e mortos acumulados semanalmente
        dados_acumulados = apiCovid.dados_covid_refinado #dicionário a quantidade de infectados e mortos acumulados
        dados_diarios = apiCovid.dados_todos_dias #dicionário com a quantidade de infectados e mortos de todos os dias

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html', dados_diarios= dados_diarios,
                                             dados_acumulados=dados_acumulados, dados_covid_semanal=dados_covid_semanal),
                             200, headers)


hello_view = HelloWorld.as_view('HelloWorld')
app.add_url_rule(
    '/hello', view_func=hello_view, methods=['GET']
)


bbChart_view = BubbleChart.as_view('BubbleChart')
app.add_url_rule(
    '/bb', view_func=bbChart_view, methods=['GET']
)

lineChart_view = Home.as_view('LineChart')
app.add_url_rule(
    '/', view_func=lineChart_view, methods=['GET']
)

