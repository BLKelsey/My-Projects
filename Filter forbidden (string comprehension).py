def filter_forbidden(string: str, forbidden: str):
    new_string = "".join(ch for ch in string if ch not in forbidden)    # build a new string excluding any characters found in 'forbidden'
    return new_string   # return the filtered string

sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print()
print(filtered)