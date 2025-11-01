
class Book:
    def __init__(self,name,year):
        self.name = name
        self.year = year

def older_book(book1, book2):
    if book1.year < book2.year:
        print(book1.name + " is older, it was published in " + str(book1.year))
    elif book2.year < book1.year:
        print(book2.name + " is older:  published in " + str(book2.year))
    else:
        print(book1.name + " and " + book2.name + " were both published in " + str(book1.year))

python = Book("Fluent Python", 2015)
everest = Book("High Adventure", 1956)
norma = Book("Norma", 2015)

print()
older_book(python, everest)
older_book(python, norma)