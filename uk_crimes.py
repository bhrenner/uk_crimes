import csv
import functions_uk
dicio:dict = {} 
data = functions_uk.process_time()

""" Abre um arquivo csv """
with open('crimes_uk/reccrimepfa-210901-151708.csv', 'r') as arquivo: 
    reader = csv.reader(arquivo, delimiter=",") 
    header = next(arquivo)
    """Laço de repetiçao que insere e filtra cada linha 
    caso não esteja no dicionário evitando repetiões
    e agrupando valores iguais"""
    for row in reader:
        if row[2] not in dicio:
           dicio[row[2]] = {}
        if int(row[4]) > 10:
            if row[3] not in dicio[row[2]]:
                dicio[row[2]][row[3]] = []
            dicio[row[2]][row[3]].append(int(row[4]))
        for key in dicio[row[2]]:   
            if len(dicio[row[2]][key])>=2:    
                soma = sum(dicio[row[2]][key])
                dicio[row[2]][key].clear()
                dicio[row[2]][key].append(soma)

elimina_regiao = functions_uk.acha_regiao(dicio)  #Retorna uma lista de regioes que possuem poucos crimes            
for x in elimina_regiao: #Elimina do dicionáio cada região com menos de 2 crimes
    if x in dicio:
        dicio.pop(x)
        
with open('crimes_uk/resultado.JSON', 'w+') as arq:
    """Cria um arquivo JSON"""
    for reg in dicio:
        arq.write('\n process time: ' + str(data) + ' region: ' + str(reg) + ' crimes: ' + str(dicio[reg]))

print('Concluído!!!')
                
           
                    
        
    
              
       