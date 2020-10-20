import requests
from datetime import date,  timedelta
import datetime
import json

class APICovid:
    def __init__(self):
        self.URL_API = "https://api.apify.com/v2/datasets/3S2T1ZBxB9zhRJTBB/items?format=json&clean=1"
        self.dados_covid_semanal={}
        self.dados_todos_dias={} #quantidade de casos novos dia a dia
        self.dados_covid = self.retornaDados()
        self.dados_covid_refinado = {} #quantidade  acumulada dos infectados e mortos

    def retornaDados(self):
        response = requests.get(self.URL_API)
        if response.status_code == 200:
            return response.json()

    def refinaDadosJSON(self, dados_diario, data):
        dicionario = {'infected': 0, 'deceased': 0}
        for item in dicionario:
            # print("item {} :: dados_item :: {}".format(item, dados_diario.get(item)))
            dicionario[item] = dados_diario.get(item)
        dicionario['data'] = data
        return dicionario

    #retorna em um dicionário a quantidade de infectados e mortos acumulados
    def retornaInfectadosEMortos(self):
        contador_dia = 0
        data_final = datetime.datetime.now()
        data_inicio = datetime.datetime(2020, 3, 14)
        while (data_final >= data_inicio):
            dados_diario = self.buscaDadosPorData(data_inicio)
            if dados_diario != None:
                self.dados_covid_refinado[contador_dia] = self.refinaDadosJSON(dados_diario, data_inicio)
                contador_dia+=1
            data_inicio += timedelta(days=1)

    #método para teste simples
    def getDadosPorData(self):
        data_atual = datetime.datetime(2020, 6, 9)
        dados_data = self.buscaDadosPorData(data_atual)
        if dados_data == None:
            return self.erroDiaNaoEncontrado(dados_data)
        else:
            return dados_data

    #retorna dados da data especificada
    def buscaDadosPorData(self, data):
        string_data = data.strftime("%Y-%m-%d")
        for x in self.dados_covid:
            if string_data in x.get('lastUpdatedAtSource'):
                return x

   # retorna a quantidade de infectados e mortos de todos os dias
    def buscaDadosDiaDia(self):
        self.retornaInfectadosEMortos() #dicionário a quantidade de infectados e mortos acumulados
        contador_dia = 0
        quantidade_dias = self.dados_covid_refinado.__len__()
        #print('quantidade de dias :: {}'.format(quantidade_dias))

        while (contador_dia < quantidade_dias-1):
            dados_anterior = self.dados_covid_refinado[contador_dia] # quantidade de infectados e mortos do dia anterior
            contador_dia+=1
            dados_atual = self.dados_covid_refinado[contador_dia] # quantidade de infectados e mortos do dia atual
            self.dados_todos_dias[contador_dia-1] =\
                    self.subtracaoDadosDiasDiferentes(dados_anterior, dados_atual)

    #mensagem de erro: dado nao encontrado
    def erroDiaNaoEncontrado(self, data):
        #a API pula alguns dias
        return {'erro': 'dia {} não encontrado na API nos desculpe por isso '.format(data.strftime("%Y-%m-%d"))}

    def subtracaoDadosDiasDiferentes(self, dados_primeiro_dia, dados_ultimo_dia):
        #usado para retornar os que surgiu no ultimo dia/semana, para isso é necessário comparar datas
        dicionario = {'infected': 0, 'deceased': 0}
        for item in dicionario:
            # subtrai os dados do ultimo dia com o primeiro dia da semana para saber os dados desse período
            dados_semana = int(dados_ultimo_dia.get(item) - dados_primeiro_dia.get(item))
            dicionario[item] = dados_semana
        return dicionario

    #retorna a quantidade de infectados e mortos na semana
    def buscaDadosPorSemana(self, primeiro_dia_semana, qntDias=7):
        # retorna a quantidade de infectados e mortos  da semana

        # caso a semana tenha se encerrado são 7 dias, do contrário ver quantos dias ainda restam
        ultimo_dia = primeiro_dia_semana + timedelta(days=qntDias)
        # obtem os dados do primeiro e ultimo dia da semana
        dados_primeiro_dia = self.buscaDadosPorData(primeiro_dia_semana)

        if (dados_primeiro_dia == None):
            return self.erroDiaNaoEncontrado(primeiro_dia_semana)
        dados_ultimo_dia = self.buscaDadosPorData(ultimo_dia)

        if (dados_ultimo_dia == None):
            return self.erroDiaNaoEncontrado(ultimo_dia)
        #compara a semana atual com a semana anterior para assim saber a quantidade de mostes e infectados que ocorreu na semana atual
        dicionario = self.subtracaoDadosDiasDiferentes(dados_primeiro_dia, dados_ultimo_dia)
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
    #retorna os dados de acordo com uma data
    #print(dadosAPI.getDadosPorData())

    #retorna a quantidade de casos que ocorreu a cada semana
    #print(dadosAPI.buscaDadosTodasSemana())
    #print(dadosAPI.dados_covid)

    #retorna a quantidade de casos que ocorreu no dia
    dadosAPI.retornaInfectadosEMortos()
    dadosAPI.buscaDadosDiaDia()
    print(dadosAPI.dados_todos_dias)

    #retorna os dados acumulados
    #dadosAPI.retornaInfectadosEMortos()
    #print(dadosAPI.dados_covid_refinado)