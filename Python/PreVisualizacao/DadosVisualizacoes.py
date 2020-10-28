from Python.PreVisualizacao.DadosBarChart import DadosBarChart

class DadosVisualizacoes:
    #classe responsável por retornar os dados refinados de todas as visualizações
    def __init__(self):
        self.dadosBarChart = DadosBarChart()

    def getDadosBarChart(self, item, semanal ):
        return self.dadosBarChart.dadosBarChart(item=item, semanal=semanal)


if __name__ == '__main__':
    dados = DadosVisualizacoes()
    print(dados.getDadosBarChart('infected', True))
    print(dados.getDadosBarChart('infected', False))