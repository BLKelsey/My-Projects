class Series:
    def __init__(self, title, seasons, genres):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []   # start with empty ratings list

    def rate(self, rating):
        if 0 <= rating <= 5:   # only accept valid ratings
            self.ratings.append(rating)

    def __str__(self):
        # join genres into one string
        genre_string = ", ".join(self.genres)

        # start the output with title and seasons
        result = f"{self.title} ({self.seasons} seasons)\n"
        result += f"genres: {genre_string}\n"

        # check if ratings exist
        if len(self.ratings) == 0:
            result += "no ratings"
        else:
            count = len(self.ratings)
            average = sum(self.ratings) / count
            result += f"{count} ratings, average {average:.1f} points"
        return result

# Main Program
dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print()
print(dexter)
