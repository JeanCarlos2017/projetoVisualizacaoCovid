# visualizacaoCovid--Python--Flask-RESTful--D3.js

Aplicação conterá visualizações dos dados sobre Covid-19 em tempo real. Para tanto será usado a linguagem Python com a extensão do micro-framework Flask - o  FlaskRESTfull - e a biblioteca JavaScript D3.js 

## Instalação 
Para usar o programa é necessário ter o Python  instalado em sua máquina, e saber usar uma virtualenv.
### Instalando o Python 
 Acesse o site do [Python](https://www.python.org/downloads/) e faça o download da versão desejada. Caso tenha dúvidas verifique a [documentação do Python](https://www.python.org/doc/)  

### Com o o Python instalado faça as seguintes etapas: 
#### 1° Clone o repositório: 
 Para clonar o repositório abra o prompt comando e digite os comandos: 
 ``````
 cd /minha/pasta/de/projetos/
 git clone https://github.com/JeanCarlos2017/projetoVisualizacaoCovid--Python--Flask-RESTful.git
 cd visualizacaoCovid--Python--Flask-RESTful--D3.js
 ``````
 Caso tenha dúvidas com o GitHub veja um tutorial simples [clicando aqui](https://docs.github.com/pt/enterprise/2.16/user/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
 #### 2° Instale as extensões:
  ``````````
  pip install -r requirements.txt
  ``````````
  Caso tenha dúvidas sobre virtualenv e o pip veja um post explicativo [clicando aqui](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais)
 #### 3° Execute a api
   Execute o arquivo <b> run.py </b> com o Python, ou se preferir use a IDE e sua preferência
  
 <b> Observação: ter acesso as visualizações gráficas é necessário conexão com a internet, porque o projeto usa uma importação remota da biblioteca D3.js, além do uso da API com os ddados do Covid </b>
 
 
 ## Construído com 
 [Python](https://www.python.org/) </br>
 
 [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)</br>
 
 [D3.js](https://d3js.org/)</br>
 
 Para ter acesso a API com os dados do Covid-19 clique [aqui](https://api.apify.com/v2/datasets/3S2T1ZBxB9zhRJTBB/items?format=json&clean=1)
 

 
   
