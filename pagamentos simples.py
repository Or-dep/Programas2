x = int(input('Total da Divida: '))
y = int(input('Valor de Pago: '))
p = 0
while x > 0:
    if x <= y:
        z = 0
        p += 1
    else:
        z = x - y
        p += 1
    print('Pagamento: {}\nAntes = {}\nDepois = {}\n-----'.format(p, x, z))
    x -= y