from Python.APICovid.APICovid import APICovid

class DadosCovid:
    def __init__(self):
        apiCovid = APICovid()
        apiCovid.retornaInfectadosEMortos()
        apiCovid.buscaDadosDiaDia()
        # dicionário a quantidade de infectados e mortos acumulados semanalmente
        self.dados_covid_semanal = apiCovid.buscaDadosTodasSemana()
        # dicionário a quantidade de infectados e mortos acumulados
        self.dados_acumulados = apiCovid.dados_covid_refinado
        # dicionário com a quantidade de infectados e mortos de todos os dias
        self.dados_diarios = apiCovid.dados_todos_dias

    def getDadosDiarios(self):
        return self.dados_diarios

    def getDadosSemanal(self):
        return self.dados_covid_semanal

    def getDadosAcumulados(self):
        return self.dados_acumulados


if __name__ == '__main__':
    dados_covid = DadosCovid()
    print(dados_covid.getDadosSemanal())
    print(dados_covid.getDadosDiarios())
    print(dados_covid.getDadosAcumulados())