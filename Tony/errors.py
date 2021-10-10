books = ['To Kill a Mockingbird', 'The Thing', '1984', 'Four Agreements']


print(books)


print(f"Today I read {books[1]}")


print(books[3])


for book in books:
    if book == "1984":
        print(book)
        print("I read that book")


def multiply(a, b):
    print(a * b)

multiply(2, 3)
