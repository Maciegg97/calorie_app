


class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * float(self.weight) + 6.5 * float(self.height) + 5 - self.temperature * 10
        return result
