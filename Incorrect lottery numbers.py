def filter_incorrect():
    with open("lottery_numbers.csv", "r", encoding="utf-8") as lottery, \
         open("incorrect_numbers.csv", "w", encoding="utf-8") as incorrect, \
         open("correct_numbers.csv", "w", encoding="utf-8") as correct:

        for line in lottery:
            parts = [p.strip() for p in line.strip().split(",")]

            if not parts or not parts[0].lower().startswith("week"):
                incorrect.write(line)
                continue

            numbers = parts[1:]

            # ✅ Expect exactly 7 numbers now
            if len(numbers) != 7:
                incorrect.write(line)
                continue

            valid = True
            for n in numbers:
                try:
                    num = int(n)
                except ValueError:
                    valid = False
                    break

                if num < 1 or num > 39:
                    valid = False
                    break

            if valid:
                correct.write(line)
            else:
                incorrect.write(line)
