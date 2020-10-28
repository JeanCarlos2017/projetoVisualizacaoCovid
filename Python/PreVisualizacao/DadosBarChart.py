from  Python.PreVisualizacao.DadosCovid import DadosCovid
from datetime import date,  timedelta
import datetime

class DadosBarChart:
    #classe  responsável  por tratar os dados e passá-los para as visualizações baseadas no BarChart
    def __init__(self):
        self.dadosCovid = DadosCovid()

    def dadosItemDicionario(self, data, valor):
        #forma um item do dicionario
        return {'date': data, 'value': valor}


    def dadosBarChartDiario(self, item):
        dados_diarios = self.dadosCovid.getDadosDiarios()
        dados_bar_chart = {}
        for x in dados_diarios:
            dados_bar_chart[x] = self.dadosItemDicionario(dados_diarios[x].get('data'), dados_diarios[x].get(item))
        return dados_bar_chart


if __name__ == '__main__':
    preVis = DadosBarChart()
    print(preVis.dadosBarChartDiario('infected'))
