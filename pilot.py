import datetime

class Pilot:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.times = {}
        self.speeds = {}
        self.total_time = datetime.timedelta()
        self.total_distance = 0.0
        self.completed_laps = 0
        self.better_time = None
        self.better_lap = None

    def add_lap(self, lap, time, speed):
        (m, s) = time.split(':')
        converted_time = datetime.timedelta(minutes=int(m), seconds=float(s))
        self.total_time += converted_time
        self.total_distance += float(speed.replace(",", ".")) * converted_time.total_seconds()
        self.times[lap] = time
        if (self.completed_laps < int(lap)):
            self.completed_laps = int(lap)
        if (not self.better_time or self.better_time.total_seconds() > converted_time.total_seconds()):
            self.better_time = converted_time
            self.better_lap = lap

    def get_time_after(self, time):
        if (self.completed_laps < 4):
            return "-"

        return str(datetime.timedelta(seconds=(self.total_time.total_seconds() - time.total_seconds())))

    def get_average_speed(self):
        return self.total_distance/self.total_time.total_seconds()

    def __cmp__(self, other):
        if self.completed_laps != other.completed_laps:
            # The more laps the better
            return other.completed_laps - self.completed_laps

        return self.total_time.total_seconds() - other.total_time.total_seconds()

    def __str__(self):
        return ",".join([self.code, self.name, str(self.completed_laps), str(self.total_time)])
