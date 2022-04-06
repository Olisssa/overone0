# Hometask_13_1
# Из полученного списка чисел создайте список с суммами
# этих чисел, отсортированными по возрастанию
# In: 965 582 023 8 695210
# Out: [5, 8, 15, 20, 23]

nums = input("введите числа ").split()
def summ(lst):
   lst0 = []
   for number in lst:
       number = str(number)
       s = 0
       for i in number:
           i = int(i)
           s += i
       lst0.append(s)
   return sorted(lst0)
print(summ(nums))

