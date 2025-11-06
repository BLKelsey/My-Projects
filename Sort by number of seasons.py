def sort_by_seasons(items: list):

    # create a new list sorted by each show's 'seasons' value in ascending order
    #key=lambda item: item['seasons'] — tells Python how to sort: look inside each dictionary (item)
    # and use the 'seasons' value as the sorting key.
    sorted_list = sorted(items, key=lambda item: item['seasons'])
    return sorted_list

shows = [{"name": "Dexter", "rating": 8.6, "seasons": 9}, {"name": "Friends", "rating": 8.9, "seasons": 10},
             {"name": "Simpsons", "rating": 8.7, "seasons": 32}]
print()
for show in sort_by_seasons(shows):
    print(f"{show['name']} {show['seasons']} seasons")



