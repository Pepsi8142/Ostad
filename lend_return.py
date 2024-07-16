from _db import connection, cursor

def lend_book(user, book):
    cursor.execute('INSERT INTO books_users (book_id, user_id) VALUES (:book, :user)', {'user': user, 'book': book})
    cursor.execute('UPDATE books SET quantity = quantity - 1 WHERE id = :book', {'book': book})
    connection.commit()

def return_book(user, book):
    cursor.execute('DELETE FROM books_users WHERE book_id =:book AND user_id = :user', {'user': user, 'book': book})
    cursor.execute('UPDATE books SET quantity = quantity + 1 WHERE id = :book', {'book': book})
    connection.commit()
