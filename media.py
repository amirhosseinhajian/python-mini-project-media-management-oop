from actor import Actor
from pytube import YouTube

class Media:
    counter = 100
    def __init__(self, name, director, imdb_score, url, duration, casts):
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = casts
        self.code = Media.counter
        Media.counter+=1 
    
    def download(self):
        try:
            YouTube(self.url).streams.first().download(output_path='./download/', filename=self.name)
        except:
            print("please check your conection and try again.")

    def print_actors(self):
        actors_len = len(self.casts)
        for i, actor in enumerate(self.casts):
            if i != actors_len-1:
                print(actor.name, end=", ")
            else:
                print(actor.name, end='')
    
    @staticmethod
    def show_all(media_object_list):
        if(len(media_object_list)) > 0:
            media_object_list[0].print_labels()
        for media in media_object_list:
            media.show_info()

    @staticmethod
    def search_media(media_object_list, keyword):
        keyword = keyword.lower()
        for media in media_object_list:
            if str(media.code) == keyword or media.name.lower() == keyword:
                return media
        return False
    
    def edit(self):
        media_properties = self.__dict__.keys()
        while True:
            property = input("Wath property do you want to edit? please enter property name acording to above table and if you want to leave this section enter 0: ").lower()
            if property == '0':
                break
            if property in media_properties:
                if property != "casts":
                    vars(self)[property] = input("Enter new value for this property: ")
                else:
                    while True:
                        user_choice = input("if you want to add new cast enter 'a' and if you want to edit available casts enter index of this actor: ")
                        if user_choice == 'a':
                            vars(self)[property].append(Actor(input("Enter name of this actor: ")))
                            break
                        else:
                            try:
                                if int(user_choice) in range(len(vars(self)[property])):
                                    vars(self)[property][int(user_choice)].name = input("Enter new value for this property: ")
                                    break
                                else:
                                    print("invalid input.")
                            except:
                                print("invalid input.")
                print("media updated successfully")
            else:
                print("the property you entread does not exist.")
    
    @staticmethod
    def search_by_time(film_list, t1_hour, t1_minute, t2_hour, t2_minute):
        total_second_1 = t1_hour * 3600 + t1_minute * 60
        total_second_2 = t2_hour * 3600 + t2_minute * 60
        if total_second_2 < total_second_1:
            total_second_1, total_second_2 = total_second_2, total_second_1
        found_movies = []
        for film in film_list:
            try:
                hour = int(film.duration.split(" ")[0].split("h")[0])
                minute = int(film.duration.split(" ")[1].split("m")[0])
                second = hour * 3600 + minute * 60
                if second >= total_second_1 and second <= total_second_2:
                    found_movies.append(film)
            except:
                print("This message indicates that a video has been ignored due to its inappropriate duration format")
        return found_movies
