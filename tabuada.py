valor = float(input('Qual tabuade de interesse: '))
for multiplicador in range(1,11):
    conta = valor * multiplicador
    print('{:.0f} X {} = {:.2f}'.format(valor,multiplicador,conta))