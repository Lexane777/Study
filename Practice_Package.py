import mypackage.My_Function as mypack
print("Программа выводит степень числа")
x=float(input("Введите число: "))
n=float(input("Введите степень числа: "))
print(f'{n} cтепень числа {x} составляет {mypack.my_power(x,n)}')