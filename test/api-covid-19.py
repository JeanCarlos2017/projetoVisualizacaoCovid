import requests
from datetime import date,  timedelta, datetime

def retornaDados():
    response = requests.get(URL_DADOS_ATUAL)
    if response.status_code == 200:
        return response.json()


def buscaDadosPorData(data):
    dados_covid = DADOS_COVID
    for x in dados_covid:
        if data in x.get('lastUpdatedAtSource'):
            return x

def buscaDadosPorSemana(diaIni, dicionario, qntDias = 7):
    #retorna a quantidade de infectados, mortos e recuperados da semana
    ultimo_dia = diaIni + timedelta(days= qntDias)
    string_ultimo_dia = ultimo_dia.strftime("%Y-%m-%d")
    string_primeiro_dia = diaIni.strftime("%Y-%m-%d")
    #obtem os dados do primeiro e ultimo dia da semana
    dados_primeiro_dia = buscaDadosPorData(string_primeiro_dia)
    dados_ultimo_dia = buscaDadosPorData(string_ultimo_dia)
    for item in dicionario:
        #subtrai os dados do ultimo dia com o primeiro dia da semana para saber os dados desse período
        dados_semana = dados_ultimo_dia.get(item) - dados_primeiro_dia.get(item)
        dicionario[item] = dados_semana

    return dicionario


if __name__ == '__main__':
    URL_DADOS_ATUAL = "https://api.apify.com/v2/datasets/3S2T1ZBxB9zhRJTBB/items?format=json&clean=1"
    DADOS_COVID = retornaDados()
    string_data_atual = date.today().strftime("%Y-%m-%d")
    # print(buscaDadosPorData(string_data_atual))
    # testando pegar dados de uma semana do dia 13/09 ao 19/09
    data_test_semana = datetime.strptime('2020-09-12', '%Y-%m-%d')
    dicionario = {'infected': 0, 'deceased': 0, 'recovered': 0}
    print(buscaDadosPorSemana(data_test_semana, dicionario))


