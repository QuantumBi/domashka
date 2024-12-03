#1 program


def zvezda(n):
    for i in range(1, n+1):
        print(i*"*")

#2 program

def tablica(spisok):
        a, b, c, d = [int(i) for i in spisok.split()]
        for i in range(c, d+1):
            print(f"\t{i}", end="")
        print("\n")
        for j in range(a, b+1):
            print(f"{j}\t", end="")
            [print(f"{j*i}\t", end="") for i in range(c, d+1)]
            print("\n")

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


# zvezda(int(input("Программа звезда, введите число: ")))
# print()
tablica(input("Программа таблица, введите 4 числа по возрастанию A < B и C < D через пробел пример(7 10 5 6)\n:"))
print()
# triangle(int(input("Программа треугольник, введите число: ")))