from _db import cursor
import json


def list_books(term=None):
    stmt = 'SELECT id, title, isbn, year, price, quantity FROM books'
    params = {}
    if term:
        stmt += ' WHERE title LIKE :term OR isbn LIKE :term'
        params['term'] = f'%{term}%'
    books = cursor.execute(stmt, params).fetchall()
    for book in books:
        authors = cursor.execute(
            'SELECT id, name FROM authors RIGHT JOIN books_authors ON author_id = id WHERE book_id = :book',
            {'book': book[0]}
        ).fetchall()
    return json.dumps(
        [{'id': b['id'], 'title': b['title'], 'isbn': b['isbn'], 'year': b['year'], 'price': b['price'], 'quantity': b['quantity'], 'authors': [{'id': a['id'], 'name': a['name']} for a in authors]} for b in books],
        indent=4
    )

