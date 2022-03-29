# В текстовый файл построчно записаны фамилия, имя учащихся класса и его оценка за тест.
# Вывести на экран сколько всего оценок.


with open("../text128.txt", "r") as file:
    counter = 0
    for line in file:
        for i in line:
            if i.isdigit():
                counter += 1
print(f"всего {counter} оценок")