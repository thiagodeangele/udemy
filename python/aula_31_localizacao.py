import requests
import json
# import pprint

accuWeatherAPIKey = 'NzZHSUUOflMPJvNQJzH2WRYLuvbKSIPf'

def pegarCoordenadas():
    # Faz um requests.get e retorna um json com diversas informações sobre a requisição.
    r = requests.get('http://www.geoplugin.net/json.gp') 
    
    # Status 200 = Resposta bem sucedida
    if r.status_code != 200:
        mensagemErro('Não foi possível obter a localização')
        return None
    else:
        try:
            # Transforma o json em dicionário
            localizacao = json.loads(r.text)        
            coordenadas = dict()
            coordenadas['lat'] = localizacao['geoplugin_latitude']
            coordenadas['long'] = localizacao['geoplugin_longitude']
            # Retorna um dicionário com latitude e longitude
            return coordenadas
        
        except:
            return None

def pegarCodigoLocal(lat, long):
    
    # Pega o endereço (cURL) da aAPI do AccuWeather e substitui a API e a latitude e longitude, adquiridos da função 'pegarCoordenadas()'

    locationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuWeatherAPIKey + "&q=" + lat + "%2C%20" + long + "&language=pt-br"
    
    # Verifica se a conexão com o locationAPUUrl foi bem sucedida.
    r = requests.get(locationAPIUrl)
    if r.status_code != 200:
        mensagemErro('Não foi possível obter a localização')
        return None
    else:
        try:
            # Converte o json recebido do mlocationAPIUrl em dicionário.
            locationResponse = json.loads(r.text)
            infoLocal = dict()
            
            infoLocal['nomeLocal'] = locationResponse['LocalizedName'] + ', ' + locationResponse['AdministrativeArea']['LocalizedName'] + '. ' + locationResponse['Country']['LocalizedName']
            
            infoLocal['codigoLocal'] = locationResponse['Key']
            
            return infoLocal
        
        except:
            return None

def pegarTempoAgora(codigoLocal, nomeLocal): 
    
    # Usa a URL da API do AccuWeather substituindo pelas funções e chaves.
    currentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" + codigoLocal + "?apikey=" + accuWeatherAPIKey + "&language=pt-br"

    r = requests.get(currentConditionsAPIUrl)
    
    if r.status_code != 200:
        mensagemErro('Não foi possível Obter o Clima.')
        return None
    else:
        try:
            currentConditionsResponse = json.loads(r.text)
            infoClima = dict()
            infoClima['textoClima'] = currentConditionsResponse[0]['WeatherText']
            infoClima['temperatura'] = currentConditionsResponse[0]['Temperature']['Metric']['Value']
            infoClima['nomeLocal'] = nomeLocal
            return infoClima
        except:
            return None

def pegarPrevisao5Dias(codigoLocal): 
    
    # Usa a URL da API do AccuWeather substituindo pelas funções e chaves.
    dailyAPIUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + codigoLocal + "?apikey=" + accuWeatherAPIKey + "&language=pt-br&metric=true"

    r = requests.get(currentConditionsAPIUrl)
    
    if r.status_code != 200:
        mensagemErro('Não foi possível Obter o Clima.')
        return None
    else:
        try:
            dailyResponse = json.loads(r.text)
            infoClima5Dias = dict()

            for dia in dailyResponse['DailyForecasts']:
                climaDia = dict()
                climaDia['max'] = dia['Temperature']['Maximum']['Value']
                climaDia['min'] = dia['Temperature']['Minimum']['Value']
                climaDia['clima'] = dia['Day']['IconPhrase']
                climaDia['dia'] = dia['EpochDate']
                infoClima5Dias.append(climaDia)
            return infoClima5Dias
        except:
            return None

def mensagemErro(mensagem):

    """
    MENSAGEM DE ERRO

    Exibe uma mensagem de erro, separada por categoria, texto e destaque (exemplo).

    """

    cores = ('\033[31m', '\033[m')
    
    print(f'{cores[0]}-{cores[1]}' * (len(mensagem)))
    print(mensagem)
    print(f'{cores[0]}-{cores[1]}' * (len(mensagem)) + '\n')


# Início do Programa

try:
    coordenadas = pegarCoordenadas()
    local = pegarCodigoLocal(coordenadas['lat'], coordenadas['long'])
    climaAtual = pegarTempoAgora(local['codigoLocal'], local['nomeLocal'])    
    
    print('Clima atual em ' + climaAtual['nomeLocal'])
    print(climaAtual['textoClima'])
    print('Temperatura:' , str(climaAtual['temperatura']) + '\xb0C')

except:
    mensagemErro('Erro ao processar a solicitação. Entre em contato com o suporte.')