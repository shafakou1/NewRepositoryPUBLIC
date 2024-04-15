tickets = int(input('Введите количество билетов: '))
summa = 0
#создаю цикл for-in для определения возраста и цены каждого билета
for i in range(1, tickets + 1):
    age = int(input('Введите возраст посетителя: '))
    #задаю критерии определения стоимости билета, исходя из значения "age"
    if age < 18:
        summa += 0
    if 18 <= age <= 25:
        summa += 990
    if age > 25:
        summa += 1390
#задаю условие получения 10%-ной скидки
if tickets > 3: summa = summa - summa//100*10
print("Сумма к оплате: ", summa)
