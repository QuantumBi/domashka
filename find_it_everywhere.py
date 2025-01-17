from itertools import count


def replacesing(text):
    repl_map = {",": " ", ".": " ", "=": " ",
                "!": " ", "?": " ", ";": " ",
                ":": " ", "-": " "}
    for key, value in repl_map.items():
        text = text.replace(key, value)
    return text


class WordsFinder:
    count = 1
    file_names = []
    def __init__(self, *args):
        for i in args:
            self.file_names.append(i)
    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, "r", encoding="utf-8") as file:
                words = replacesing(file.read().lower()).split()
                all_words[i] = words
        return all_words

    def find(self, word):
        GAW = self.get_all_words()
        finder = {}
        for key, value in GAW.items():
            for i in value:
                if i == word.lower():
                    finder[key] = value.index(i)+1
        return finder

    def count(self, word):
        GAW = self.get_all_words()
        counter = {}
        word_count = 0
        for key, value in GAW.items():
            for i in value:
                if i == word.lower():
                    word_count += 1
            counter[key] = word_count
            word_count = 0
        return counter


finder2 = WordsFinder('file1.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего
    