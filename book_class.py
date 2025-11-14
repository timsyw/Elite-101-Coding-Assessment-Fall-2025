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
    
    '''
    def checkout(self, when_it_is_due):
        if self.available = True:
            # if it is available this next parts should run

            # this below sets the availability in the current object to false pretty self explainatory.
            self.available = False

            # I had AI help me heavily with this part. 
            # It was hard setting the due date to 2 weeks later.
            # datetime is foreign to me, and I had to dig through a bunch of online web documentation
            # in order to get it to work properly
            self.due_date = when_is_it_due
        else:
            print(f"The book you are searching for is not here. The book will be back {self.due_date}")
    '''