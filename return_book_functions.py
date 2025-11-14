from book_class import BookClass
from general_functions import end_of_action_question

#this one is a lot like the checkout one.
def book_return():
    
    all_books = BookClass.book_log_objects
    needed_book_id = input("Please enter a book ID to return: ")

    for count in all_books:
        if count.id == needed_book_id:

            count.return_book()
            print("You will be returned to main menu.\n")

            return
    
    print("No book has that ID")

    #I need to do this because it must always be updated.
    

    end_of_action = end_of_action_question()

    if end_of_action == "return end":
        return
    elif end_of_action == "continue":
        book_return()
    print("\nReturning to Menu...\n")