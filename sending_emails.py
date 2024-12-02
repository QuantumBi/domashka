def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    port = [".com", ".ru", ".net"]
    sob = "@"
    flag = True
    if sob not in recipient and sob not in sender:
        flag = False
    else:
        for i in port:
            if i in recipient:
                flag = True
            if i in sender:
                flag = True
                break
            else:
                flag = False
                continue

    if flag:
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        elif sender != "university.help@gmail.com":
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')