from calc_speed import CalcSpeed

class CalcDistance:
    def __init__(self, rpm, time_seconds):        
        self.speed = CalcSpeed(rpm, time_seconds).calculate_speed()
        self.time_seconds = time_seconds
        self._distance = None

    def calculate_distance(self):
        self._distance = round((self.speed * self.time_seconds)/3.6)
        return self._distance

    def get_distance(self):
        return self._distance


