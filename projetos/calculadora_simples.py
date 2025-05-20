
def calculadora():
    n1 = int(input('escolha um numero por favor: '))
    n2 = int(input('escolha outro numero: '))
    op = ['+','-','*','/']   
    
    while True:
        cal = input(f'escolha:({op[0]});({op[1]});({op[2]});({op[3]})').lower()
        if cal == op[0]:
           res = n1 + n2
           print(res)
           break
        elif cal == op[1]:
            res = n1 - n2
            print(res) 
            break      
        elif cal == op[2]:
            res = n1 * n2
            print(res)
            break       
        elif cal == op[3]:
            if n2 != 0:
                res = n1 / n2
                print(res)
                break  
            else:
                print('descupa nao da para dividir por 0') 
        else:
           print('nao')
        

calculo = calculadora()
