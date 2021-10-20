class Booklist():
	def __init__(self):
		self.books = []

	def add(self, title, author):
		book = {'title': title, 			'author': author}
		self.books.append(book)

	def count_books(self):
		return(len(self.books))

	def remove_title(self, title):
		for book in self.books:
			if book['title'] == title:
				self.books.remove(book)

