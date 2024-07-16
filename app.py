import re
import sqlite3

from add_book import add_book
from list_books import list_books

with open('init.sql', 'r') as sql_file:
    init_script = sql_file.read()

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
cur.executescript(init_script)
con.commit()

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
        con.close()
        exit(0)
    case '1':
        title = input('Title: ')
        isbn = input('ISBN: ')

        while True:
            year = input('Year: ')
            try:
                if re.search('^(19[7-9]|2[01][0-2])[0-9]$', year) is None:
                    raise Exception('Invalid year!')
            except Exception as e:
                print(e)
            else:
                break

        while True:
            price = input('Price: $')
            try:
                if re.search('^\\d{1,3}(\\.\\d{2})?$', price) is None:
                    raise Exception('Invalid price!')
            except Exception as e:
                print(e)
            else:
                break

        while True:
            quantity = input('Quantity: ')
            try:
                if re.search('^[1-9]\\d{0,2}$', quantity) is None:
                    raise Exception('Invalid quantity!')
            except Exception as e:
                print(e)
            else:
                break

        authors = []

        while True:
            authors_options = ['-- Done --', 'Associate an Existing Author', 'Create and Add a New Author']
            [print(f'{i}. {x}') for i, x in enumerate(authors_options)]
            authors_choice = input('Select: ')

            try:
                if authors_choice not in [str(n) for n in range(len(authors_options))]:
                    raise Exception('Invalid input!')
            except Exception as e:
                print(e)
            else:
                match(authors_choice):
                    case '0':
                        if len(authors) < 1:
                            print('No Authors!')
                            continue
                        break
                    case '1':
                        cur = con.cursor()
                        res = cur.execute('SELECT id, name FROM authors')
                        authors_list = res.fetchall()
                        print(authors_list)
                    case '2':
                        author_name = input('Author\'s Name: ')
                        cur = con.cursor()
                        res = cur.execute('INSERT INTO authors (name) VALUES (:name)', {'name': author_name})
                        con.commit()
                        authors.push(res.lastrowid)

        try:
            add_book({
            'title': title,
            'isbn': isbn,
            'year': year,
            'price': price,
            'quantity': quantity,
            'authors': authors
        })
        except Exception as e:
            print(e)

    case '2':
        try:
            list_books()
        except Exception as e:
            print(e)
