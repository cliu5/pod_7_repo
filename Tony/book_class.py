class Booklist():
	def __init__(self):
		self.books=[]


	def add(self, title, author):
		self.books.append({"title" : title,
			"author" : author})


	def count_books(self):
			return len(self.books)

	
	def remove_title(self, title):
		book_list = []
		for book in self.books:
			if book['title'] != title:
				book_list.append(book)
			self.books = book_list



	def display_titles(self):
		book_titles = []
		for book in self.books:
			book_titles.append(book['title'])
		print(sorted(book_titles))




