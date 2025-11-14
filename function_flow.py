from library_functions import (
    print_all_books_available,
    search_through_books,
    checkout_book,
    pathway_with_no_function_yet
)

function_flow = [
    {
        "message": "here is the menu",
        "options": [
            "View available books",
            "Search",
            "Checkout",
            "Return",
            "View Overdue Books",
            "View top 3 most checked-out books"
        ],
        "next": [0, 0, 0, 0, 0, 0],
        "functions": [
            print_all_books_available,
            search_through_books,
            checkout_book,
            pathway_with_no_function_yet,
            pathway_with_no_function_yet,
            pathway_with_no_function_yet
        ]
    }
]
