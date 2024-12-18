def tist_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


#При вызове inner_function выйдет ошибка так как из глобального пространства её вызвать нельзя
#И нельзя использовать название для функции test_function так как это зарезервированное имя для пакета pytest
#И при активации выводит ошибку pytest
tist_function()