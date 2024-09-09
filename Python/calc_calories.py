class CalcCalories:
    def __init__(self, power, time_seconds):
        if not isinstance(power, int) or not isinstance(time_seconds, int):
            raise TypeError("Los valores deben ser números enteros")
        
        self.power = power
        self.time_seconds = time_seconds

    def calculate_calories(self):
        if self.power <= 0 or self.time_seconds <= 0:
            raise ValueError("Hubo un error en la medición")
        
        calories = round((self.power * self.time_seconds) / 4.184)
        return calories
