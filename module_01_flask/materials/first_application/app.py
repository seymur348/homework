import datetime
from itertools import count
import random
import os
import re

from flask import Flask

app = Flask(__name__)

count=[0]
cars=["Chevrolet", "Renault", "Ford", "Lada"]
cat_breeds=[
"корниш-рекс",
    "русская голубая",
    "шотландская вислоухая",
    "мейн-кун",
    "манчкин",
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

# Читаем книгу и создаём список слов при запуске приложения
with open(BOOK_FILE, 'r', encoding='utf-8') as book:
    # Извлекаем слова с помощью регулярного выражения
    words = re.findall(r'\b\w+\b', book.read().lower())


@app.route('/test')
def test_function():
    now = datetime.datetime.now().utcnow()
    return f'Это тестовая страничка, ответ сгенерирован в {now}'

@app.route('/hello')
def hello_function():
    return f'Привет, мир!'
@app.route('/counter')
def count_function():
    count[0] += 1
    return f'Текущая страница открывалась {count[0]} раз'

@app.route('/cars')
def get_cars():
    return ", " .join(cars)

@app.route('/cats')
def get_random_cat():
    random_breed = random.choice(cat_breeds)
    return f"Случайная порода кошек: {random_breed}"

@app.route('/time')
def get_time_now():
    current_time=datetime.datetime.now()
    return f'Точное время: {current_time}'

@app.route('/time_future')
def get_time_future():

    current_time = datetime.datetime.now()

    current_time_after_hour = current_time + datetime.timedelta(hours=1)

    return f'Точное время через час будет: {current_time_after_hour.strftime("%Y-%m-%d %H:%M:%S")}'

@app.route('/get_random_word')
def get_random_word():
    # Выбираем случайное слово из списка
    random_word = random.choice(words)
    return f'Случайное слово из книги: {random_word}'


if __name__ == '__main__':
    app.run(debug=True)
