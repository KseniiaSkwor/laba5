import random

a=("Иванов", "Петров", "Сидоров", "Абдулов", "Баринов", "Васильев", "Мартынов", "Штиглец", "Чайковский", "Гок")
b=("Иванов", "Мостовой", "Киржаков", "Бубновский", "Красоткин", "Дубровский", "Тургенев", "Есенин", "Лермонтов", "Круг")

random_team = tuple(random.sample(a, 5) + random.sample(b, 5))

print("Исходный список 1 группы: ", a)
print("Исходный список 2 группы: ", b)
print ("Новая команда: ", random_team)

print("Длина команды: ", len(random_team))

print("Сортировка по алфавиту: ", sorted(random_team))

i=0
if "Иванов" in random_team:
    i = i+1
    print("Иванов встречается", i , "раз")
else:
    print("Иванова в списке нет")
