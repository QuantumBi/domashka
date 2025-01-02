from time import sleep


class Video:
    """
    Doc: Класс Видео
    """
    def __init__(self, title, duration, adult_mode = False, time_now = 0):
        self.title = title.lower()
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now
    def __repr__(self):
        return self.title




class User:
    """
    Doc: Класс user
    Атрибуты: name - имя юзера, password - пароль юзера, age - возраст юзера
    """

    def __init__(self, nickname, password, age):
        self.data = {}
        self.nickname = nickname
        self.password = hash(str(password))
        self.age = age
        if nickname not in self.data:
            self.data[self.nickname] = [self.password, self.age]
        else:
            print(f"Пользователь {self.nickname} уже существует")

    def __str__(self):
        return self.nickname

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)
            else:
                print("Такое видео уже существует")
    def get_videos(self, video_name):
        post_data = []
        for i in self.videos:
            if video_name.lower() in i.title:
                post_data.append(i)
        return post_data

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.current_user = User(nickname, password, age)
            self.users.append(self.current_user.nickname)
        else:
            print(f"Пользователь {nickname} уже существует")

    def watch_video(self, video_name):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            for i in self.videos:
                if video_name.lower() == i.title:
                    for i in range(1, i.duration + 1):
                        print(i, end=" ")
                        sleep(1)
                    print("Конец видео")

    def __str__(self):
        return self.current_user





ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)



# Добавление видео

ur.add(v1, v2)



# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')



# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)



# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')




