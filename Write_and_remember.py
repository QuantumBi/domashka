

def custom_write(file_name, strings):
    lens = len(strings)
    spis = {}
    # with open(file_name, "a", encoding="utf-8") as f:
    #     for i in strings:
    #         f.write(i + "\n")
    with open(file_name, "r", encoding="utf-8") as f:
        for i in range(lens):
            x = f.tell()
            text = f.readline().rstrip("\n")
            spis[(i+1, x)] = text


    return spis


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]



result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)