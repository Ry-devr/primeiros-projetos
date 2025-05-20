# pergutar

altura = float(input('qual sua altura? (m): '))
while altura >= 2.70:
    print('acima da altura macaco')
    altura = float(input('qual sua altura? (m obs: coloque o ponto(.)): '))

peso = float(input('qual sua peso? '))
while peso >= 200:
    print('sai da frente do pc e coloque seu peso certo em (kg)')
    peso = float(input('qual seu peso? (kg)'))

imc = peso / (altura * altura)

# falar oq vc tem

if imc >= 40:
    print(f'seu imc é ({imc:.2f}). ja esta com obesidade de grau 3. daqui a pouco é grau especial em!!')

elif imc >= 35:
    print(f'seu imc é ({imc:.2f}). vc esta com obseidade de grau 2')

elif imc >= 30:
    print(f'seu imc é ({imc:.2f}). vc esta com obsesidade de grau 1')

elif imc >= 25:
    print(f'seu imc é ({imc:.2f}).vc esta sobrepeso')

elif imc >= 18.5:
    print(f'seu imc é ({imc:.2f}). vc esta com o peso normal')

else:
    print(f'seu imc é ({imc:.2f}). vc esta abaixo do peso, coma direito minino')