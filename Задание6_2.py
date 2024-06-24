print("Введите натуральное число, не превышающее 2000000000")
X = int(input())
if X > 2e9:
    print("Превышено допустимое значение!")
else:
    count = 0
    for i in range(1, X +1):
         if X % i == 0:
            count += 1
            print(i)
    print(count)