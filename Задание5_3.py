A = int(input())
B = int(input())
X = int(input())

if A >= X and B >= X:
    print("2")
elif A >= X and B <= X:
    print("Mike")
elif A <= X and B >= X:
    print("Ivan")
else:
    if A + B >= X:
        print("1")
    else:
        print("0")