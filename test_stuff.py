from library_books import library_books
from book_class import BookClass
from function_flow import function_flow
from general_functions import print_message, ask_user_next, print_options





#variables
current_message_id = 0


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






#add the parts of the library to objects stored in the list of the class
add_dictionaries_to_book_classes(library_books)

#main loop
program_is_running = True
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