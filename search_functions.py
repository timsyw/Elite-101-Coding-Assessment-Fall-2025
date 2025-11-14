from book_class import BookClass
from general_functions import print_specific_book, end_of_action_question, end_program


def search_input(messageid):
    return input(f"What {messageid} would you like to search for?\n--> ")

def search_by_thing(type_of_search, item_of_search):
    print(f"------Books with \"{item_of_search}\" as their {type_of_search}------")
    found_book = False
    for count in BookClass.book_log_objects:
        #basically you cant just used count.type_of_search.lower()
        #idk why this wasnt working until I found the object we are looking for is not in type_of_search
        #this is because this is just a refrence and not an actual dictionary.
        #later I figured out that you can just get getattr to ger the attribute that is in the object
        #update: I have switched the == to be "in" because it will give a broader range of search.
        if item_of_search.lower() in getattr(count, type_of_search).lower():
            print_specific_book(count)
            found_book = True
    if not found_book:
        print(f"No books found for this {type_of_search}.")



def search_through_books():
    print("\n------Here you can search through books------\n")
    search_type = "title"
    # while loop to figure out what type of search
    while True:
        # ask for type of search
        user_response_type = input("Would you like to search for author, genre, or title?\n--> ")
        user_response_type = user_response_type.lower()
        # creates variable for the final type of search before moving on
        
        if user_response_type == "author":
            search_type = "author"
            break
        elif user_response_type == "genre":
            search_type = "genre"
            break
        elif user_response_type == "title":
            search_type = "title"
            break
        else:
            print("Oh no! You must have entered something wrong! Please try again.")

    #asks the user for the name of whatever type of thing they are looking for. very handy
    search_thing = search_input(search_type)
    
    if search_type == "author":
        search_by_thing(search_type, search_thing)
    elif search_type == "genre":
        search_by_thing(search_type, search_thing)
    elif search_type == "title":
        search_by_thing(search_type, search_thing)
    else:
        print("!!!! something broke")
    
    end_of_action = end_of_action_question()

    if end_of_action == "return end":
        return
    elif end_of_action == "continue":
        search_through_books()
    print("\nReturning to Menu\n")
    