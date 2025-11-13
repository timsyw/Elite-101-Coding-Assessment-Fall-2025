from datetime import datetime, timedelta

class BookClass:
    # this is used to log all of the objects we have created
    book_log_objects = []

    def __init__(self, idb, title, author, genre, available, due_date, checkouts):
        self.id = idb
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
        # current object adds itself to the list of other class objects
        BookClass.book_log_objects.append(self)
    
    def checkout(self):
        self.available = False
        