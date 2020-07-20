from flask import Flask, render_template, make_response, Blueprint
from flask.views import MethodView
from my_app import app

#catalogo de visualizacao
catalog = Blueprint('catalog', __name__, template_folder='templates',
    static_folder='static')
                    #static_url_path='static/assets')

@app.errorhandler(404)
def page_not_found(error):
    return "erro, página não encontrada"
   #return render_template('page_not_found.html'), 404


@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."


class HelloWorld(MethodView):
    def get(self):
        return 'hello world'


class BubbleChart(MethodView):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('testModel.html'), 200, headers)


#api._blueprint_setup_add_url_rule_patch('/h', view_func=HelloWorld.as_view('hello_world'))
#app.add_url_rule('', view_func=HelloWorld.as_view('hello'))

hello_view = HelloWorld.as_view('HelloWorld')
app.add_url_rule(
    '/hello', view_func=hello_view, methods=['GET']
)



bbChart_view = BubbleChart.as_view('BubbleChart')
app.add_url_rule(
    '/bb', view_func=bbChart_view, methods=['GET']
)

