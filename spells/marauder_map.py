import os
import string
import json


class MapMagic:
    _map_open = "I solemnly swear that I am up to no good."
    _map_close = "Mischief managed."


class MarauderMap(MapMagic):
    __films_titles = {"results": [
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
    ]}

    def __init__(self, path):
        self.path = path

    def map_generator(self):
        print(self._map_open)

        os.mkdir("Harry Potter")
        os.chdir("Harry Potter")

        for hp_title in self.__films_titles["results"]:
            os.mkdir(hp_title["title"].replace(":", ""))


        dir_list = os.listdir(os.getcwd())

        for movie_folder in dir_list:
            os.chdir(movie_folder)
            for i in string.ascii_uppercase:
                os.mkdir(i)
            os.chdir("..")

        hp_titles_list = []

        for hp_title in self.__films_titles["results"]:
            hp_titles_list.append(hp_title["title"].replace(":", ""))



        awards_list = {}
        key_template = ('type', 'award_name', 'award')
        temp_dict = {}

        film_awards_file = open(self.path)
        json.load(film_awards_file)

        for movie_title in hp_titles_list:
            for awards_item in film_awards_file:
                if movie_title == awards_item["results"][0]["movie"]["title"].replace(":", ""):
                    print(awards_item["results"][0]["movie"]["title"].replace(":", ""))
                    temp_list = []
                    for res_item in awards_item["results"]:
                        temp_award_dict = temp_dict.fromkeys(key_template)
                        temp_award_dict["type"] = res_item["type"]
                        temp_award_dict["award_name"] = res_item["award_name"]
                        temp_award_dict["award"] = res_item["award"]
                        temp_list.append(temp_award_dict)
                        awards_list.update({movie_title: temp_list})


        dir_list = os.listdir(os.getcwd())
        for dir_title in dir_list:

            for movie_title in awards_list:
                if dir_title == movie_title:
                    os.chdir(dir_title)
                    letters_list = os.listdir(os.getcwd())
                    for letter_dir in letters_list:
                        for x in awards_list[dir_title]:
                            if x['award_name'][0] == letter_dir:
                                file_path = os.path.join(os.getcwd(), letter_dir, x['award_name'] + '.txt')
                                with open(file_path, 'ab') as award_write:
                                    award_write.write(x['award'].encode('utf-8') + b'\n')
                                    print(f"The award '{x['award']}' is added to '{x['award_name']}.txt' in directory '{letter_dir}'.")

                    os.chdir('..')

        print(self._map_close)


marauder_map = MarauderMap("C:/Users/denis.guldas/PycharmProjects/Hillel_homeworks/spells/films_awards.json")
marauder_map.map_generator()
