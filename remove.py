from _db import connection, cursor

def filter_books(term=None):
    stmt = 'SELECT id, title, isbn FROM books WHERE id NOT IN (SELECT book_id FROM books_users) AND quantity > 0'
    params = {}
    if term:
        stmt += ' AND (title LIKE :term OR isbn LIKE :term)'
        params['term'] = f'%{term}%'
    books = cursor.execute(stmt, params).fetchall()
    return books

def remove_book(id):
    cursor.execute('DELETE FROM books WHERE id = :id', {'id': id})
    connection.commit()
