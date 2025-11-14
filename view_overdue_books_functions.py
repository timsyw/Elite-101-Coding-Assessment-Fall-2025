from book_class import BookClass
from datetime import datetime
from general_functions import print_specific_book

def view_overdue_books():
    all_of_books = BookClass.book_log_objects
    today_date = datetime.now().date()

    overdue_stuff_list = []

    for count in all_of_books:
        #some more tricky code. if the current objects availabilty is false adn the due date is something other than none, then proceed
        #this narrows down everything
        if count.available is False and count.due_date is not None:

            try:
                #here is some more code I had to google. th
                object_due_date = datetime.strptime(count.due_date, "%Y-%m-%d").date()
            except ValueError:
                continue

            if object_due_date < today_date:
                overdue_stuff_list.append(count)
    
    #if the ligth of the list is 0 then we can assume that we have no overdue books.
    if len(overdue_stuff_list) == 0:
        print("\nThere is not a single overdue book for some reason idk?")
        return
    
    
    print("\n---OVerdue Books---")
    #just uses the print specific one so I dont hjave to right everythin all the time lol
    for count1 in overdue_stuff_list:
        print_specific_book(count1)