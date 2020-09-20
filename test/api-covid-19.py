import requests
from datetime import date,  timedelta
import datetime

def retornaDados():
    response = requests.get(URL_DADOS_ATUAL)
    if response.status_code == 200:
        return response.json()


def buscaDadosPorData(data):
    dados_covid = DADOS_COVID
    string_data = data.strftime("%Y-%m-%d")
    for x in dados_covid:
        if string_data in x.get('lastUpdatedAtSource'):
            return x

def buscaDadosPorSemana(primeiro_dia, qntDias = 7):
    #retorna a quantidade de infectados e mortos  da semana
    dicionario = {'infected': 0, 'deceased': 0}
    #caso a semana tenha se encerrado são 7 dias, do contrário ver quantos dias ainda restam
    ultimo_dia = primeiro_dia + timedelta(days= qntDias)
    #obtem os dados do primeiro e ultimo dia da semana
    dados_primeiro_dia = buscaDadosPorData(primeiro_dia)
    if (dados_primeiro_dia == None):
        #a API pula alguns dias por isso faço a verificação
        return {'erro' : 'dia {} não encontrado na API nos desculpe por isso '.format(primeiro_dia.strftime("%Y-%m-%d"))}
    dados_ultimo_dia = buscaDadosPorData(ultimo_dia)
    if (dados_ultimo_dia == None):
        return {'erro': 'dia {} não encontrado na API nos desculpe por isso '.format(ultimo_dia.strftime("%Y-%m-%d"))}
    for item in dicionario:
        #subtrai os dados do ultimo dia com o primeiro dia da semana para saber os dados desse período
        dados_semana = dados_ultimo_dia.get(item) - dados_primeiro_dia.get(item)
        dicionario[item] = dados_semana
    return dicionario


if __name__ == '__main__':
    URL_DADOS_ATUAL = "https://api.apify.com/v2/datasets/3S2T1ZBxB9zhRJTBB/items?format=json&clean=1"
    DADOS_COVID = retornaDados()
    data_atual = datetime.datetime(2020, 6, 6)
    if buscaDadosPorData(data_atual) == None:
        print("lista vazia")
    else:
        print(buscaDadosPorData(data_atual))
    # testando pegar dados de uma semana do dia 13/09 ao 19/09
    data_test_semana = datetime.datetime(2020, 9, 12)
    print(buscaDadosPorSemana(data_test_semana))




