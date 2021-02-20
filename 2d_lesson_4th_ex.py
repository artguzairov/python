"""
 Создать список, содержащий цены на товары (10 – 20 товаров), например:

[57.8, 46.51, 97, ...]
- Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). 
    Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
- Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
- Создать новый список, содержащий те же цены, но отсортированные по убыванию.
- Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""
price_list = [57.08, 46.51, 97, 77, 56.70, 30, 45.50, 10, 70.33, 24]
idx = 0
for price_list[idx] in price_list:
    if isinstance(price_list[idx], float) == True:
        rub = int(price_list[idx])
        kop = (price_list[idx] - int(price_list[idx])) * 100
        kop = int(round(kop, 2))
        if kop < 10:
            kop = '0' + str(kop)
        rub_kop = '"' + str(rub) + ' руб ' + str(kop) + ' коп"'
        unit_1_of_price_list = price_list.pop(idx)
        price_list.insert(idx, rub_kop)
    else:
        rub_kop = ('"' + str(price_list[idx]) + ' руб 00 коп"')
        unit_1_of_price_list = price_list.pop(idx)
        price_list.insert(idx, rub_kop)
    idx += 1
for item in price_list:
    print(item, end=',')
print()
price_list.sort()
for item in price_list:
    print(item, end=',')
if price_list == price_list:
    print('\nСписок тот же')
price_list_from_big_to_small = price_list.copy()[::-1]
for item in price_list_from_big_to_small:
    print(item, end=',')
print()
five_biggest_price = price_list_from_big_to_small[:4]  
for item in five_biggest_price:
    print(item, end=',')