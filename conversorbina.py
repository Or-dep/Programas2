print('digite um valor para ser convertido')
x = int(input('Qual valor:'))
print('escolha uma conversão abaixo:\n[1]Binário\n[2]Octal\n[3]Hexadecimal')
y = int(input('Qual sua opção:'))
if y == 1:
    print('A converção binaria do valor {} é: {}'.format(x, bin(x)[2:]))
elif y == 2:
    print('A converção octal do valor {} é: {}'.format(x, oct(x)[2:]))
elif y == 3:
    print('A converção henxadecimal do valor {} é: {}'.format(x, hex(x)[2:]))