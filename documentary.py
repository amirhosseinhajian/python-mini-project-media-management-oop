from media import Media

class Documentary(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, subject):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.subject = subject
    
    def show_info(self):
        print(f"{self.code}\t\t{self.name}\t\t{self.director}\t\t{self.imdb_score}\t\t{self.duration}\t\t", end="")
        self.print_actors()
        print("\t", self.subject)
    
    def print_labels(self):
        print("Code\t\tName\t|\tDirector\t|\tIMDB_score\t|\tduration\t|\tcasts\t|\tsubject")
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
