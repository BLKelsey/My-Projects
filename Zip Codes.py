class City:
    # class variable shared by all City objects as a dictionary
    zipcodes = {
        "Helsinki": "00100",
        "Turku": "20100",
        "Tampere": "33100",
        "Rovaniemi": "96100",
        "Oulu": "90100"
    }

# --- Main Program ---
print()
print(City.zipcodes)              # show the whole dictionary
print("Helsinki's zip code: ",City.zipcodes["Helsinki"])  # access Helsinki’s postcode
print("Oulu's zip code: ",City.zipcodes["Oulu"])      # access Oulu’s postcode
