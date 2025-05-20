import random

numero = random.randint(1, 10)
qtd = 0

while True:
    qtd = qtd + 1

    esc = int(input('escolha um numero de 1 a 10: '))
    while esc not in range(1, 11) :
        
        print('é só de 1 a 10')
        esc = int(input('escolha um numero de 1 a 10: '))
    
    quente = numero - esc

    if esc == numero:
        print(f'parabéns o numero {numero} é o certo')
        break
    
    elif quente in [1, -1]:
        print('muito quente')   
    
    elif quente in [t, -2]:
        print('quente')    
    
    else:
        print('frio')

print(f'você teve {qtd} de tentativas')
