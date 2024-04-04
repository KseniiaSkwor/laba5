a = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")

otvet=int(input("Сколько выходных вы хотите? "))

weekends = a[-otvet: ]
workday = a[:-otvet]

print("Ваши выходные дни: ", "," .join(weekends))
print("Ваши рабочие дни: ", "," .join(workday))

