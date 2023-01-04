from media import Media

class Series(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, number_of_episodes, janr,  is_ended):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.number_of_episodes = number_of_episodes
        self.janr = janr
        self.is_ended = is_ended

    def show_info(self):
        print(f"{self.code}\t\t{self.name}\t\t{self.director}\t\t{self.imdb_score}\t\t{self.duration}\t\t", end="")
        self.print_actors()
        print("\t", self.janr,'\t', self.number_of_episodes)
    
    def print_labels(self):
        print("Code\t\tName\t|\tDirector\t|\tIMDB_score\t|\tduration\t|\tcasts\t|\tjanr\t|\tnumber of episodes")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
