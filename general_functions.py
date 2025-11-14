def try_user_input_int():
    while True:
        try:
            user_input = int(input("Enter this:\n--> "))
            break
        except ValueError:
            print("Please input a number that is an integer!")
    return user_input

def run_function_from_flow(index1, function1):
    #update: added () at end and did [function-1]
    function_flow[index1]["functions"][function1-1]()

def print_message(messageid):
    print(function_flow[messageid]["message"])
    print("")

def print_options(messageid):
    current_options = function_flow[messageid]["options"]
    count_number_of_options = 0
    for count in current_options:
        count_number_of_options += 1
        print(f"{count_number_of_options}. {count}")
    return count_number_of_options

def ask_user_next(messageid, numberOfOptions):
    user_number = -1
    user_number = try_user_input_int()
    print("")
    while True:
        if user_number > 0 & user_number <= numberOfOptions:
            break
        else:
            print("Please enter a number only in the list of options!\n")
            user_number = try_user_input_int()
            print("")
    run_function_from_flow(messageid, user_number)
    return function_flow[messageid]["next"][user_number-1]


#object related
def print_specific_book(book_inputed):
    print(f"---")
    print(f"Book ID (id)         : {book_inputed.id}")
    print(f"Name of Book (title) : {book_inputed.title}")
    print(f"Author               : {book_inputed.author}")
    print(f"Genre of Book (genre): {book_inputed.genre}")
    print(f"Is it available?     : {book_inputed.available}")
    print(f"Due Date             : {book_inputed.due_date}")
    print(f"How many checkouts   : {book_inputed.checkouts}")
    print("---\n")