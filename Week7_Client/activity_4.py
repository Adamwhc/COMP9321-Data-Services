import requests


def print_book(book):
    print("Book {")
    for key in book.keys():
        attr = str(key)
        if isinstance(book[key], unicode):
            val = str(book[key].encode('utf-8'))
        else:
            val = str(book[key])

        print("\t" + attr + ":" + val)
    print("}")


def get_book(id):
    r = requests.get("http://127.0.0.1:5000/books/" + str(id))
    book = r.json()
    print("Get status Code:" + str(r.status_code))
    if r.ok:
        print_book(book)
        return book
    else:
        print('Error:' + book['message'])


def remove_book(id):
    pass


if __name__ == '__main__':

    print("***** Book information before update *****")
    book = get_book(206)

    # update the book information
    print("***** Deleting Book *****")
    r = requests.delete("http://127.0.0.1:5000/books/206")
    print("Delete status Code:" + str(r.status_code))
    print(r.json()['message'])

    print("***** Book information after Delete *****")
    book = get_book(206)

