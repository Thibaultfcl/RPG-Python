from weapon import fist
from health_bar import HealthBar

class Entity:
    def __init__(self, name, health, x, y) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.x = x
        self.y = y
        self.weapon = fist
    
    def attack(self, other) -> None:
        other.health -= self.weapon.damage
        other.health = max(other.health, 0)
        other.health_bar.update()
        print(f"{self.name} dealt {self.weapon.damage} damage to {other.name}")

class Hero(Entity):
    def __init__(self, name, health, x, y) -> None:
        super().__init__(name, health, x, y)
        self.health_bar = HealthBar(self, color="green")
    
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped {self.weapon.name}")
    
    def move(self, dx, dy) -> None:
        self.x += dx
        self.y += dy
        print(f"{self.name} moved to ({self.x}, {self.y})")

class Ennemy(Entity):
    def __init__(self, name, health, x, y, weapon) -> None:
        super().__init__(name, health, x, y)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color="red")