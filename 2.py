f=[29,2,17,13,29,8]
povtor = []

for i in range(len(f)):
    for j in range (i+1, len(f)):
        if f[i]==f[j] and f[i] not in povtor:
            povtor.append(f[i])
if povtor:
    print ("Повторяющийся элемент: ", povtor)
else:
    print ("Повторов нет")