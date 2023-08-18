class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")

dog = Dog('porter', 8)
dog.sit()