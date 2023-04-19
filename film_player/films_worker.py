# У модулі films_worker створіть класс Film. Для цього класу оберіть
# атрибути та методи на свій розсуд. Приклад компонентів фільму зі значеннями:
class Film:
    def __init__(self, title, description, director, writer, running_time, country):
        self.title = title
        self.description = description
        self.director = director
        self.writer = writer
        self.running_time = running_time
        self.country = country

    def play(self):
        print(f'Now playing: {self.title}')

    def pause(self):
        print(f'Paused: {self.running_time}')

    def get_info(self):
        return f'Title: {self.title}\n' \
               f'Description: {self.description}\n' \
               f'Director: {self.director}\n' \
               f'Writer: {self.writer} min\n' \
               f'Running_time: {self.running_time}\n'


#Для класу Film обов'язково додайте атрибути storage_address та два методи upload_file та get_film_address.
    def upload_file(self):
        open(f"film_storage/{self.title[0]}/{self.title}.txt", "w")

    def get_film_address(self):
        print(f"film_storage/{self.title[0]}/{self.title}.txt")
