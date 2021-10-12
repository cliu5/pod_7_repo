class Booklist():
    def __init__(self):
        self.books = []

    def add(self, title, author):
        book = {}
        book['title'] = title
        book['author'] = author
        self.books.append(book)

    def count_books(self):
        return len(self.books)

    def remove_title(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)

    def display_titles(self):
        results = []
        sorted_list = sorted(self.books, key=lambda x: x['title'])
        for dict in sorted_list:
            results.append(dict['title'])
        return results
