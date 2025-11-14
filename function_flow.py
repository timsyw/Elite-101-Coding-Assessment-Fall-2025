from veiw_available_functions import print_all_books_available, all_books_available_print
from search_functions import search_through_books
from checkout_functions import checkout_book
from general_functions import pathway_with_no_function_yet, end_program
from return_book_functions import book_return
from view_overdue_books_functions import view_overdue_books


function_flow = [
    {
        "message": "------Main Menu------",
        "options": [
            "View Available Books",
            "Search",
            "Checkout",
            "Return",
            "View Overdue Books",
            "View top 3 most checked-out books",
            "End Program"
        ],
        "next": [0, 0, 0, 0, 0, 0, 0],
        "functions": [
            all_books_available_print,
            search_through_books,
            checkout_book,
            book_return,
            view_overdue_books,
            pathway_with_no_function_yet,
            end_program
        ]
    }
]
