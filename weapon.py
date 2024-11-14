import random
class Weapon:
    def __init__(self, name, damage, value):
        self.name = name
        self.damage = damage
        self.value = value

sword = Weapon("Sword", 15, 100)
axe = Weapon("Axe", 20, 150)
dager = Weapon("Dager", 10, 50)
fist = Weapon("Fist", 5, 0)

weapons = [sword, axe, dager, fist]

class Chest:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.weapon = random.choice(weapons)

    def __repr__(self):
        return f"Chest({self.x}, {self.y}, {self.weapon})"

    def open(self, hero):
        print(f"{hero.name} found {self.weapon.name} in the chest.")
        hero.equip(self.weapon)
        input("Press any key to continue...")
        return
    
    def remove(self):
        self.x = 1000
        self.y = 1000