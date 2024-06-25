cash = int(input())
cost = int(input())
cassa = int(input())

if (cash >= cost) and ((cash - cost) <= cassa):
    print ("Кола Наша")
else:
    print("Колу не купим")
# and показывает, что должны выполниться оба условия
# or показывает, что может выполниться одно из условий

if not cash >= cost: # not показывает если НЕ выполняется условие, то что произойдет
    print("Хер тебе")