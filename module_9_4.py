# Домашнее задание по теме
# "Создание функций на лету"

# Задача "Функциональное разнообразие":

from os import write
from random import choice

"""Lambda-функция:"""

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)

"""Замыкание:"""

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding='utf-8') as file:
            for data in data_set:
                file.write(f'{data} \n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

"""Метод __call__:"""

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

from random import choice
# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


