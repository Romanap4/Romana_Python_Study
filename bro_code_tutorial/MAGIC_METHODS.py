# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # STRING -> return a string representation of the object when we print it directly to the console
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # EQUALS -> compare if two objects are equal
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # LESS THAN
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    # GREATER THAN
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    # ADDITION
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    # CONTAINS
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    # GET ITEM
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found."

book1 = Book("Sherlock Holmes", "Sir Arthur Conan Doyle", 1796)
book2 = Book("Frankenstein", "Mary Shelley", 352)
book3 = Book("1984", "George Orwell", 336)
book4 = Book("Sherlock Holmes", "Sir Arthur Conan Doyle", 1257)

print(book1)
print(book2)
print(book3)

print(book1 == book4)
print(book3 < book1)
print(book1 > book2)
print(book2 + book3)
print("Holmes" in book1)
print("Mary" in book2)
print(book1['title'])
print(book2['author'])
print(book3['num_pages'])
print(book3['num_pages'])
print(book4['audio'])
