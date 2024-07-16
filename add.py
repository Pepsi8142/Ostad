from _db import connection, cursor

def add_book(info):
    res = cursor.execute(
        'INSERT INTO books (title, isbn, year, price, quantity) VALUES (:title, :isbn, :year, :price, :quantity)',
        {
            'title': info['title'],
            'isbn': info['isbn'],
            'year': info['year'],
            'price': info['price'],
            'quantity': info['quantity']
        }
    )
    connection.commit()
    book_id = res.lastrowid

    for author_id in info["authors"]:
        cursor.execute(
            'INSERT INTO books_authors (book_id, author_id) VALUES (:book_id, :author_id)',
            {
                'author_id': author_id,
                'book_id': book_id
            }
        )
    connection.commit()

    print('\nBook has been added successfully!')
