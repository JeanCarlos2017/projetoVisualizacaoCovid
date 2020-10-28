from Python.PreVisualizacao.DadosCovid import DadosCovid
from datetime import date,  timedelta
import datetime

class DadosBarChart:
    #classe  responsável  por tratar os dados e passá-los para as visualizações baseadas no BarChart
    def __init__(self):
        self.dadosCovid = DadosCovid()

    def dadosItemDicionario(self, data, valor):
        #forma um item do dicionario
        return {'date': data, 'value': valor}


    def dadosBarChartAux(self, item, dados):
        #dados = self.dadosCovid.getDadosDiarios()
        dados_bar_chart = {}
        for x in dados:
            if dados[x]!= None:
                dados_bar_chart[x] = self.dadosItemDicionario(dados[x].get('data'), dados[x].get(item))
        return dados_bar_chart

    def dadosBarChart(self, item, semanal):
        #função que refina os dados para as visualizações semanais e diárias
        if semanal == True:
            dados = self.dadosCovid.getDadosSemanal()
        else:
            dados = self.dadosCovid.getDadosDiarios()
        return self.dadosBarChartAux(item, dados)

if __name__ == '__main__':
    preVis = DadosBarChart()
    print(preVis.dadosBarChart('infected', True))
    print(preVis.dadosBarChart('infected', False))