# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

from library_books import library_books
from book_class import BookClass
from function_flow import function_flow
from general_functions import print_message, ask_user_next, print_options
from program_state import program_is_running

#creates a bunch of objects based on library list of dictionaries. Creates a list of references.
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


#variables
current_message_id = 0



#add the parts of the library to objects stored in the list of the class
add_dictionaries_to_book_classes(library_books)


if __name__ == "__main__":
    while program_is_running == True:

        #prints the starting message
        print_message(current_message_id)

        #prints the options of functions to run from the main homepage. returns the number of options that the user is given 
        current_number_of_options = print_options(current_message_id)
        #asks the user to answer the question of 
        current_message_id = ask_user_next(current_message_id, current_number_of_options)

        #print_all_books_available()
        #search_through_books()
        #checkout_book()

        #program_is_running = False

    print("Thanks for Using this Library Program!\n\n")



