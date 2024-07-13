import re
import sqlite3

def add_book(info):
    # if len(info.isbn) !== 10:
    #     raise Exception('Incorrect ISBN value!')

    if re.search('^(19[7-9]|2[01][0-2])[0-9]$', info['year']) is None:
        raise Exception('Invalid year!')
    
    if re.search('^\\d{1,3}(\\.\\d{2})?$', info['price']) is None:
        raise Exception('Invalid price!')
    
    if re.search('^[1-9]\\d{0,2}$', info['quantity']) is None:
        raise Exception('Invalid quantity!')

    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    res = cur.execute('INSERT INTO authors (name) VALUES (:name)', {'name': info['author']['name']})
    con.commit()
    author_id = res.lastrowid

    res = cur.execute(
        'INSERT INTO books (title, isbn, year, price, quantity) VALUES (:title, :isbn, :year, :price, :quantity)',
        {
            'title': info['title'],
            'isbn': info['isbn'],
            'year': info['year'],
            'price': info['price'],
            'quantity': info['quantity']
        }
    )
    con.commit()
    book_id = res.lastrowid

    res = cur.execute(
        'INSERT INTO books_authors (book_id, author_id) VALUES (:book_id, :author_id)',
        {
            'author_id': author_id,
            'book_id': book_id
        }
    )
    con.commit()

    print('Book has been added successfully!')
