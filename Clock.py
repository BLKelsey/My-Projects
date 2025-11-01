class Stopwatch:
    def __init__(self):               # constructor to set starting time
        self.hours = 0                # start with 0 hours
        self.minutes = 0              # start with 0 minutes
        self.seconds = 0              # start with 0 seconds

class Clock:
    # This defines a Clock class, which will keep track of hours, minutes, and seconds.

    def __init__(self, hours, minutes, seconds):
        # The constructor initializes a new Clock object with given hours, minutes, and seconds
        self.hours = hours        # set the starting hours
        self.minutes = minutes    # set the starting minutes
        self.seconds = seconds    # set the starting seconds


    def tick(self):
        # This method moves the clock forward by one second
        self.seconds += 1                      # add 1 to second
        if self.seconds == 60:                 # if seconds reach 60
          self.seconds = 0                     # reset seconds to 0
          self.minutes += 1                    # increase minutes by 1
        if self.minutes == 60:                 # if minutes reach 60
            self.minutes = 0                   # reset minutes to 0
            self.hours += 1                    # increase hours by 1
        if self.hours == 24:                   # if hours reach 24
            self.hours = 0                     # reset hours back to 0 (start a new day)
            # self.minutes += 1                # ❌ not needed, would incorrectly add extra minutes

    def set(self, new_hours, new_minutes):
        # This method sets the clock to a new time
        self.hours = new_hours                 # change the clock's hour value
        self.minutes = new_minutes             # change the clock's minute value
        self.seconds = 0                       # reset seconds back to 0 when setting new time

    def to_string(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hours,self.minutes, self.seconds)

clock = Clock(23,59,55)
print (clock.to_string())
clock.tick()
print (clock.to_string())
clock.tick()
print (clock.to_string())
clock.tick()
print (clock.to_string())
clock.tick()
print (clock.to_string())
clock.tick()
print (clock.to_string())
clock.tick()
print (clock.to_string())
clock.tick()
clock.set(12,5)
print (clock.to_string())

