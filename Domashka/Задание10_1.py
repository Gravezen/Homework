print ("Введите имя питомца, его вид, возраст и имя владельца")
name = input()
key1 = 'Вид питомца'
key2 = 'Возраст питомца'
key3 = 'Имя владельца'
vid = input()
age = int(input())
if age == 1 or age == 21 or age == 31 or age == 41 or age == 51 or age == 61 or age == 71 or age == 81 or age == 91:
    age1 = str(age) + (str(' год'))
elif age == 2 or age == 3 or age == 4 or age == 22 or age == 23 or age == 24 or age == 31 or age == 32 or age == 33 or age == 34 or age == 41 or age == 42 or age == 43 or age == 44:
    age1 = str(age) + (str(' года'))
else:
    age1 = str(age) + (str(' лет'))
vlad = input()
pet = {name : {key1: vid, 
key2: age1, key3: vlad}}
name = dict()
name = {key1 : vid, key2: age1, key3: vlad}

print(f'Это {name[key1]} по кличке "{[key for key in pet.keys()][0]}". {[n for n in name.keys()][1]}: {name[key2]}. {[o for o in name.keys()][2]}: {name[key3]}.')
   