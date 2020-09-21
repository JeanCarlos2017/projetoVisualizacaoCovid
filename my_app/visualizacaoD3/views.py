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

class LineChart(MethodView):
    def get(self):
        apiCovid = APICovid()
        dados_covid_dia = apiCovid.getDadosPorData()
        dados_covid_semanal = apiCovid.buscaDadosTodasSemana()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('LineChart.html',
                                             dados_covid=dados_covid_dia, dados_covid_semanal=dados_covid_semanal),
                             200, headers)


hello_view = HelloWorld.as_view('HelloWorld')
app.add_url_rule(
    '/hello', view_func=hello_view, methods=['GET']
)


bbChart_view = BubbleChart.as_view('BubbleChart')
app.add_url_rule(
    '/bb', view_func=bbChart_view, methods=['GET']
)

lineChart_view = LineChart.as_view('LineChart')
app.add_url_rule(
    '/line', view_func=lineChart_view, methods=['GET']
)

