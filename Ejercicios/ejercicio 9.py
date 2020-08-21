x = int(input('Porfavor ingrese el numero secreto'))
y = 0

while y < 1:
    if x == 111:
        y=y+1
    else:
        x = int(input('Vuelva a intentarlo'))

print(f'Felicidades. El numero secreto era {111}')