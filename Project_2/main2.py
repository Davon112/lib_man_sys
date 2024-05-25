from library2 import Library

def main_menu():
    library = Library()
    print("Welcome to the Library Managment System!")
    while True:
        print("""\n Main Menu:
        1. Book Operations 
        2. User Operations
        3. Author Operations
        4. Genre Operations
        5. Quit""")
        lms_input = input("Enter Selection: ")


# ==============BOOK OPERATIONS============       
        try: 
            if lms_input == "1":
                print("""\nBook Operations Menu:
        1 - Add a new book
        2 - Borrow a book
        3 - Return a book
        4 - Search for a book
        5 - Display all books
        6 - Exit to main menu """)
                book_input = input("\nEnter choice: ")
                if book_input == "1":
                    library.add_book()
                elif book_input == "2":
                    library.checkout_book()
                elif book_input == "3":
                    library.checkin_book()
                elif book_input == "4":
                    library.search_books()
                elif book_input == "5":
                    library.all_books()
                elif book_input == "6":
                    break
                else:
                    print("Please enter a valid choice")
        except Exception as e:
            print(f"An error occurred: {e}")

        
# ==============USER OPERATIONS=============        
        try: 
            if lms_input == "2":
                print("""\nUser Operations Menu:
        1 - Add a new user
        2 - View user details
        3 - Display all users
        4 - Exit to main menu""")
                user_input = input("\nEnter choice: ")
                if user_input == "1":
                    library.add_user()
                elif user_input == "2":
                    library.user_details()
                elif user_input == "3":
                    library.all_users()
                elif user_input == "4":
                    return
                else:
                    print("Please enter a valid choice")
        except Exception as e:
            print(f"An error occurred: {e}")


# ==============AUTHOR OPERATIONS=============
        try: 
            if lms_input == "3":
                print("""\nAuthor Operations Menu:
        1 - Add a new author
        2 - View author details
        3 - Display all authors
        4 - Exit to main menu""")
                author_input = input("\nEnter choice: ")
                if author_input == "1":
                    library.add_author()
                elif author_input == "2":
                    library.author_details()
                elif author_input == "3":
                    library.all_authors()
                elif author_input == "4":
                    return
                else:
                    print("Please enter a valid choice")
        except Exception as e:
            print(f"An error occurred: {e}")


# ==============GENRE OPERATIONS=============            
        try: 
            if lms_input == "4":
                print("""\nGenre Operations Menu:
        1 - Add a new genre
        2 - View genre details
        3 - Display all genres
        4 - Exit to main menu""")
                genre_input = input("\nEnter choice: ")
                if genre_input == "1":
                    library.add_genre()
                elif genre_input == "2":
                    library.genre_details()
                elif genre_input == "3":
                    library.all_genres()
                elif genre_input == "4":
                    return
                else:
                    print("Please enter a valid choice")
        except Exception as e:
            print(f"An error occurred: {e}")  
        if lms_input == "5":
            print("\nExiting the program...")
            break

if __name__ == "__main__":
    main_menu()