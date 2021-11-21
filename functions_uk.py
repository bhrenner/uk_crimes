import datetime

def process_time():
    data = datetime.datetime.now()
    data = data.strftime('%d/%m/%Y %H:%M')
    return data

def acha_regiao(dicio):
    elimina_regiao = []
    for reg in dicio:
        if len(dicio[reg]) < 2:
            elimina_regiao.append(reg)
    return elimina_regiao