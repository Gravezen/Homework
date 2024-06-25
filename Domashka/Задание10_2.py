list = []
new = dict()
for i in range(-5,11):
    list.append(i)
    for o in list:
        k = o
        new[k] = k ** k
print(new)
