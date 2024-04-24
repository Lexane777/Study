import re
listRegAuto = input("Введите номер автомобиля: ").upper().split()
strRegAuto=''.join(listRegAuto)
result = re.compile(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}RUS')
if re.match(result,strRegAuto):
    print("Номер введен верно")
else:
    print("Номер введен неверно")