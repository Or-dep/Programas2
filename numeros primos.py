print('-'*5,'Identificador de N° Primos','-'*5)
ini = int(input('Digite um inicio: '))
fim = int(input('Digite um fim: '))
p = 0
numeros = list()
for numb in range(ini, fim + 1):
    if numb > 1:
        for primos in range(2, numb):
            if (numb % primos == 0):
                break
        else:
            numeros.append(numb)
            p += 1
print('{}\nprimos: {}'.format(numeros, p))