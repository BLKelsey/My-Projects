def smallest_average(person1: dict, person2: dict, person3: dict):

    # 1. Calculate averages for each person
    average1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    average2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    average3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3

    # 2. Compare averages
    if average1 > average2:
        smallest_average = average2
        return person2
    elif average2 > average3:
        smallest_average = average3
        return person3
    elif average3 > average1:
        smallest_average = average1
        return person1
    elif average1 > average3:
        smallest_average = average3
        return person3

# 3. Defne each person as a dictionary enty
person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# 4. Function call
winner = smallest_average(person1, person2, person3)
print(winner)



