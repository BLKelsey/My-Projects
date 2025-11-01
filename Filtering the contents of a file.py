def filter_solutions():
    with (
        open("solutions.csv", "r", encoding="utf-8") as infile,
        open("correct.csv", "w", encoding="utf-8") as correct_file,
        open("incorrect.csv", "w", encoding="utf-8") as incorrect_file
    ):
        for line in infile:
            line = line.strip()
            if not line:
                continue

            parts = line.split(";")
            if len(parts) != 3:
                continue

            name = parts[0]
            problem = parts[1]
            result = int(parts[2])

            # calculate the correct result
            if "+" in problem:
                left, right = problem.split("+")
                correct_result = int(left) + int(right)
            elif "-" in problem:
                left, right = problem.split("-")
                correct_result = int(left) - int(right)
            else:
                continue  # skip if operation is unknown

            output_line = f"{name};{problem};{result}\n"

            # write into correct.csv or incorrect.csv
            if result == correct_result:
                correct_file.write(output_line)
            else:
                incorrect_file.write(output_line)

if __name__ == "__main__":
    filter_solutions()
    print("Done! Results written to correct.csv and incorrect.csv")
