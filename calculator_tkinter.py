import tkinter as tk
from time import sleep

def get_values():
    try:
        num1 = int(number1_entry.get())
        num2 = int(number2_entry.get())
    except (ValueError, TypeError):
        answer_entry.insert(0, "Ошибка")
        answer_entry.delete(0, "end")
    else:
        return int(num1), int(num2)

    

def insert_values(res):
    answer_entry.delete(0, "end")
    answer_entry.insert(0, res)


def add():
    numer1, numer2 = get_values()
    res = numer1 + numer2
    insert_values(res)


def sub():
    numer1, numer2 = get_values()
    res = numer1 - numer2
    insert_values(res)

def mult():
    numer1, numer2 = get_values()
    res = numer1 * numer2
    insert_values(res)

def div():
    numer1, numer2 = get_values()
    if numer1 == 0 or numer2 == 0:
        insert_values("Ошибка, на ноль делить нельзя")
    else:
        res = numer1 / numer2
        insert_values(res)



window = tk.Tk() #инициализируем окно
window.title("Калькудятор") # Задаём название окна
window.geometry("350x250") # задаём рпазмер окну
window.resizable(False, False) #звапрещаем изменять размер окна по высоте и ширине

#создаем виджеты
#объявляем кнопки
button_add = tk.Button(window, text="+", width=6, height=3, command=add)
button_sub = tk.Button(window, text="-", width=6, height=3, command=sub)
button_mult = tk.Button(window, text="x", width=6, height=3, command=mult)
button_div = tk.Button(window, text="/", width=6, height=3, command=div)


#размещаем кнопки в нашем окне
button_add.place(x=30, y=190)
button_sub.place(x=110, y=190)
button_mult.place(x=190, y=190)
button_div.place(x=270, y=190)


#объявляем текстовое поле
number1_entry = tk.Entry(width=51)
number2_entry = tk.Entry(width=51)
answer_entry = tk.Entry(width=51)

#выводим поля для ввода и указатели
number1 = tk.Label(window, text="Ведите первое число")
number1.place(x=20, y=18)

number2 = tk.Label(window, text="Ведите второе число")
number2.place(x=20, y=58)

number_answer = tk.Label(window, text="Ответ")
number_answer.place(x=20, y=128)




number1_entry.place(x=20, y=40)
number2_entry.place(x=20, y=80)
answer_entry.place(x=20, y=150)






window.mainloop() # обновление информации в нашем окне



