from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from actor import Actor

class DB:
    def __init__(self):
        # Config Database files path
        self.database_dir = "./database/"
        self.movies_file_name = "movies.txt"
        self.series_file_name = "series.txt"
        self.clips_file_name = "clips.txt"
        self.documantary_file_name = "documantary.txt"

    def get_all_medias(self):
        movies = self.model_movie(self.read_from_database(self.movies_file_name))
        series = self.model_series(self.read_from_database(self.series_file_name))
        documantaries = self.model_documantary(self.read_from_database(self.documantary_file_name))
        clips = self.model_clip(self.read_from_database(self.clips_file_name))
        return movies, series, documantaries, clips

    def read_from_database(self, file_name):
        file = open(self.database_dir + file_name, "r")
        result = []
        for line in file:
            result.append(line.split(","))
        file.close()
        return result

    def model_actors(self, actors):
        actor_objects = []
        for actor in actors:
            actor_objects.append(Actor(actor))  
        return actor_objects

    def model_movie(self, movies):
        movies_objects = []
        for movie in movies:
            movies_objects.append(Film(movie[0], movie[1],movie[2],movie[3],movie[4],self.model_actors(movie[5].split("-")),movie[6]))
        return movies_objects

    def model_series(self, series_s):
        series_objects = []
        for series in series_s:
            series_objects.append(Series(series[0], series[1],series[2],series[3],series[4],self.model_actors(series[5].split("-")),series[6], series[7], series[8]))
        return series_objects
    
    def model_documantary(self, documantaries):
        documantaries_object = []
        for documantary in documantaries:
            documantaries_object.append(Documentary(documantary[0], documantary[1],documantary[2],documantary[3],documantary[4],self.model_actors(documantary[5].split("-")),documantary[6]))
        return documantaries_object

    def model_clip(self, clips):
        clip_objects = []
        for clip in clips:
            clip_objects.append(Clip(clip[0], clip[1],clip[2],clip[3],clip[4],self.model_actors(clip[5].split("-")),clip[6]))
        return clip_objects

    def save_to_database(self, direction, media_list):
        file = open(direction, "w")
        for media in media_list:
            file.write(f"{media.name},{media.director},{media.imdb_score},{media.url},{media.duration},")
            for i, actor in enumerate(media.casts):
                if i !=len(media.casts)-1:
                    file.write(f"{actor.name}-")
                else:
                    file.write(f"{actor.name},")
            remain_items = list(media.__dict__.values())[7:]
            for index, item in enumerate(remain_items):
                if index != len(remain_items)-1:
                    file.write(f"{item},")
                else:
                  file.write(item)  

    def write_to_database(self, film_list, series_list, documantaries_list, clip_list):
        # save movies
        self.save_to_database(self.database_dir+self.movies_file_name, film_list)
        # save series
        self.save_to_database(self.database_dir+self.series_file_name, series_list)
        # save documantaries
        self.save_to_database(self.database_dir+self.documantary_file_name, documantaries_list)
        # save clips
        self.save_to_database(self.database_dir+self.clips_file_name, clip_list)
