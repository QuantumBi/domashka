def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in other_words:
        if i.lower() in root_word:
            same_words.append(i)
        elif root_word in i.lower():
            same_words.append(i)
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))