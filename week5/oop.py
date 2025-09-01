# Q1 Inheritance example
# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I have the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass with inheritance
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h using {self.power}!")

# Another subclass
class StrengthHero(Superhero):
    def __init__(self, name, power, origin, strength_level):
        super().__init__(name, power, origin)
        self.strength_level = strength_level

    def use_power(self):
        print(f"{self.name} lifts {self.strength_level} tons with {self.power}!")

# Create objects
hero1 = FlyingHero("SkyBolt", "Wind Blast", "Cloud City", 800)
hero2 = StrengthHero("Titan", "Mega Punch", "Earth Core", 100)

# Use methods
hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()


# Q2 Polymorphism example
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat()]

# Loop through and call move()
for v in vehicles:
    v.move()
