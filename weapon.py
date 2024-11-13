class Weapon:
    def __init__(self, name, damage, value):
        self.name = name
        self.damage = damage
        self.value = value

sword = Weapon("Sword", 15, 100)
axe = Weapon("Axe", 20, 150)
dager = Weapon("Dager", 10, 50)
fist = Weapon("Fist", 5, 0)