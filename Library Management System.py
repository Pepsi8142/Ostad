from data import save_data, load_data

books = load_data()  # Load existing books on startup


def add_book():
    # Get book details from user
    title = input("Enter book title: ")
    authors = input("Enter author(s) separated by commas: ").split(",")
    isbn = input("Enter ISBN: ")
    year = int(input("Enter publishing year: "))
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    # Create book dictionary
    book = {
      "title": title,
      "authors": authors,
      "isbn": isbn,
      "year": year,
      "price": price,
      "quantity": quantity,
      "lent": []  # List to store borrowed information
    }

    books.append(book)
    save_data(books)
    print("Book added successfully!")


def view_books():
    if not books:
        print("No books found!")
        return

    print("{:30} {:20} {:15} {:10}".format("Title", "Author(s)", "ISBN", "Quantity"))
    for book in books:
        print("{:30} {:20} {:15} {:10}".format(book["title"], ", ".join(book["authors"]), book["isbn"], book["quantity"]))


def search_books(term):
    results = []
    for book in books:
        if term.lower() in book["title"].lower() or term.lower() in book["isbn"].lower():
            results.append(book)
    return results


def search_by_author(term):
    results = []
    for book in books:
        for author in book["authors"]:
            if term.lower() in author.lower():
                results.append(book)
                break  # Stop searching authors once a match is found for the book
    return results


def remove_book():
    term = input("Enter book title or ISBN to remove: ")
    found_books = search_books(term)
    if not found_books:
        print("Book not found!")
        return

# Let user choose the book to remove
    for i, book in enumerate(found_books):
        print(f"{i+1}. {book['title']}")
    choice = int(input("Enter the number to remove: ")) - 1

    if 0 <= choice < len(found_books):
        books.pop(choice)
        save_data(books)
        print("Book removed successfully!")
    else:
        print("Invalid choice!")


def lend_book():
    term = input("Enter book title or ISBN to lend: ")
    found_books = search_books(term)
    if not found_books:
        print("Book not found!")
        return

# Let user choose the book to lend
    for i, book in enumerate(found_books):
        print(f"{i+1}. {book['title']}")
    choice = int(input("Enter the number to lend: ")) - 1

    if 0 <= choice < len(found_books):
        book = found_books[choice]
        if book["quantity"] == 0:
            print("Sorry, no more books available to lend!")
            return
        book["quantity"] -= 1
        borrower_name = input("Enter borrower name: ")
        book["lent"].append({"borrower": borrower_name})
        save_data(books)
        print("Book lent successfully!")
    else:
        print("Invalid choice!")


def view_lent_books():
    if not books:
        print("No books found!")
        return

    print("{:30} {:20}".format("Title", "Borrower"))
    for book in books:
        for lent in book["lent"]:
            print("{:30} {:20}".format(book["title"], lent["borrower"]))


def return_book():
    term = input("Enter book title or ISBN to return: ")
    found_books = search_books(term)
    if not found_books:
        print("Book not found!")
        return

