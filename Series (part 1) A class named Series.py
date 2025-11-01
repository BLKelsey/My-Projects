class Series:
    def __init__(self, title, seasons, genres):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []   # start empty, no ratings yet

    def __str__(self):
        # Join genres list into one string with commas
        genre_string = ", ".join(self.genres)

        # If no ratings exist, show "no ratings"
        if not self.ratings:
            ratings_info = "no ratings"
        else:
            ratings_info = f"ratings: {self.ratings}"

        # Build final string with line breaks
        return f"{self.title} ({self.seasons} seasons)\n" \
               f"genres: {genre_string}\n" \
               f"{ratings_info}"

dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
print(dexter)
genre_list = ["Crime", "Drama", "Mystery", "Thriller"]
genre_string = ", ".join(genre_list)
print(genre_string)
