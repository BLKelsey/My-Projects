# Define a class called Book to represent a book object
class Book:
    # Constructor method: runs when a new Book is created
    def __init__(self, name, author, genre, year):
        self.name = name          # store the book's name
        self.author = author      # store the book's author
        self.genre = genre        # store the book's genre (e.g. crime, programming)
        self.year = year          # store the year the book was published

# Function to filter books by a specific genre
def books_of_genre(books: list, genre: str):
    result = []                          # empty list to store matching books
    for book in books:                   # loop through all books in the list
        if book.genre == genre:          # check if this book's genre matches
            result.append(book)          # if yes, add it to the result list
    return result                        # return the list of matching books

# Create Book objects
python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

# Put all the Book objects into a list
books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

print()   # just prints a blank line for spacing
print("Books in the crime genre:")

# Loop through the result of books_of_genre and print each match
for book in books_of_genre(books, "crime"):
    print(f"{book.author}: {book.name}")   # print author and book title




