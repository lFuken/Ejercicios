x = 1
a = 0
r = 0
print ('la nota minima es 1.0 y la nota maxima es 5.0. El estudiante necesita una nota de 3 o superior para aprobar')
for x in range(1,16):
    y = float(input(f'Ingresar nota del estudiante {x}'))

    if y >= 3:
        a=a+1
    else:
        r=r+1

print('El numero de estudiantes aprobados es de: '+ str(a))
print('El numero de estudiantes reprobados es de: '+ str(r))