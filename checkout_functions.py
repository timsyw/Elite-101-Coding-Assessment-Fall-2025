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