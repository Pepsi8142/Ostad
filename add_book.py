import sqlite3

def add_book(info):
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
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

    for author_id in info["authors"]:
        res = cur.execute(
            'INSERT INTO books_authors (book_id, author_id) VALUES (:book_id, :author_id)',
            {
                'author_id': author_id,
                'book_id': book_id
            }
        )
    con.commit()

    print('Book has been added successfully!')
