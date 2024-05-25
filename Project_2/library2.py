from book2 import Book
from user2 import User
from genre2 import Genre
from author2 import Author


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.user = []
        self.borrowed_book = []
        self.authors = []

#=========Book Operations==========
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter isbn: ")
        publication_date = input("Enter publication date: ")
        book_genre = input("Whats the books genre? ")
        genre_description = input("Describe the genre: ")
        genre = Genre(book_genre, genre_description)
        new_book = Book(title, author, isbn, publication_date, genre)
        self.books.append(new_book)

    def checkout_book(self):
        library_id = input("What is the library id? ")
        user = self.find_user(library_id)
        if user is None:
            print("Not a valid id")
            return

        isbn = input("isbn: ")
        book_found = False
        for book in self.books:
            if book.get_isbn() == isbn:
                book_found = True
                if book.is_available():
                    try:
                        user.borrow_book(book)
                        book.borrow_book()
                        print(f"Book '{book.get_name()}' checked out to {user.get_name()}")
                    except ValueError as e:
                        print(f"An error occurred: {e}")
                else:
                    print("That book is unavailable or not found.")
                break
        if not book_found:
            print("Book not found.")

    def checkin_book(self):
        library_id = input("Enter your library id: ")   
        user = self.find_user(library_id)
        if user is None:
            print("User Not Found.")
            return
        
        isbn = input("isbn: ")
        for book in self.books:
            if book.get_isbn() == isbn and not book.is_available():
                try:
                    user.return_book(book)
                    book.return_book()
                    print(f"Book '{book.title}' returned successfully by {user.name}.")
                except ValueError as e:
                    print(f"An error occurred: {e}")
                    return
        print("Book not found.")

    def search_books(self):
        search = input("isbn: ")
        for book in self.books:
            if book.get_isbn() == search or book.get_title.title() == search.title():
                print(book)
                return
            print("Book not found.")                
    
    def all_books(self):
        if not self.books:
            print("No books available.")
        else:    
            for book in self.books:
                print(book)     

#=========User Operations==========

    def add_user(self):
        name = input("Enter name: ")
        library_id = "ID" + str(len(self.users) + 1).zfill(3)
        new_user = User(name, library_id)
        self.users.append(new_user)
        print(f"Library ID: {library_id}")
        return new_user
    
    def find_user(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                return user
        return None
        
    def user_details(self):
        library_id = input("Library id: ")
        user = self.find_user(library_id)
        if user:
            print(user)
        else:
            print("User not found.")
            
    def all_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            print(user)
            
#=========Author Operations==========
    def add_author(self):
        name = input("Authors name: ")
        biography = input("Brief bio about author: ")
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print(f"{name} added to authors.")
        return new_author
    
    def author_details(self):
        author_name = input("Authors name: ")
        for author in self.authors:
            if author.name() == author_name:
                print(f"Name: {author.name()}")
                print(f"Biography: {author.biography()}")
                return
        else:
            print("Author not found.")    
            
    def all_authors(self):         
        if not self.authors:
            print("Author not found.")
        for book in self.authors:
            print(self.authors)
  
            
#=========Genre Operations==========

    def add_genre(self):
        genre_name = input("Genre: ")
        description = input("Describe the genre: ")
        new_genre = Genre(genre_name, description)
        self.genres.append(new_genre)
        print(f"{genre_name} added  to genres.")
        return new_genre
    
    def genre_details(self):
        genre_name = input("Genre name: ")
        genre = self.find_genre(genre_name)
        if genre:
            print(genre)
        else:
            print("Genre not found.")
            
    def all_genres(self):         
        if not self.authors:
            print("Genre not found.")
        for genre in self.genres:
            print(self.genres)