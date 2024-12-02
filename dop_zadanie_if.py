#1 program
def which_triangle(spis):
    a, b, c = [int(i) for i in spis.split()]
    if a == b == c:
        print("Равносторонний")
    elif a == b or a == c or c == b:
        print("Равнобедренный")
    elif a != b != c:
        print("Разносторонний")


#2 program
def seredina(spis):
    a, b, c = [int(i) for i in spis.split()]
    if a > b and a < c:
        print(f"Серединное число: {a}")
    elif b > a and b < c:
        print(f"Серединное число: {b}")
    elif c > a and b > c:
        print(f"Серединное число: {c}")
    else:
        print("Значит срединного числа нет")


def cveta(spis):
    a, b = spis.split()
    a.lower()
    b.lower()
    if a == "красный" and b == "синий" or a == "синий" and b == "красный":
        print(f"-если смешать {a} и {b}, то получится фиолетовый")
    elif a == "красный" and b == "желтый" or a == "желтый" and b == "красный":
        print(f"-если смешать {a} и {b}, то получится оранжевый")
    elif a == "синий" and b == "желтый" or a == "желтый" and b == "синий":
        print(f"-если смешать {a} и {b}, то получится зеленый")


which_triangle(input("Программа 'Какой треугольник?'\nВведите длинны сторон треугольника через пробел\n:"))
print()
seredina(input("Программа 'Найти серединное число'\nВведите 3 числа через пробел\n:"))
print()
cveta(input("Введите 2 цвета из списка (красный, синий, жёлтый)\n:"))