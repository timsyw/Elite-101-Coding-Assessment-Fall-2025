from datetime import datetime, timedelta

class BookClass:
    #this is used to log all of the objects we have created
    book_log_objects = []

    def __init__(self, idb, title, author, genre, available, due_date, checkouts):
        self.id = idb
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
        #current object adds itself to the list of other class objects
        BookClass.book_log_objects.append(self)
    
    #update: removed when_it_is_due because I decided to just autimatically do it in the method
    def checkout(self):
        if self.available == True:
            #if it is available this next parts should run

            #this below sets the availability in the current object to false pretty self explainatory.
            self.available = False

            #I had AI help me heavily with this part. 
            #It was hard setting the due date to 2 weeks later.
            #datetime is foreign to me, and I had to dig through a bunch of online web documentation
            #in order to get it to work properly

            #basically the due variable is set to the time right now plus 14 days in the future (according to time delta)
            due = datetime.now() + timedelta(days=14)
            #idk how to explain this one. It has to do with the date amounts. You only want to change the day. I had AI write this line for me.
            self.due_date = due.strftime("%Y-%m-%d")
            
            #add another checkout. this was really easy to understand.
            self.checkouts += 1

            print(f"You have checked out \"{self.title}\"! Remeber that it's due on {self.due_date}!")
        else:
            print(f"\nOh no!\n\nThe book \"{self.title}\" is not available at the moment! It will be back on {self.due_date}.")
    