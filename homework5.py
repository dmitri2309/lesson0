immutable_var = 1,3,10,True,"good"
print(immutable_var)
immutable_var = (1,5,8,False, "bad")
print(immutable_var)
immutable_var = ([1,"yes"],2,5,"norm")
print(immutable_var)
immutable_var[0][0] = 2
print(immutable_var)
immutable_var[0][1] = "no"
print(immutable_var)
mutable_list = [4,6,8,False,"fine"]
print(mutable_list)
print(mutable_list[1:4])
print(mutable_list[-3:-1])
print(mutable_list[:-1])
mutable_list[2] = 5
print(mutable_list)
mutable_list[-1] = 'poor'
print(mutable_list)
print(mutable_list+ [1,2])
print(immutable_var * 3)
# элементы кортежа изменить нельзя, они неизменяемы, элементы кортежа могут быть разные типы, элемент кортежа может быть даже список который можно изменять
