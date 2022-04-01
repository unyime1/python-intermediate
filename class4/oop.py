class Person:
    breath = True
    def __init__(self, full_name, full_address, full_language) -> None:
        self.name = full_name
        self.address = full_address
        self.language = full_language
    
    def __str__(self):
        return f"name: {self.name}, address: {self.address}, langage: {self.language}"
    
    def speak(self, sound):
        return f"{self.name} speaks {sound}"

    def laugh(self):
        return f"{self.name} laughs hahaha"


class Student(Person):
    def sing(self):
        return f"{self.name} sings {self.language}"
    
    def speak_child(self, sound="English"):
        return super().speak(sound)
    
    def laugh_child(self):
        return super().laugh()


uche = Student("Uche", "test address", "python")
print(uche.speak_child())
print(uche.laugh_child())