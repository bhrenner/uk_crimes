import datetime

def process_time():
    """Retorna uma variavel da hora em que a função é chamada"""
    data = datetime.datetime.now()
    data = data.strftime('%d/%m/%Y %H:%M')
    return data

def acha_regiao(dicio):
    """Cria uma lista com as regiões que não possuem vais de 2 crimes"""
    elimina_regiao = []
    for reg in dicio:
        if len(dicio[reg])<2:
            elimina_regiao.append(reg)
    return elimina_regiao