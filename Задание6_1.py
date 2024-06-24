N = int(input())
i = 0
count = 0
while i < N:
    n = int(input())
    i += 1
    if n == 0:
        count += 1
print(count)