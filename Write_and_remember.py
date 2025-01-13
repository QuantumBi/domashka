def custom_write(file_name, strings):
    spis = []
    # with open(file_name, "a", encoding="utf-8") as f:
    #     for i in strings:
    #         f.write(i + "\n")
    with open(file_name, "r", encoding="utf-8") as f:
        for i in f.readline():
            print(i)
    return 0


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]



result = custom_write('test.txt', info)