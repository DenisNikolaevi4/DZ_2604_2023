# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью
# рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input("Введите число А: ")) 
b = int(input("Введите степень B: ")) 
def stepen(a, b):
    if b == 1:
        return a
    return a * stepen(a, b-1)

print(f"Число A({a}) в степени В({b}) = {stepen(a,b)}")