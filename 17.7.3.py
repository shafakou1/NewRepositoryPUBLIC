money = int(input("money= "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

values_list = list(per_cent.values())
values_list[0] = money*values_list[0]/100
values_list[1] = money*values_list[1]/100
values_list[2] = money*values_list[2]/100
values_list[3] = money*values_list[3]/100
values_list_deposit = list(map(int,values_list))

print("deposit = ", values_list_deposit)
print("Максимальная сумма, которую вы можете заработать - ", max(values_list_deposit))

