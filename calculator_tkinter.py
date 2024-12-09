import tkinter as tk 

window = tk.Tk() #инициализируем окно
window.title("Калькудятор") # Задаём название окна
window.geometry("350x250") # задаём рпазмер окну
window.resizable(False, False) #звапрещаем изменять размер окна по высоте и ширине

#создаем виджеты
#объявляем кнопки
button_add = tk.Button(window, text="+", width=6, height=3)
button_sub = tk.Button(window, text="-", width=6, height=3)
button_mult = tk.Button(window, text="x", width=6, height=3)
button_div = tk.Button(window, text="/", width=6, height=3)
button_equally = tk.Button(window, text="=", width=15, height=3)

#размещаем кнопки в нашем окне
button_add.place(x=4, y=190)
button_sub.place(x=60, y=190)
button_mult.place(x=116, y=190)
button_div.place(x=172, y=190)
button_equally.place(x=228, y=190)

#объявляем текстовое поле
number1_entry = tk.Entry(width=51)
number2_entry = tk.Entry(width=51)
answer_entry = tk.Entry(width=51)

number1 = tk.Label(window, text="Ведите первое число")
number1.place(x=20, y=18)
number1 = tk.Label(window, text="Ведите второе число")
number1.place(x=20, y=58)
number_answer = tk.Label(window, text="Ответ")
number_answer.place(x=20, y=128)




number1_entry.place(x=20, y=40)
number2_entry.place(x=20, y=80)
answer_entry.place(x=20, y=150)






window.mainloop() # обновление информации в нашем окне