import sqlite3

from add_book import add_book
from list_books import list_books

with open('init.sql', 'r') as sql_file:
    init_script = sql_file.read()

# Initialize SQLite DB with data
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
cur.executescript(init_script)
con.commit()
con.close()

features = ['-- Quit --', 'Add New Book', 'View All Books', 'Search Books']

[print(f'{i}. {x}') for i, x in enumerate(features)]


'''
We're checking if `choice` is within the indices of `features`.

Since `choice` is of type `str`, we're returning a new list
by looping through `features`, taking out the indices, and
changing its type to `str` on the fly. So that the types match.
'''
while True:
    choice = input('Select An Option: ')
    try:
        if choice not in [str(n) for n in range(len(features))]:
            raise Exception('Invalid input!')
    except Exception as e:
        print(e)
    else:
        break

match choice:
    case '0':
        print('Thanks!')
        exit(0)
    case '1':
        title = input('Title: ')
        isbn = input('ISBN: ')
        year = input('Year: ')
        price = input('Price: $')
        quantity = input('Quantity: ')

        # Authors:
        # 1. Associate an Existing Author
        # 2. Create New Author

        # If 1 is chosen, show all authors from DB.
        # If 2 is chosen, prompt to get author's name.

        author_name = input('Author\'s Name: ')
        
        # authors = []

        # ...

        info = {
            'title': title,
            'isbn': isbn,
            'year': year,
            'price': price,
            'quantity': quantity,
            'author': {
                'name': author_name
            }
        }
        
        try:
            add_book(info)
        except Exception as e:
            print(e)

    case '2':
        try:
            list_books()
        except Exception as e:
            print(e)
