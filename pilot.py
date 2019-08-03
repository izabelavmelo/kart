import datetime

class Pilot:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.times = {}
        self.total_time = datetime.timedelta()
        self.completed_laps = 0

    def add_time(self, lap, time):
        (m, s) = time.split(':')
        converted_time = datetime.timedelta(minutes=int(m), seconds=float(s))
        self.total_time += converted_time
        self.times[lap] = time
        if (self.completed_laps < int(lap)):
            self.completed_laps = int(lap)

    def __cmp__(self, other):
        if self.completed_laps != other.completed_laps:
            # The more laps the better
            return other.completed_laps - self.completed_laps

        return self.total_time.total_seconds() - other.total_time.total_seconds()

    def __str__(self):
        return ",".join([self.code, self.name, str(self.completed_laps), str(self.total_time)])
