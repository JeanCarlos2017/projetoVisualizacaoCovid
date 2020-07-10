from flask import Flask, render_template, make_response
from flask_restful import Resource, Api


#app = Flask('projetoVisualizacaoCovid') #usar o __name__ não é uma boa prática
app = Flask(__name__)
api = Api(app)


@app.route("/flask") #funciona!
def index():
    return render_template("testModel.html")


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class BubbleChart(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('testModel.html'), 200, headers)
        #return render_template("index.html")
        #return render_template("bbChart.html")
        #return render_template('testModel.html')


api.add_resource(HelloWorld, '/hello')
api.add_resource(BubbleChart, '/')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)