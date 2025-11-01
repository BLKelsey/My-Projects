def personal_data(person: tuple, header=False):
    with open('people.csv', 'a') as csvfile:           # # open the file in append mode so new entries are added at the end
        if header:   # write header if requested
            csvfile.write("name,age,height\n")

        name = str(person[0])
        age = int(person[1])
        height = float(person[2])
        line = f"{person[0]};{person[1]};{person[2]}\n"           # format the line as name;age;height
        csvfile.write(line)

if __name__ == '__main__':
      # Write header once                                      
      personal_data(("Paul Paulson", 37, 71.5), header=True)   
      personal_data(("Alice Johnson", 25, 165.2))              


