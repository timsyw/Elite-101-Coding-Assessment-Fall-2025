from book_class import BookClass
from general_functions import end_of_action_question

#old code it was broken 
'''


def checkout_book():
    
    # I will tell you exactly what the parts I needed are.
    # I understood how to use the unloading of objects from an object list
    # but I did not know you could access the variables of an object using the unpacked refrences.
    all_books = BookClass.book_log_objects
    needed_book_id = input("Please enter a book ID: ")

    for count in all_books:
        if count.id == needed_book_id:
            count.checkout()
            return
'''

#I rewrote it with a cleaner mind.


def checkout_book():
    all_books = BookClass.book_log_objects
    needed_book_id = input("Please enter a book ID: ")

    for count in all_books:
        if count.id == needed_book_id:
            count.checkout()
            print("You will be returned to main menu.\n")

            return
    
    print("No book with that ID exists.")

    end_of_action = end_of_action_question()

    if end_of_action == "return end":
        return
    elif end_of_action == "continue":
        checkout_book()
    print("\nReturning to Menu\n")
