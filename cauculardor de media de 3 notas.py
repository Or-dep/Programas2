n1 = float(input('1°nota:'))
n2 = float(input('2°nota:'))
n3 = float(input('3°nota:'))
media = (n1 + n2 + n3) / 3
if media >= 6:
    print('Média do aluno:{:.2f}\nAprovado'.format(media))
else:
    print('Média do aluno:{:.2f}\nReprovado'.format(media))