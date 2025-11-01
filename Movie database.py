# Please write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int), which adds a new movie object into a movie database.

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    new_movie = {                   # Create a dictionary called 'movie'
        "name": name,               # Create key/value pairs
        "director": director,
        "year": year,
        "runtime": runtime
    }
    database.append(new_movie)     # Add this dictionary to the 'database' list
                                   # This grows the list by one entry each time you call add_movie()

def find_movies(database: list, search_term: str) -> list:
    term = search_term.lower()             # Convert the search term to lowercase once (for case-insensitive search)

    results = [movie for movie in database if term in movie["name"].lower()]    # Use a list comprehension to filter movies

    return results


if __name__ == "__main__":
    db = []
    print()
    add_movie(db, "The Lion and Wardrobe", "Andrew Adamson", 2005, 150)
    add_movie(db, "The Matrix", "Lana Wachowski and Lilly Wachowski", 1999, 136)
    add_movie(db, "The Matrix Reloaded", "Lana Wachowski and Lilly Wachowski", 2003, 138)
    add_movie(db, "F1", "Joseph Kosinski", 2025, 155)
    add_movie(db, "Chitty Chitty Bang Bang", "Ken Hughes", 1968, 144)

    print("All movies in database:")
    print()
    for movie in db:
        print(movie)

    # Search
    print()
    print("Search results for 'Mat':")
    results = find_movies(db, "Mat")

    for movie in results:
        print(movie)










