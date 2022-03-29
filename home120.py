# В текстовый файл построчно записаны фамилия, имя учащихся класса и его оценка за тест.
# Вывести на экран сумма всех оценок.

with open("../text128.txt", "r") as file:
    summ = 0
    for line in file:
        line = line.rstrip()
        mark = int(line[-1])
        summ += mark
print(f"сумма всех оценок = {summ}")