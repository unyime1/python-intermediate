class Car:
    def __init__(self, color, model, engine_type, tires, seats, year) -> None:
        self.color = color
        self.model = model
        self.engine_type = engine_type
        self.tires = tires
        self.seats = seats
        self.year = year
    
    def __str__(self) -> str:
        return f"{self.model} is a nice car!"
    
    def year_plus(self, number: int) -> str:
        return f"{self.year + number}"

honda = Car("red", "honda", "trdes", 4, 4, 2019)
volvo = Car("black", "volvo", "34re", 4, 4, 2017)

print(honda.year_plus(5), volvo.year_plus(9))
