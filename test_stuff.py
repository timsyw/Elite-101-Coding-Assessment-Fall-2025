from library_books import library_books
from datetime import datetime, timedelta
from book_class import BookClass
from function_flow import function_flow

# attach functions after import
function_flow[0]["functions"] = [
    print_all_books_available,
    search_through_books,
    checkout_book,
    pathway_with_no_function_yet,
    pathway_with_no_function_yet,
    pathway_with_no_function_yet
]


# variables
current_message_id = 0

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


def pathway_with_no_function_yet():
    print("This has not been made yet.")



#add the parts of the library to objects stored in the list of the class
add_dictionaries_to_book_classes(library_books)
program_is_running = True
while program_is_running == True:
    
    print_message(current_message_id)
    current_number_of_options = print_options(current_message_id)
    current_message_id = ask_user_next(current_message_id, current_number_of_options)
    #print_all_books_available()
    #search_through_books()
    #checkout_book()

    program_is_running = False