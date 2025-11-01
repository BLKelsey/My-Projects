def cheaters():

    # 1. Read start times
    start_times = {}
    with open("start_times.csv", "r") as file:
        for line in file:
            part = line.strip().split(";")
            name = part[0]
            time = part[1]  # format hh:mm
            start_times[name] = time

    # 2. Read submissions
    cheater_list = {}
    with open("submissions.csv", "r") as file:
        for line in file:
            part = line.strip().split(";")
            name = part[0]
            task = part[1]
            points = part[2]
            hour = part[3]
            minute = part[4]

            # Build submission time string like "16:05"
            submission_time = hour.zfill(2) + ":" + minute.zfill(2)

            # Skip if student not in start_times
            if name not in start_times:
                print("Warning: No start time for", name)
                continue

            start_time = start_times[name]

            # Convert both times to total minutes
            start_hour, start_minute = start_time.split(":")
            sub_hour, sub_minute = submission_time.split(":")

            start_total = int(start_hour) * 60 + int(start_minute)
            sub_total = int(sub_hour) * 60 + int(sub_minute)

            time_difference = sub_total - start_total

            # If more than 3 hours late
            if time_difference > 180:
                if name not in cheater_list:
                    cheater_list[name] = []
                cheater_list[name].append(task)

    return cheater_list


# Example usage
result = cheaters()
print(result)
