from media import Media
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from database import DB
from actor import Actor

db = DB()
movies, series, documantaries, clips = db.get_all_medias()

def exit_program():
    db.write_to_database(movies, series, documantaries, clips)
    print("goodbye.")
    exit(0)

def show_movies():
    print("\n------------------------------------------------------------ Film ------------------------------------------------------------\n")
    Media.show_all(movies)

def show_series():
    print("\n------------------------------------------------------------ Series ------------------------------------------------------------\n")
    Media.show_all(series)

def show_documantaries():
    print("\n------------------------------------------------------------ Documantaries ------------------------------------------------------------\n")
    Media.show_all(documantaries)

def show_clips():
    print("\n------------------------------------------------------------ Clips ------------------------------------------------------------\n")
    Media.show_all(clips)

def show_all_media():
    show_movies()
    show_series()
    show_documantaries()
    show_clips()

def select_media_to_show():
    print("great. what media do you want to show?", menu["select_media_menu"])
    user_choice = input("e- all media\n")
    while user_choice not in menu["secondary_valid_inputs"] and user_choice != "e":
        user_choice = input("invalid input. please enter again: ")
    menu["operations"]["1"+user_choice]()

def make_casts_objects(str_casts):
    casts = []
    for cast in str_casts.split("-"):
        casts.append(Actor(cast))
    return casts

def select_media_to_add():
    user_choice = print("great. what media do you want to add?", end=" ")
    user_choice = input( menu["select_media_menu"] + "\n")
    while user_choice not in menu["secondary_valid_inputs"]:
        user_choice = input("invalid input. please enter again: ")
    name = input("Enter name: ")
    director = input("Enter director: ")
    imdb_score = input("Enter imdb score: ")
    url = input("Enter URL: ")
    duration = input("Enter duration: ")
    casts = input("Enter casts with a - between each cast: ")
    menu["operations"]["2"+user_choice](name, director, imdb_score, url, duration, make_casts_objects(casts))

def add_new_film(name, director, imdb_score, url, duration, casts):
    janr = input("Enter janr: ")
    new_film = Film(name, director, imdb_score, url, duration, casts, janr)
    movies.append(new_film)
    print("Film successfuly added!")

def add_new_series(name, director, imdb_score, url, duration, casts):
    number_of_episodes = input("Enter number of episodes: ")
    janr = input("Enter janr: ")
    is_ended = input("is this series ended? ")
    new_series = Series(name, director, imdb_score, url, duration, casts, number_of_episodes, janr, is_ended)
    series.append(new_series)
    print("new series succesfuly added!")

def add_new_documantaries(name, director, imdb_score, url, duration, casts):
    subject = input("enter subject: ")
    new_documantary = Documentary(name, director, imdb_score, url, duration, casts, subject)
    documantaries.append(new_documantary)
    print("new documantary succesfuly added!")

def add_new_clip(name, director, imdb_score, url, duration, casts):
    category = input("enter category: ")
    new_clip = Clip(name, director, imdb_score, url, duration, casts, category)
    clips.append(new_clip)
    print("new clip succesfuly added!")

def search_media():
    result = Media.search_media(movies+series+documantaries+clips, input("enter media code or media name: "))
    if result:
        result.print_labels()
        result.show_info()
        return result
    else:
        print("Media not found.")
        return False

def edit_media():
    result = search_media()
    if result:
        result.edit()

def remove_media():
    code_or_name = input("enter media code or media name: ")
    found_in_movies = Media.search_media(movies, code_or_name)
    found_in_series = Media.search_media(series, code_or_name)
    found_in_documantaries = Media.search_media(documantaries, code_or_name)
    found_in_clips = Media.search_media(clips, code_or_name)
    if found_in_movies:
        movies.remove(found_in_movies)
    elif found_in_series:
        series.remove(found_in_series)
    elif found_in_documantaries:
        documantaries.remove(found_in_documantaries)
    elif found_in_clips:
        clips.remove(found_in_clips)
    print("media successfully removed!") if found_in_movies or found_in_series or found_in_documantaries or found_in_clips else print("media not found.")

def validation_hour(hour):
    if hour >= 0:
        return True
    return False

def validation_minute(minute):
    if minute >= 0 and minute < 60:
        return True
    return False

def search_by_time():
    print("!!!!! this feature only works between movies(not series, documantaries and clips)!!!!!")
    while True:
        try:
            time_1_hour = int(input("Enter first time hour: "))
            time_1_minute = int(input("Enter first time minute: "))
            time_2_hour = int(input("Enter seccond time hour: "))
            time_2_minute = int(input("Enter seccond time minute: "))
            if validation_hour(time_1_hour) and validation_minute(time_1_minute) and validation_hour(time_2_hour) and validation_minute(time_2_minute):
                break
            else:
                print("invalid. hour most greater than 0 and minute most be in range 0, 59. please enter again in corect format.")
        except:
            print("invalid input. please enter again in number format.")
    found_movies = Media.search_by_time(movies, time_1_hour, time_1_minute, time_2_hour, time_2_minute)
    Media.show_all(found_movies) if len(found_movies)>0 else print("No movies found in this range.")

def download_media():
    result = search_media()
    if result:
        print("Downloading................................")
        result.download()

menu = {
    "valid_inputs": ['1', '2', '3', '4', '5', '6', '7', "e"],
    "secondary_valid_inputs": ['a', 'b', 'c', 'd'],
    "main_menu": """---------------------------------------------
Enter number of your choice:
1- show medias
2- add new media
3- search
4- edit
5- remove
6- search by time
7- download a media
e- exit""",

    "select_media_menu": """Enter number of your choice:
a- Movies
b- Series
c- Documantaries
d- Clips""",

    "operations": {
        "1": select_media_to_show,
        "1a": show_movies,
        "1b": show_series,
        "1c": show_documantaries,
        "1d": show_clips,
        "1e": show_all_media,
        "2": select_media_to_add,
        "2a": add_new_film,
        "2b": add_new_series,
        "2c": add_new_documantaries,
        "2d": add_new_clip,
        "3": search_media,
        "4": edit_media,
        "5": remove_media,
        "6": search_by_time,
        "7": download_media,
        "e": exit_program
    }
}

print("Welcome to video media management!")
while True:
    print(menu["main_menu"])
    user_choice = input()
    menu["operations"][user_choice]() if user_choice in menu["valid_inputs"] else print("invalid input.")
