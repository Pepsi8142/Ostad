from add_book import add_book

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
        exit(0)
    case '1':
        # title = input('Title: ')
        # isbn = input('ISBN: ')
        year = input('Year: ')
        price = input('Price: $')
        quantity = input('Quantity: ')
        
        authors = []

        # ...

        info = {
            # 'title': title,
            # 'isbn': isbn,
            'year': year,
            'price': price,
            'quantity': quantity
        }
        
        try:
            add_book(info)
        except Exception as e:
            print(e)
