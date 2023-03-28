# Завдання 1
# Ситворіть функцію(назву оберіть самі) без параметрів, котра повертає(return) рядок "Це моя перша функція".
# Викличте цю функцію у наступному рядку.

def my_first_function():
    return "Це моя перша функція"
print(my_first_function())

# Завдання 2
# Ситворіть функцію, котра має один параметр(число) і повертає це число у степині 2.

def my_first(number=6):
    return number ** 2
print(my_first())

# Завдання 3
# Ситворіть функцію, котра приймає список фільмів і повертає новий список з фільмами назва яких більше 8 літер.

films = ['Spider-man: No way to home',
         'Crazy Stupid Love.',
         'Die Hard',
         'Dead Poets Society',
         'Home Alone',
         'Seven',
         'Memento',
         'Harry Potter and the Prisoner of Azkaban',
         "One Flew Over the Cuckoo's Nest"
        ]


def long_movies(films):
    result = []
    for film in films:
        if len(film) > 8:
            result.append(film)
    return result

long_films = long_movies(films)
print(long_films)

# Завдання 4
# Ситворіть функцію, котра приймає список чисел та повертає тупл.
Перше значення тупла є середнім значенням всіх аргументів, а друге значення перше число яке більше середнього.\

test_list = [1, 2, 3, 4, 12, 322, 55, 66, 71, 80, 94, 6, 10, 32]

def new_tuple(first):
    avg = sum(first) / len(first)
    first_number = None
    for i in first:
        if i > avg:
            first_number = i
            break
    return (avg, first_number)

result = new_tuple(test_list)
print(result)


test_list = [1, 2, 3, 4, 12, 322, 55, 66, 71, 80, 94, 6, 10, 32]

def numbers(test_list):
    result = []
    for i in test_list:
        if i % 2 == 0:
            result.append(i)
    return result

new_numbers = numbers(test_list)
print(new_numbers)


# Завдання 6
# Створіть функцію, яка приймає список туплів і повертає назву предмету з найвищою оцінкою.


grade = [('Англійська мова', 88), ('Біологія', 90), ('Математика', 97), ('Українська мова', 82)]

def mark(grades):
    max_grade = 0
    best_subject = ""
    for i, grade in grades:
        if grade > max_grade:
            max_grade = grade
            best_subject = i
    return best_subject

get_best_subject = mark(grade)
print(get_best_subject)

# Завдання 7
# Створіть функцію, яка приймає два параметри:
# перший число(назва довільна), другий параметр(step) за замовчуванням дорывнює
# 2. Функція повертає аргумент першгого параметра возведений у степінь що передається у параметрі 2.

num = int(input("Введіть число: "))

def degree(num, step=2):
    return num ** step
result = degree(num)
print(result)

Завдання 8
Створіть функцію, яка приймає один параметр imdb_id
і повертає назву фільму, що відповідає цьому id зі списку films_title.

films_title = {
    "results": [
        {
            "imdb_id": "tt1201607",
            "title": "Harry Potter and the Deathly Hallows: Part 2"
        },
        {
            "imdb_id": "tt0241527",
            "title": "Harry Potter and the Sorcerer's Stone"
        },
        {
            "imdb_id": "tt0926084",
            "title": "Harry Potter and the Deathly Hallows: Part 1"
        },
        {
            "imdb_id": "tt0304141",
            "title": "Harry Potter and the Prisoner of Azkaban"
        },
        {
            "imdb_id": "tt0417741",
            "title": "Harry Potter and the Half-Blood Prince"
        },
        {
            "imdb_id": "tt0295297",
            "title": "Harry Potter and the Chamber of Secrets"
        },
        {
            "imdb_id": "tt0330373",
            "title": "Harry Potter and the Goblet of Fire"
        },
        {
            "imdb_id": "tt0373889",
            "title": "Harry Potter and the Order of the Phoenix"
        }
    ]
}

def name_movie(imdb_id):
    for movie in films_title['results']:
        if movie['imdb_id'] == imdb_id:
            return movie['title']

imdb_id = input("Введіть imdb_id:")
movie_title = name_movie(imdb_id)
print(movie_title)




