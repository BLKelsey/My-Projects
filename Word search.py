def find_words(search_term: str):
    results = []
    term = search_term.lower()   # work in lowercase for safety

    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                w = word.strip().lower()   # clean + lowercase

                # Case 1: search term starts with "*" → endswith
                if term.startswith("*"):
                    part = term[1:]
                    if w.endswith(part):
                        results.append(word)

                # Case 2: search term ends with "*" → startswith
                elif term.endswith("*"):
                    part = term[:-1]
                    if w.startswith(part):
                        results.append(word)

                # Case 3: no * → contains
                else:
                    if term in w:
                        results.append(word)
    return results

# ✅ Function call
if __name__ == "__main__":
    print()
    search_term = input("Search term: ")
    print()
    matches = find_words(search_term)
    print('Matches: ')
    print(matches)
