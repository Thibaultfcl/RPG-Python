import random
class Weapon:
    def __init__(self, name, damage, value):
        self.name = name
        self.damage = damage
        self.value = value

sword = Weapon("Sword", 15, 100)
axe = Weapon("Axe", 20, 150)
dager = Weapon("Dager", 10, 50)
fist = Weapon("Fist", 4, 0)

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

class Items:
    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description
    
    def add (self, hero):
        hero.inventory.append(self)
        print(f"{hero.name} picked up a {self.name}.")
        input("Press any key to continue...")
        return

class HealthPotion(Items):
    def __init__(self):
        super().__init__("Health Potion", 50, "Heals 50 HP")
    
    def use(self, hero):
        hero.health += self.value
        hero.health = min(hero.health, hero.health_max)
        print(f"{hero.name} used a Health Potion and restored 50 HP.")
        input("Press any key to continue...")
        return

class Bomb(Items):
    def __init__(self):
        super().__init__("Bomb", 50, "Deals 50 damage to the enemy")
    
    def use(self, enemy):
        enemy.health -= self.value
        enemy.health = max(enemy.health, 0)
        enemy.health_bar.update()
        enemy.health_bar.draw()
        print(f"{enemy.name} took 50 damage from the bomb.")
        input("Press any key to continue...")
        return