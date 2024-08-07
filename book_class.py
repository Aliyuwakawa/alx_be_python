class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year =  year

    def __str__(self):
        return "{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        print(f"Deleting {self.title}")


book = Book("1984", "George Orwell", 1949)
print(book)
