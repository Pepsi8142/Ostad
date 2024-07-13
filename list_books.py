import sqlite3

def list_books():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    res = cur.execute('SELECT books.id AS id, title, isbn, year, price, quantity, authors.name AS author_name FROM books LEFT JOIN books_authors ON books_authors.book_id = books.id LEFT JOIN authors ON books_authors.author_id = authors.id')
    for row in res.fetchall():
        print(row)