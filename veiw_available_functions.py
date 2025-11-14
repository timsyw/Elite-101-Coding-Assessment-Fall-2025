def print_all_books_available():
    print("------These are the available books.------")

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
            print_specific_book(book_current)

