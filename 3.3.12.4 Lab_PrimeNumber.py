def IsPrime(num):
    a=0
    num=int(input("Ingresa un número: \n"))
    for i in range (1,num+1):
        if(num%i ==0):
            a=a+1
    if(a!=2):
        print("No es primo")
    else:
        print("Si es primo")
#
# put your code here
#

for i in range(1,20):
	if IsPrime(i + 1):
			print(i+1,end=" ")
print()
