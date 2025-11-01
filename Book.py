  # Please write a class named Book with the attributes name, author, genre and year, along with a constructor which assigns initial values to these attributes.

class Book:
     def __init__(self, name, author, genre, year):
         self.name = name
         self.author = author
         self.genre = genre
         self.year = year


 # Create two Book objects
python = Book('Fluent Python', 'Luciano Ramalho', 'programming', 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

# Print details about the books
print()
print(f"{python.author}: {python.name} ({python.year})")
print(f"The genre of the book {everest.name} is {everest.genre}")


