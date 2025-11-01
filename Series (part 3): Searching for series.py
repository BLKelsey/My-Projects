class Series:
    def __init__(self, title, seasons, genres):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def rate(self, rating):
        if 0 <= rating <= 5:
            self.ratings.append(rating)

    def __str__(self):
        genre_string = ", ".join(self.genres)
        result = f"{self.title} ({self.seasons} seasons)\n"
        result += f"genres: {genre_string}\n"
        if len(self.ratings) == 0:
            result += "no ratings"
        else:
            count = len(self.ratings)
            average = sum(self.ratings) / count
            result += f"{count} ratings, average {average:.1f} points"
        return result

    # @property decorator in Python lets you define a method that can be accessed like an attribute — without needing parentheses ().
    @property
    def rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

# --- Now these are correctly OUTSIDE the class ---
def minimum_grade(min_rating, series_list):
    result = []
    for series in series_list:
        if series.rating >= min_rating:
            result.append(series)
    return result

def includes_genre(genre, series_list):
    result = []
    for series in series_list:
        if genre in series.genres:
            result.append(series)
    return result

# Main Program
# --- Creating Series instances ---
s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

# --- Using the functions ---
print()
print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("\ngenre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)