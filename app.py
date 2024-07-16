import re
from _db import connection, cursor
from add import add_book
from list import list_books
from lend_return import lend_book, return_book
from remove import filter_books, remove_book

with open('init.sql', 'r') as sql_file:
    init_script = sql_file.read()

cursor.executescript(init_script)
connection.commit()

# Menu:
features = [
    '-- Quit --',
    'Add New Book',
    'View All Books',
    'Search Books',
    'Delete Book',
    'Lend Book',
    'Return Book'
]
print()
for i, x in enumerate(features):
    print(f'{i}. {x}')
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
print()

match choice:
    case '0':
        print('Thanks for visiting our Library!')
        exit(0)

    case '1':
        title = input('Enter the Title of the Book: ')
        isbn = input('Enter the ISBN of the Book: ')

        while True:
            year = input('Enter the publishing Year of the book: ')
            try:
                if re.search('^(19[7-9]|2[01][0-2])[0-9]$', year) is None:
                    raise Exception('Invalid year!')
            except Exception as e:
                print(e)
            else:
                break

        while True:
            price = input('Enter the Price of the Book: $')
            try:
                if re.search('^\\d{1,3}(\\.\\d{2})?$', price) is None:
                    raise Exception('Invalid price!')
            except Exception as e:
                print(e)
            else:
                break

        while True:
            quantity = input('Enter the Quantity of the Book: ')
            try:
                if re.search('^[1-9]\\d{0,2}$', quantity) is None:
                    raise Exception('Invalid quantity!')
            except Exception as e:
                print(e)
            else:
                break

        authors = []

        while True:
            print('\nLet\'s Add Author(s):')
            authors_options = ['-- Done --', 'Associate an Existing Author', 'Create and Associate a New Author']
            [print(f'{i}. {x}') for i, x in enumerate(authors_options)]
            authors_choice = input('Select an option: ')
            try:
                if authors_choice not in [str(n) for n in range(len(authors_options))]:
                    raise Exception('Invalid input!')
            except Exception as e:
                print(e)
            else:
                match(authors_choice):
                    case '0':
                        if len(authors) < 1:
                            print('No Author!')
                            continue
                        break
                    case '1':
                        try:
                            authors_list = cursor.execute('SELECT id, name FROM authors').fetchall()
                            [print(f'{a[0]}. {a[1]}') for a in authors_list]
                            author_choice = input('Choose an option: ')
                            if author_choice not in [str(a[0]) for a in authors_list]:
                                raise Exception('Invalid input!')
                        except Exception as e:
                            print(e)
                        else:
                            authors.append(author_choice)
                            print('Author has been associated successfully!')
                    case '2':
                        author_name = input('Enter Author\'s Name: ')
                        res = cursor.execute('INSERT INTO authors (name) VALUES (:name)', {'name': author_name})
                        connection.commit()
                        authors.append(res.lastrowid)
                        print('Author has been created successfully!')

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
            print(list_books())
        except Exception as e:
            print(e)

    case '3':
        term = input('Search Term: ')
        try:
            print(list_books(term))
        except Exception as e:
            print(e)

    case '4':
        term = input('Search Term: ')
        try:
            books_list = filter_books(term)
            if len(books_list) < 1:
                raise Exception('No books!')
            print('Choose A Book:')
            [print(f'{b[0]}. {b[1]} (ISBN: {b[2]})') for b in books_list]
            book_choice = input('Choose an option: ')
            if book_choice not in [str(b[0]) for b in books_list]:
                raise Exception('Invalid input!')
            remove_book(book_choice)
            print('Book has been deleted successfully!')
            print(list_books())
        except Exception as e:
            print(e)

    case '5':
        while True:
            try:
                books_list = cursor.execute('SELECT id, title, isbn FROM books WHERE quantity > 0').fetchall()
                if len(books_list) < 1:
                    raise Exception('No Available Books!')                                    
                print('Choose A Book:')
                [print(f'{b[0]}. {b[1]} (ISBN: {b[2]})') for b in books_list]
                book_choice = input('Choose: ')
                if book_choice not in [str(b[0]) for b in books_list]:
                    raise Exception('Invalid input!')
            except Exception as e:
                print(e)
            else:
                users_options = ['-- Cancel --', 'Lend an Existing User', 'Create and Lend a New User']
                [print(f'{i}. {x}') for i, x in enumerate(users_options)]
                users_choice = input('Select: ')
                try:
                    if users_choice not in [str(n) for n in range(len(users_options))]:
                        raise Exception('Invalid input!')
                except Exception as e:
                    print(e)
                else:
                    match(users_choice):
                        case '0':
                            print('Cancelled!')
                            exit(0)
                        case '1':
                            try:
                                users_list = cursor.execute('SELECT id, name FROM users').fetchall()
                                if len(users_list) < 1:
                                    print('No User!')
                                    continue
                                [print(f'{a[0]}. {a[1]}') for a in users_list]
                                user_choice = input('Choose: ')
                                if user_choice not in [str(u[0]) for u in users_list]:
                                    raise Exception('Invalid input!')
                                lend_book(user_choice, book_choice)
                                print('\nBook has been lent successfully!')
                                break
                            except Exception as e:
                                print(e)
                        case '2':
                            try:
                                user_name = input('User\'s Name: ')
                                res = cursor.execute('INSERT INTO users (name) VALUES (:name)', {'name': user_name})
                                connection.commit()
                                lend_book(res.lastrowid, book_choice)
                                print('\nBook has been lent successfully!')
                                break
                            except Exception as e:
                                print(e)

    case '6':
        while True:
            try:
                users_list = cursor.execute('SELECT id, name FROM users RIGHT JOIN books_users ON user_id = id').fetchall()
                if len(users_list) < 1:
                    print('No Users!')
                    break
                print('Choose A User:')
                [print(f'{u[0]}. {u[1]}') for u in users_list]
                user_choice = input('Choose: ')
                if user_choice not in [str(u[0]) for u in users_list]:
                    raise Exception('Invalid input!')
                books_list = cursor.execute('SELECT id, title, isbn FROM books LEFT JOIN books_users ON book_id = id WHERE user_id = :user', {'user': user_choice})
                print('Choose A Book:')
                [print(f'{b[0]}. {b[1]} (ISBN: {b[2]})') for b in books_list]
                book_choice = input('Choose: ')
                return_book(user_choice, book_choice)
                print('\nBook has been returned successfully!')
                break
            except Exception as e:
                print(e)
