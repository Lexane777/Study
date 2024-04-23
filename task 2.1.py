#######################################
# Данная программа меняет средние числа#
# двух трехзначных чисел               #
########################################
strNumber1=input("Введите первое число ")[:3]
strNumber2=input("Введите второе число ")[:3]
result1=(int(strNumber1)//100)*100+int(strNumber2)%100-int(strNumber2)%10+int(strNumber1)%10
result2=(int(strNumber2)//100)*100+int(strNumber1)%100-int(strNumber1)%10+int(strNumber2)%10
#Запишем полученный результат
print(f"Результат работы программы: {result1} {result2}")

