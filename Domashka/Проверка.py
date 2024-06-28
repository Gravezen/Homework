n = int(input())
def age(n):
    if n == 1 or n % 10 == 1 and n != 11:
        return(str(' год'))
    elif n == 1 or n == 2 or n == 3 or n == 4 or n % 10 == 1 and n != 11 or n % 10 == 2 and n != 12 or n % 10 == 3 and n != 13 or n % 10 == 4 and n != 14:
        return (str(' года'))
    else:
        return (str(' лет'))

f = str(n) + age(n)
print(f)