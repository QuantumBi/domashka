from operator import index

const_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Прописные буквы
const_lower = 'abcdefghijklmnopqrstuvwxyz' # Строчные буквы


step = 1
new_words = []
words = input("Введите вашу для шифрования \n:")
for i in words:
    if i in const_upper:
        num = const_upper.index(i)
        new_words.append(const_upper[num-step])
    elif i in const_lower:
        num = const_lower.index(i)
        new_words.append(const_lower[num - step])
    else:
        new_words.append(i)

print("Зашифрованная фраза")
for i in new_words:
    print(i, end="")
print()

post_word = []
for i in new_words:
    if i in const_upper:
        num = const_upper.index(i)
        post_word.append(const_upper[num+step-26])
    elif i in const_lower:
        num = const_lower.index(i)
        post_word.append(const_lower[num+step-26])
    else:
        post_word.append(i)
for i in post_word:
    print(i, end="")
