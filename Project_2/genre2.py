
class Genre():

    def __init__(self, name, description):
        
        
        self.name = name
        self.description = description
        self.genres = {}
        

    def new_genre(self):
        genre = input("What is the new genre? ")
        description = input("Describe the genre: ")
        nested = {"Genre": {genre}, "Description": {description}}
        self.genres = nested
        
        

    def genre_names(self):
        return f"Genre: {self.name}"

