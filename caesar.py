from operator import index

const_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Прописные буквы
const_lower = 'abcdefghijklmnopqrstuvwxyz' # Строчные буквы

print("""Для зашифровки фразы введите 0
Для расшифроки фразы введите 1
Для вывода зашифрованной фразы введите list
Для вывода расшифрованной фразы введите postlist
Для выхода введите end\n""")


new_word = []
post_word = []

def shifrator():
        global new_word
        step = int(input("Укажите шаг шифрования от 1 до 26\n"))
        words = input("Введите фразу для шифрования \n:")
        print()
        for i in words:
                if i in const_upper:
                        num = const_upper.index(i)
                        new_word.append(const_upper[num-step])
                elif i in const_lower:
                        num = const_lower.index(i)
                        new_word.append(const_lower[num - step])
                else:
                        new_word.append(i)

def deshifrator():
        global post_word
        step = int(input("Укажите шаг расшифрования от 1 до 26\n"))
        unshif_word = input("Введите фразу для расшифрования \n")
        for i in unshif_word:
                if i in const_upper:
                        num = const_upper.index(i)
                        post_word.append(const_upper[num+step-26])
                elif i in const_lower:
                        num = const_lower.index(i)
                        post_word.append(const_lower[num+step-26])
                else:
                        post_word.append(i)
def listing():
        global new_word
        for i in new_word:
                print(i, end="")
        print()
def postlisting():
        global post_word
        for i in post_word:
                print(i, end="")
        print()

while True:
        select = input("--->  ")
        print()
        if select == "0":
                shifrator()
        elif select == "1":
                deshifrator()
        elif select == "end":
                break
        elif select == "list":
                listing()
        elif select == "postlist":
                postlisting()

print()