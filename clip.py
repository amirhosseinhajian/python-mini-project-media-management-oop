from media import Media

class Clip(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, category):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.category = category
    
    def show_info(self):
        print(f"{self.code}\t\t{self.name}\t\t{self.director}\t\t{self.imdb_score}\t\t{self.duration}\t\t", end="")
        self.print_actors()
        print("\t", self.category)
    
    def print_labels(self):
        print("Code\t\tName\t|\tDirector\t|\tIMDB_score\t|\tduration\t|\tcasts\t|\tcategory")
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
