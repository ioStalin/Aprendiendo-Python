def strange(n):
    if(n%2==0):
        return True
#print(strange(2))
#print(strange(1))

x = int(input("Igresa un numero par o impar: "))   #int: permite transformar a entero el dato de entrada input
print(strange(x))                                  #paso de argumento en función
                                                   #recordar que es un resultado de return

