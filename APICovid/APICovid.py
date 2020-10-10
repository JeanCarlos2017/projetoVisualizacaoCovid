import requests
from datetime import date,  timedelta
import datetime
import json

class APICovid:
    def __init__(self):
        self.URL_API = "https://api.apify.com/v2/datasets/3S2T1ZBxB9zhRJTBB/items?format=json&clean=1"
        self.dados_covid_dia= {}
        self.dados_covid_semanal={}
        self.dados_todos_dias={}

    def retornaDados(self):
        response = requests.get(self.URL_API)
        if response.status_code == 200:
            return response.json()

    #método para teste simples
    def getDadosPorData(self):
        self.dados_covid_dia = self.retornaDados()
        data_atual = datetime.datetime(2020, 6, 9)
        dados_data = self.buscaDadosPorData(data_atual)
        if dados_data == None:
            return self.erroDiaNaoEncontrado(dados_data)
        else:
            return dados_data

    #retorna dados da data especificada
    def buscaDadosPorData(self, data):
        string_data = data.strftime("%Y-%m-%d")
        for x in self.dados_covid_dia:
            if string_data in x.get('lastUpdatedAtSource'):
                return x



    #mensagem de erro: dado nao encontrado
    def erroDiaNaoEncontrado(self, data):
        #a API pula alguns dias
        return {'erro': 'dia {} não encontrado na API nos desculpe por isso '.format(data.strftime("%Y-%m-%d"))}

    #retorna a quantidade de infectados e mortos na semana
    def buscaDadosPorSemana(self, primeiro_dia_semana, qntDias=7):
        # retorna a quantidade de infectados e mortos  da semana
        dicionario = {'infected': 0, 'deceased': 0}
        # caso a semana tenha se encerrado são 7 dias, do contrário ver quantos dias ainda restam
        ultimo_dia = primeiro_dia_semana + timedelta(days=qntDias)
        # obtem os dados do primeiro e ultimo dia da semana
        dados_primeiro_dia = self.buscaDadosPorData(primeiro_dia_semana)

        if (dados_primeiro_dia == None):
            return self.erroDiaNaoEncontrado(primeiro_dia_semana)
        dados_ultimo_dia = self.buscaDadosPorData(ultimo_dia)

        if (dados_ultimo_dia == None):
            return self.erroDiaNaoEncontrado(ultimo_dia)

        for item in dicionario:
            # subtrai os dados do ultimo dia com o primeiro dia da semana para saber os dados desse período
            dados_semana = dados_ultimo_dia.get(item) - dados_primeiro_dia.get(item)
            dicionario[item] = dados_semana
        return dicionario

    def buscaDadosTodasSemana(self):
        # retorna um dicionário com os dados de todas as semanas
        data_final = datetime.datetime.now()
        contador_semana = 12
        data_inicio = datetime.datetime(2020, 3, 14)  # fim da primeira semana
        while (data_final >= data_inicio + timedelta(days=7)):
            self.dados_covid_semanal[contador_semana] = self.buscaDadosPorSemana(data_inicio)
            data_inicio += timedelta(days=7)
            contador_semana += 1
        return self.dados_covid_semanal


if __name__ == '__main__':
    dadosAPI =  APICovid()
    print(dadosAPI.getDadosPorData())
    print(dadosAPI.buscaDadosTodasSemana())