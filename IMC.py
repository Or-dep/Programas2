altura = float(input('Qual a sua Altura:'))
peso = float(input('Qual o seu Peso:'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('\nVocê esta abaixo do seu peso')
elif 18.5 <= imc < 25:
    print('\nvocê está no seu peso ideal')
elif 25 < imc < 30:
    print('\nvocê esta com de sobrepeso')
elif 30 < imc < 40:
    print('\nObesidade\nVocê esta acimado peso!')
elif imc > 40:
    print('\nObesidade Mórbida\nVocê esta muito acima do peso!')