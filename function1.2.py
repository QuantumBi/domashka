a = [True, True, False]
print(any(a))
b = "" #False
c = "0" #True
#Если хотя бы один из элементов в объекте будет тру программа вернет тру

man = [True, True, False]
print(all(man))

#Если хотя бы один из элементов в объекте будет false программа вернет false

spis = [1, 1, 1]
#print(dir(spis)) #выводит всю информацию об атрибутах объектов

print(isinstance(spis, list)) # возвращает булево значение сравнение объекта с типом

spis1 = [True, True, False]
print(id(spis1)) #вывод id элемента в памяти компьютера

#print(help(spis1)) # выводит документацию для работы с объектом

def new_func():
    """Это docstring строка для документации функции"""
    pass

print(new_func.__doc__)