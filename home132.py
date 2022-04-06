# Hometask_13_3
# Напишите функцию которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# In: 852 85 784 58
# Out: [426, 392, 29]


nums = [int(i) for i in input("введите числа ").split()]
def number(lst):
    lst0 = []
    for i in lst:
        if i % 2 == 0:
            i = i / 2
            i = int(i)
            lst0.append(i)
    return lst0
print(number(nums))