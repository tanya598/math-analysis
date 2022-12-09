import math
import matplotlib.pyplot as plt

f = open("answer.txt", "w")
data = []
for i in open("input_100.txt"):
    data.append(int(i.strip()))

print("Послідовність:", data)
f.write("Послідовність:")
f.write(str(data))
# Завдання 1
# -----------------------------------------------
print("Завдання 1:")
f.writelines("\n\nЗавдання 1:")
print("Таблиця частот та сукупних частот: ")
f.writelines("\nТаблиця частот та сукупних частот: ")

A = set(sorted(data))

for item in A:
    print("___________________________")
    print("|", item, "\t | \t", data.count(item), "\t | \t", round(((data.count(item)/(len(data)))*100)), "%", "|")
    f.writelines("\n______________________________________")
    f.write("\n|")
    f.write(str(item))
    f.write("\t | \t")
    f.write(str(data.count(item)))
    f.write("\t | \t")
    f.write(str(round(((data.count(item)/(len(data)))*100))))
    f.write("%")
    f.write("|")
# -----------------------------------------------
print('Найбільше переглядів:', max(data))
f.write('\nНайбільше переглядів:')
f.write(str(max(data)))
# -----------------------------------------------
# Завдання 2
# -----------------------------------------------
print("Завдання 2:")
f.writelines("\n\nЗавдання 2:")

def mediana(arr):
    if len(arr) % 2 == 0:
        median = (arr[int(len(arr) / 2)] + arr[int(len(arr) / 2) - 1]) / 2
    else:
        median = arr[int(len(arr) / 2) + 1]
    return median

f.write("\nМедіана = ")
f.write(str(mediana(sorted(data))))
print("Медіана = ", mediana(sorted(data)))
# -----------------------------------------------
Moda = 0
ModaN = 0
for i in data:
    if ModaN < data.count(i):
        Moda = data[i]
        ModaN = data.count(i)
if (ModaN == 1):
    f.write("\nМоди не існує")
    print("\nМоди не існує")
else:
    f.write("\nМода: ")
    f.write(str(Moda))
    f.write("та кількість повторень: ")
    f.write(str(ModaN))
    print("Мода: ", Moda, " та кількість повторень: ", ModaN)
# -----------------------------------------------
# Завдання 3
# -----------------------------------------------
print("Завдання 3:")
f.writelines("\n\nЗавдання 3:")
disp = 0
for i in data:
    disp += ((i - (sum(data) / len(data))) ** 2) / (len(data) - 1)
print("Дисперсія = ", disp)
f.write("\nДисперсія = ")
f.write(str(disp))
# -----------------------------------------------
print("Середнє квадратичне відхилення розподілу:", math.sqrt(disp))
f.write("\nСереднє квадратичне відхилення розподілу:")
f.write(str(math.sqrt(disp)))
# -----------------------------------------------
# Завдання 4
# -----------------------------------------------
print("Завдання 4:")
f.writelines("\n\nЗавдання 4:")
plt.bar(range(len(data)), data)
plt.xlabel("Фільм")
plt.ylabel("«Частота»")
plt.show()
f.close()
