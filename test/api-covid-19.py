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



if __name__ == '__main__':
    URL_DADOS_ATUAL = "https://api.apify.com/v2/datasets/3S2T1ZBxB9zhRJTBB/items?format=json&clean=1"
    DADOS_COVID = retornaDados()
    string_data_atual = date.today().strftime("%Y-%m-%d")
    print(buscaDadosPorData(string_data_atual))


