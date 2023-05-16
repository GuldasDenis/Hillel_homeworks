import os
import string
# У модулі media_player створіть клас Player. Для цього класу оберіть атрибути та методи на свій розсуд.
# Перегляньте з чеого складаються медіа плеери netflix, megogo, youtube.
# До прикладу методи: play, pause, save_last_time, change_quality

class Player:
    def __init__(self, media_name):
        self.media_name = media_name
        self.current_time = 0
        self.playing = False
        self.quality = "low"
        self.last_time = 0

    def play(self):
        if not self.playing:
            print(f"Playing {self.media_name}")
            self.playing = True

    def pause(self):
        if self.playing:
            self.playing = False
            print(f"Paused {self.media_name}")

    def save_last_time(self, time):
        if self.playing:
            self.last_time = time
            print(f"Last time saved: {self.last_time} minutes")

    def change_quality(self, quality):
        self.quality = quality
        print(f"Quality changed to {self.quality}")

# В середині пакету film_player створіть дерикторію film_storage. А в середині film_storage дерикторії від A до Z


film_storage_path = os.path.join("film_storage")

if not os.path.exists(film_storage_path):
    os.mkdir(film_storage_path)

for letter in string.ascii_uppercase:
    letter_path = os.path.join('film_storage', letter)

    if not os.path.exists(letter_path):
        os.mkdir(letter_path)
