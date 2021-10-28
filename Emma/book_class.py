class Booklist():
    def __init__(self):
        self.booklist = []

    def add_booklist(self, title, author, books):
        self.title = title
        self.author = author
        self.books = books
        {title}, {author}.append(title, author)

    def count_books(self):
        return len(self.books)

    def remove_title(self, title):
        for books in self.books:
            if books["title"] == title:
                self.books.remove(books)

    def display_titles(self):
        for books in self.books:
            if books == True:
                self.books.sort(books)

    def nyt_bestsellers(self, Booklist):
        self.nyt_bestsellers = Booklist
