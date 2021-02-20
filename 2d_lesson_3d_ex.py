"""
Дан список, содержащий искаженные данные с должностями и именами сотрудников:

['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' 
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду? Можно ли при этом не создавать новый список?
"""
state_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for user_name_list in state_list:
    user_name = user_name_list.split(' ')
    user_name = user_name[::-1]
    user_name = user_name[0]
    print("Привет,", user_name.capitalize())