# work with dictionary
my_dict = {"Дима":1969,"Женя":1966} # создание dictionary
print(my_dict)
print(my_dict["Дима"]) # печать значения элемента для ключа Дима
my_dict["Саша"] = 1963 # добавления пары элемента в dictionary
print(my_dict)
my_dict.update({"Вася":1972,"Андрей":1968}) # добавление сразу двух пар элементов в dictionary
print(my_dict)
del my_dict["Женя"] # удаление значения по ключу
print(my_dict)
my_dict["Дима"] = 1970 # замена значения в ключе Дима
print(my_dict)
n = my_dict.pop("Дима") # метод pop удаление из словаря пары по ключу Дима и присвоение переменной значение этого ключа
print(n)

# work with set
my_set = {1,1,2,3,3,2,"test","trial","test",False, False} # создание множества
print(my_set)
my_set.add(5) # добавление элемента (5) во множество
my_set.add('all') # добавление элемента ("all') во множество
my_set.add((8,9)) # добавление кортежа во множестов
print(my_set)
my_set.remove(1) # удаление при помощи метода remove
print(my_set)
my_set.discard(3) # удаление при помощи метода discard
print(my_set)
my_set = list(my_set) # преобразование множества в список
print(my_set)
my_set.remove((8,9)) # удаление кортежа из списка при помощи метода remove, метод discard со списком не работает
print(my_set)
