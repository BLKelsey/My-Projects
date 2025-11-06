def sort_by_ratings(items: list):
    sorted_list = sorted(items, key=lambda item: item['rating'])
    return sorted_list

shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]
print()
print("Rating according to IMDB:")
for show in sort_by_ratings(shows):
    print(f"{show['name']}  {show['rating']}")