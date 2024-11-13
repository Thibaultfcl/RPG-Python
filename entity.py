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
    
    def move(self, dx, dy, enemies, map) -> None:
        min_x = min(room.x for room in map.rooms.values())
        max_x = max(room.x for room in map.rooms.values())
        min_y = min(room.y for room in map.rooms.values())
        max_y = max(room.y for room in map.rooms.values())
        if self.x + dx < min_x or self.x + dx > max_x or self.y + dy < min_y or self.y + dy > max_y:
            self.x += dx
            self.y += dy
        print(f"{self.name} moved to ({self.x}, {self.y})")
        for enemy in enemies:
            if self.x == enemy.x and self.y == enemy.y:
                self.attack(enemy)
                break

class Ennemy(Entity):
    def __init__(self, name, health, x, y, weapon) -> None:
        super().__init__(name, health, x, y)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color="red")