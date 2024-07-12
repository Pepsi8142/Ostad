import re

def add_book(info):
    # if len(info.isbn) !== 10:
    #     raise Exception('Incorrect ISBN value!')

    if re.search('^(19[7-9]|2[01][0-2])[0-9]$', info['year']) is None:
        raise Exception('Invalid year!')
    
    if re.search('^\d{1,3}(\.\d{2})?$', info['price']) is None:
        raise Exception('Invalid price!')
    
    if re.search('^[1-9]\d{0,2}$', info['quantity']) is None:
        raise Exception('Invalid quantity!')

    pass
