def filter_solutions():
    with (
        open("solutions.csv", "r", encoding="utf-8") as infile,
        open("correct.csv", "w", encoding="utf-8") as correct_file,
        open("incorrect.csv", "w", encoding="utf-8") as incorrect_file
    ):
        for line in infile:
            print("RAW:", repr(line))   # debug

            line = line.strip()
            if not line:
                continue

            parts = line.split(";")
            print("SPLIT:", parts)      # debug

            name = parts[0]
            problem = parts[1]
            student_result = int(parts[2])

            if "+" in problem:
                left, right = problem.split("+")
                correct_result = int(left) + int(right)
            else:
                left, right = problem.split("-")
                correct_result = int(left) - int(right)

            print(f"CHECK: {name} {problem} → {correct_result}, student wrote {student_result}")

            if student_result == correct_result:
                print("→ writing to correct.csv")
                correct_file.write(line + "\n")
            else:
                print("→ writing to incorrect.csv")
                incorrect_file.write(line + "\n")


if __name__ == "__main__":
    filter_solutions()
