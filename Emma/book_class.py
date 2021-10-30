class Booklist():
    def __init__(self):
        self.books = []

    def add(self, title, author):
        self.books.append({'title': title, 'author': author})

    def count_books(self):
        return len(self.books)

    def remove_title(self, title):
        for books in self.books:
            if (books["title"] == title):
                self.books.remove(books)

    def nyt_bestsellers(self, Booklist):
        self.nyt_bestsellers = Booklist

    def display_titles(self):
        alphabetically = sort()
