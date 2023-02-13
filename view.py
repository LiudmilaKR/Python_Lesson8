def select_class():
    return input('Введите класс или exit для выхода => ')


def exit_process():
    print('Выход здесь!')
    exit()


def show_journal(jour: list):
    for item in jour:
        print(item)


def select_subject():
    return input('Выберите предмет => ')


def who_answer():
    return input('Кто будет отвечать => ')


def what_mark():
    return input('На какую оценку ответил => ')
