# -*- coding: utf8 -*-
from gym_service import GymService


def print_command_list():
    print('''1 - Найти клиента 
2 - Выход''')


def start():
    name = str(input('Ваше имя? \n'))
    last_name = str(input('Ваша фамилия? \n'))
    gym_service.start_work_with_client(name, last_name)


def run():
    while True:
        task = int(input('Что вы хотите? \n'))
        if task == 1:
            start()
        if task == 2:
            break


if __name__ == "__main__":
    gym_service = GymService()
    print_command_list()
    run()


