x = int(input()) # intervalo de final
y = 1
while y <= x: 
    for z in range(1, 11):
        r = y * z
        print(f'{y} x {z} = {r}')
    y += 1
    print('----------')
