class CalcSpeed:
    def __init__(self, rpm, time_seconds):
        if not isinstance(rpm, int) or not isinstance(time_seconds, int):
            raise TypeError("Los valores deben ser números enteros")
        
        if rpm <= 0 or time_seconds <= 0:
            raise ValueError("Los valores deben ser números positivos")
        
        self.rpm = rpm
        self.time_seconds = time_seconds

    def calculate_speed(self):
        speed = round(((self.rpm * 60) / self.time_seconds))
        return speed

    def get_speed(self):
        return self.calculate_speed()
