dell = ["Akintola Mathew", "54 Akintola Street, Lagos", "Python", 24]
uche = ["Uche", "54 Uche Street, Lagos", "Python", 23]
sandra = ["Sandra", "54 Sandra Street, Lagos", 23]

class Person:
    breath = True
    def __init__(self, full_name, full_address, full_language) -> None:
        self.name = full_name
        self.address = full_address
        self.language = full_language
    
    def __str__(self):
        return f"name: {self.name}, address: {self.address}, langage: {self.language}"

    def speak(self):
        return f"{self.name}, speaks {self.language}"


dell = Person("Akintola Mathew", "54 Akintola Street, Lagos", "Python")
uche = Person("Uche", "54 Uche Street, Lagos", "Python")
sandra = Person("Sandra", "54 Sandra Street, Lagos", 23)

print(dell)
print("dunder methods")
