def IsTriangle(a,b,c):
    return a+b>c and b+c>a and c+a<=b

def RightTriang(a,b,c):
    if not IsTriangle(a,b,c):
        return False
    if c>a and c>b:
        return c**2==a**2+b**2
    if a>b and a>c:
        return a**2==c**2+b**2
    return a**2==c**2+b**2
    

a=float(input("First side's lenght?: "))
b=float(input("Second side's lenght?: "))
c=float(input("Third side's lenght?: "))

#if IsTriangle(a,b,c):
#    print("Congrats- it could be a triangle")
#else:
#    print("Sorry, it won't be a triangle")
print(RightTriang(a,b,c))
