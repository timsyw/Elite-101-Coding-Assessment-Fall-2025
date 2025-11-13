from library_books import library_books
from datetime import datetime, timedelta
from book_class import BookClass



def add_dictionaries_to_book_classes(list_of_books):
    for count in range(len(list_of_books)):
        BookClass(
            list_of_books[count]["id"], 
            list_of_books[count]["title"], 
            list_of_books[count]["author"], 
            list_of_books[count]["genre"], 
            list_of_books[count]["available"], 
            list_of_books[count]["due_date"], 
            list_of_books[count]["checkouts"]
            )

def print_all_books_available():
    print("------\nThese are the available books:\n------")

    # after much trial and error, I have come to conclude:
    #that you cannot just use BookClass.book_log_objects as a list of dictionaries
    #Instead I have decided to unload all of the objects into a variable.
    #Just so we are clear, I did use chatGPT to figure out:
    #why the list of objects was not acting like a list of dictionaries
    all_of_books = BookClass.book_log_objects

    for count in range(len(all_of_books)):
        #book that is current

        book_current = all_of_books[count]

        if book_current.available == True:
            print(f"object order--> {count}")
            print(f"Book ID (id)         : {book_current.id}")
            print(f"Name of Book (title) : {book_current.title}")
            print(f"Author               : {book_current.author}")
            print(f"Genre of Book (genre): {book_current.genre}")
            print(f"Is it available?     : {book_current.available}")
            print(f"Due Date             : {book_current.due_date}")
            print(f"How many checkouts   : {book_current.checkouts}")
            print("")


add_dictionaries_to_book_classes(library_books)
print_all_books_available()
checkout_book()