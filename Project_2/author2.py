class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
        

    def author_name(self):
        return self.name
    
    def author_bio(self):
        return self.biography
    
    def __str__(self):
        return f"Name: {self.name}, Biography: {self.biography}"