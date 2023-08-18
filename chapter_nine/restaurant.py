class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine, flavors):
        super().__init__(name, cuisine)
        self.flavors = flavors

    def get_flavors(self):
        print(f"The flavors are {self.flavors}")