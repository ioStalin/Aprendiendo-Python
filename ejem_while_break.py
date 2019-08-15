max = -999999999
counter = 0

while True:
    number = int(input("Enter a value: "))
    if number == -1:
        break
    counter +=1
    if number > max:
        max = number
if counter:
    print ("Largest num is: " ,max)
else:
    print("Are you kidding?")
