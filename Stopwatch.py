class Stopwatch:
    def __init__(self):               # constructor to set starting time
        self.seconds = 0              # start with 0 seconds
        self.minutes = 0              # start with 0 minutes

    def tick(self):                   # method to move time forward by 1 second
        self.seconds += 1             # add 1 second
        if self.seconds == 60:        # if 60 seconds have passed
            self.seconds = 0          # reset seconds back to 0
            self.minutes += 1         # increase minutes by 1
        if self.minutes == 60:        # if 60 minutes have passed
            self.minutes = 0          # reset minutes back to 0 (start over)

    def to_string(self):              # method to display stopwatch time
        return "{:02d}:{:02d}".format(self.minutes, self.seconds)
        # format ensures "00:00" style with 2 digits each

watch = Stopwatch()                   # create a new stopwatch starting at 00:00

for i in range(3602):                 # run for 3602 ticks (a little over 1 hour)
    # print the first few times
    if i < 3:
        print(watch.to_string())

    # print just before and after 1 minute
    elif i in (59, 60, 61):
        print(watch.to_string())

    # print just before and after 1 hour
    elif i in (3598, 3599, 3601):     # show 59:58, 59:59, and 01:00
        print(watch.to_string())

    # print after rollover back to 00:00 and 00:01
    elif i in (3600, 3601):           # show when it resets
        print(watch.to_string())

    # placeholder for skipped lines after 3rd tick
    elif i == 3:
        print("... many more lines printed out")
    # placeholder for skipped lines after 1 minute
    elif i == 62:
        print("... many, many more lines printed out")

    watch.tick()                      # advance stopwatch by 1 second
