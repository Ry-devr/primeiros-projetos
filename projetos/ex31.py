'''valor inteiro'''
while True:
    km = input('quantos km rodados: \n=> ') 
    try:
        Km_int = int(km) #armazena na variável (Km_int) o valor inteiro de (km)
        break 
    except ValueError: #continua o laço de repetição se o valor for erro (bem eu acho nê)
        pass 

'''conferir se a pessoa colocou o valor "certo"'''   
ceteza = input(f'Você quer rodar {Km_int}km, tem certeza? [s],[n]\n=> ').lower().strip()

while ceteza not in ['s', 'sim', 'n', 'nao','não']:
    print('valor errado, por favor tenta novamente:')
    ceteza = input(f'[s],[n]\n=> ').lower().strip()

'''função em si'''
if ceteza == 'sim' or ceteza == 's':
    if Km_int <= 200:
        reais = Km_int * 0.5

    else:
        reais = Km_int * 0.45

    print(f'você vai pagar um total de {reais:.2f} Reais')

else:
    print('desculpa, abra o programa de novo')

