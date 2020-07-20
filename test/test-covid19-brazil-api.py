import requests
from datetime import date,  timedelta


def montaURL(local):
    #ultimoDia: monta a url para trazer os dados do último dia
    baseUrl = 'https://covid19-brazil-api.now.sh/api/report/v1/'

    # concatena url com os dados do local
    baseUrl = baseUrl + local['pais']
    if local['estado']:
        baseUrl = baseUrl + "/uf/" + local['estado']
    #concatena a data
    if local['data']:
        baseUrl += '/' + local['data']

    return baseUrl


def dadosTotaisCovid (local):
    #retorna os dados acumulados de um estado ou pais
    baseUrl = montaURL(local)
    response = requests.get(baseUrl)
    if response.status_code == 200:
        dados = response.json()
        results = dados.get('data', [])
        #print(results)
        if 'cases' in results:
            print(results['cases'])

        return results


def buscaDadosEstado (uf_estado, dados):
    for x in dados:
        if x.get('state') == uf_estado:
            return x


def dados24hCovid():
    #obtendo a data atual e do dia anterior
    data_atual = date.today()
    data_dia_anterior = data_atual - timedelta(days=1, hours=0, minutes=0)

    #mudando o formato da data para ficar de acordo com a api
    data_dia_anterior = data_dia_anterior.strftime('%Y%m%d')

    #criando o argumento
    local = {
        "pais": "brazil",
        "estado": "",
        "data": ""
    }
    # obtendo dados atuais
    dados_atual = dadosTotaisCovid(local)
    #print(dados_atual)

    #obtendos dados dia anterior
    local["data"] = str(data_dia_anterior)
    dados_dia_anterior = dadosTotaisCovid(local)
    dados_dia_anterior = buscaDadosEstado(local['estado'], dados_dia_anterior)

    print(dados_dia_anterior)
    print(dados_atual)


    #casos_ultimo_dia = dados_atual.get('cases') - dados_dia_anterior.get('cases')
    #print(casos_ultimo_dia)


def status_api ():
    pass


def status_conexao_usuario():
    #para teste local
    pass


if __name__ == '__main__':
    local = {
        "pais": "brazil",
        "estado": "sp",
    }

    dados24hCovid()
    #casosTotalCovid(local)


#API nao mostrou ser eficiente