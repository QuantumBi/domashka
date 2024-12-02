#1 program


def zvezda(n):
    for i in range(n):
        print(i*"*")

#2 program

def tablica(spisok):
        a, b, c, d = [int(i) for i in spisok.split()]
        for i in range(c, d+1):
            print("\t", i, end="")
        print()
        for j in range(a, b+1):
            print(f"{j} \t{j*c} \t{j*d}")
#3 program
def triangle(n):
    x = 1
    call = 1
    for i in range(n):
        for j in range(call):
            print(x, end=" ")
            x += 1
        print()
        call += 1


zvezda(int(input("Программа звезда, введите число: ")))
print()
tablica(input("Программа таблица, введите 4 числа по возрастанию A < B и C < D через пробел пример(7 10 5 6)\n:"))
print()
triangle(int(input("Программа треугольник, введите число: ")))