list = [10, 1, 8, 3, 5]
l = len(list)
for i in range(l//2):
    list[i],list[l-i-1] = list[l-i-1],list[i]
print(list)
