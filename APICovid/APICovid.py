import requests
from datetime import date,  timedelta
import datetime
import json

class APICovid:
    def __init__(self):
        self.URL_API = "https://api.apify.com/v2/datasets/3S2T1ZBxB9zhRJTBB/items?format=json&clean=1"
        self.dados_covid= {}

    def retornaDados(self):
        response = requests.get(self.URL_API)
        if response.status_code == 200:
            return response.json()


    def buscaDadosPorData(self, data):
        string_data = data.strftime("%Y-%m-%d")
        for x in self.dados_covid:
            if string_data in x.get('lastUpdatedAtSource'):
                return x


    def getDadosPorData(self):
        self.dados_covid = self.retornaDados()
        data_atual = datetime.datetime(2020, 6, 9)
        dados_data = self.buscaDadosPorData(data_atual)
        if dados_data == None:
            error_message = {'Erro: ': 'Dados não encontrados na API, retornando lista vazia!'}
            return error_message
        else:
            return dados_data


if __name__ == '__main__':
    dadosAPI =  APICovid()
    print(dadosAPI.getDadosPorData())