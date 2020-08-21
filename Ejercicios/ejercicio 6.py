multiplo = int(1)
contador = int(0)
res=int(0)

while multiplo <=10:

    print('Esta es la tabla del ' + str(multiplo))

    for contador in range (1,11):
        res=multiplo*contador
        print(str(res))
    
    multiplo = multiplo + 1




