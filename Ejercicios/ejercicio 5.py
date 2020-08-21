x = int(input("Ingrese inicio de contador"))
y = int(input("Ingrese limite de contador"))

if x<y:
    while x <= y:
        print(str(x))

        x = x+1

else:
    print('ERROR: El inicio debe ser menor al limite')
