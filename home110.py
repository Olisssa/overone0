# Решить задачу с обработкой исключений.
# Вызвать ошибку KeyError и вернуть программу к исполнению команд.
# Укажите пользователю какое вино он может выбрать.
# Катя с Анной пьют вино. Программа принимает сколько бутылок вина выпьет каждая.
# Еще программа принимает какое вино пьет Катя, а Анна всегда пьет белое.
# In: 2
# 5
# pink wine
# Out: Есть только ['red wine', 'white wine'], выберите из них

katya = int(input("введите сколько пьет Катя "))
anna = int(input("введите сколько пьет Анна "))
wine_katya = input("введите какое вино пьет Катя ")
wine_lst = ['red wine', 'white wine']

try:
    if wine_katya in wine_lst:
        d = {wine_katya: katya, 'white wine': anna}
    else:
        d = {}
    print(d["white wine"])

except KeyError:
    print(f"Есть только {wine_lst}, выберите из них")
