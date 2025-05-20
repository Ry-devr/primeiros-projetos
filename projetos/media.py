#calcular a media de um aluno

n1 = float(input('primeiro bimestre: '))
while n1 > 10:
    print(f'{n1} nao pode')
    n1 = float(input('primeiro bimestre: '))
        
n2 = float(input('sengundo bimestre: '))
while n2 > 10:
    print(f'{n2} nao pode')
    n2 = float(input('segundo bimestre: '))

n3 = float(input('terceiro bimestre: '))
while n3 > 10:
    print(f'{n3} nao pode')
    n3 = float(input('terceiro bimestre: '))

n4 = float(input('quarto bimestre: '))
while n4 > 10:
    print(f'{n4} nao pode')
    n4 = float(input('quarto bimestre: '))

media = (n1 + n2 + n3 + n4) / 4

print(f'{media:.1f}')

       
       
