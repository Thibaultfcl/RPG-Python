import os
import time
from weapon import *
from health_bar import HealthBar

class Entity:
    def __init__(self, name, health, x, y) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.x = x
        self.y = y
        self.weapon = fist

class Hero(Entity):
    def __init__(self, name, health, x, y) -> None:
        super().__init__(name, health, x, y)
        self.health_bar = HealthBar(self, color="green")
        self.inventory = []
    
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped {self.weapon.name}")
    
    def display_inventory(self) -> None:
        os.system('cls')
        print("=== INVENTORY ===")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Weapon: {self.weapon.name}")
        for item in self.inventory:
            print(f"Item: {item.name}")
        input("Press any key to continue...")
    
    def attack(self, other) -> None:
        print(f"{self.name} just found {other.name}")
        input("Press any key to continue...")
        
        while self.health > 0 and other.health > 0:
            os.system('cls')
            action = input(f"Press 'a' to attack {other.name} or 'i' to use an item: ")
            if action == 'a':
                other.health -= self.weapon.damage
                other.health = max(other.health, 0)
                other.health_bar.update()
                other.health_bar.draw()
                print(f"{self.name} dealt {self.weapon.damage} damage to {other.name}")
                
                if other.health <= 0:
                    print(f"{other.name} has been defeated!")
                    potion = HealthPotion()
                    bomb = Bomb()
                    random_item = random.choice([potion, bomb])
                    random_item.add(self)
                    continue
                
                time.sleep(1)
                
                self.health -= other.weapon.damage
                self.health = max(self.health, 0)
                self.health_bar.update()
                self.health_bar.draw()
                print(f"{other.name} counterattacked and dealt {other.weapon.damage} damage to {self.name}")
                
                if self.health <= 0:
                    print(f"{self.name} has been defeated!")
                
            elif action == 'i':
                print("=== INVENTORY ===")
                for idx, item in enumerate(self.inventory):
                    print(f"{idx + 1}. {item.name} - {item.description}")
                item_choice = input("Choose an item to use (number): ")
                try:
                    item_index = int(item_choice) - 1
                    if 0 <= item_index < len(self.inventory):
                        item = self.inventory[item_index]
                        if isinstance(item, HealthPotion):
                            item.use(self)
                        elif isinstance(item, Bomb):
                            item.use(other)
                        self.inventory.pop(item_index)
                    else:
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number.")
                
                if other.health <= 0:
                    print(f"{other.name} has been defeated!")
                    potion = HealthPotion()
                    bomb = Bomb()
                    random_item = random.choice([potion, bomb])
                    random_item.add(self)
                    continue
                
                time.sleep(1)
                
                self.health -= other.weapon.damage
                self.health = max(self.health, 0)
                self.health_bar.update()
                self.health_bar.draw()
                print(f"{other.name} counterattacked and dealt {other.weapon.damage} damage to {self.name}")
                
                if self.health <= 0:
                    print(f"{self.name} has been defeated!")
            else:
                print("Invalid action. Please press 'a' to attack or 'i' to use an item.")
            
            input("Press any key to continue...")
            os.system('cls')
    
    def move(self, dx, dy, enemies, map, chests) -> None:
        min_x = min(room.x for room in map.rooms.values())
        max_x = max(room.x for room in map.rooms.values())
        min_y = min(room.y for room in map.rooms.values())
        max_y = max(room.y for room in map.rooms.values())
        if min_x <= self.x + dx <= max_x and min_y <= self.y + dy <= max_y:
            self.x += dx
            self.y += dy
            print(f"{self.name} moved to ({self.x}, {self.y})")
            for enemy in enemies:
                if self.x == enemy.x and self.y == enemy.y:
                    self.attack(enemy)
                    break
            for chest in chests:
                if self.x == chest.x and self.y == chest.y:
                    chest.open(self)
                    chests.remove(chest)
                    break
        else:
            print("INVALID MOVE")

class Ennemy(Entity):
    def __init__(self, name, health, x, y, weapon) -> None:
        super().__init__(name, health, x, y)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color="red")