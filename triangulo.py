x = int(input('lado 1'))
y = int(input('lado 2'))
z = int(input('lado 3'))
if x < y + z and y < x + z and z < x + y:
    print('é possivel formar um triangulo!')
else:
    print('não é possivel formar um triangulo com essas medidas')
