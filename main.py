import time
import os
import json

import keyboard
from map import Map, Room
from entity import Hero, Ennemy
from weapon import *

SAVE_FILE = "savegame.json"

def display_menu() -> str:
    os.system('cls')
    print("=== MENU ===")
    print("1. Start Game")
    print("2. Load Game")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def display_GameOver() -> str:
    os.system('cls')
    print("=== GAME OVER ===")
    print("1. Retry")
    print("2. Exit")
    choice = input("Enter your choice: ")
    return choice

def save_game(hero, enemies, map_instance) -> None:
    game_state = {
        "hero": {
            "name": hero.name,
            "health": hero.health,
            "x": hero.x,
            "y": hero.y,
            "weapon": hero.weapon.name
        },
        "enemies": [
            {
                "name": enemy.name,
                "health": enemy.health,
                "x": enemy.x,
                "y": enemy.y,
                "weapon": enemy.weapon.name
            }
            for enemy in enemies
        ],
        "map": [
            {"x": room.x, "y": room.y, "description": room.description}
            for room in map_instance.rooms.values()
        ]
    }
    with open(SAVE_FILE, 'w') as f:
        json.dump(game_state, f)
    print("Game saved.")

def load_game():
    with open(SAVE_FILE, 'r') as f:
        game_state = json.load(f)
    
    hero = Hero(game_state["hero"]["name"], game_state["hero"]["health"], game_state["hero"]["x"], game_state["hero"]["y"])
    hero.weapon = next(w for w in [sword, axe, dager, fist] if w.name == game_state["hero"]["weapon"])
    
    enemies = []
    for enemy_data in game_state["enemies"]:
        enemy = Ennemy(enemy_data["name"], enemy_data["health"], enemy_data["x"], enemy_data["y"], sword)
        enemy.weapon = next(w for w in [sword, axe, dager, fist] if w.name == enemy_data["weapon"])
        enemies.append(enemy)
    
    map_instance = Map()
    for room_data in game_state["map"]:
        map_instance.add_room(Room(room_data["x"], room_data["y"], room_data["description"]))
    
    return hero, enemies, map_instance

def main() -> None:
    hero, enemies, map_instance = None, None, None
    while True:
        choice = display_menu()
        if choice == '1':
            hero = Hero("Hero", 100, 0, 0)
            enemy = Ennemy("Ennemy", 50, 1, 0, dager)
            chest = Chest(-1, 0)
            chests = [chest]
            enemies = [enemy]
            map_instance = Map()
            map_instance.add_room(Room(0, 0, "Salle de départ"))
            map_instance.add_room(Room(1, 0, "Salle au Nord"))
            map_instance.add_room(Room(0, 1, "Salle gardée par un ennemi"))
            map_instance.add_room(Room(1, 1, "Salle mysterieuse"))
            map_instance.add_room(Room(-1, 0, "Salle du trésor"))
            break
        elif choice == '2':
            try:
                hero, enemies, map_instance = load_game()
                print("Game loaded.")
                break
            except FileNotFoundError:
                print("No saved game found.")
                time.sleep(2)
        elif choice == '3':
            print("Exiting...")
            time.sleep(2)
            return
        else:
            print("Invalid choice, please try again.")
            time.sleep(2)
    
    while True:
        time.sleep(0.5)
        os.system('cls')
        
        if hero.health <= 0:
            choice = display_GameOver()
            if choice == '1':
                hero = Hero("Hero", 100, 0, 0)
                enemy = Ennemy("Ennemy", 50, 1, 0, dager)
                chest = Chest(-1, 0)
                chests = [chest]
                enemies = [enemy]
                map_instance = Map()
                map_instance.add_room(Room(0, 0, "Salle de départ"))
                map_instance.add_room(Room(1, 0, "Salle au Nord"))
                map_instance.add_room(Room(0, 1, "Salle gardée par un ennemi"))
                map_instance.add_room(Room(1, 1, "Salle mysterieuse"))
                map_instance.add_room(Room(-1, 0, "Salle du trésor"))
            elif choice == '2':
                print("Exiting...")
                time.sleep(2)
                break
        
        move = input('Enter direction (z/q/s/d) or , to display map,i to inventory, m to exit: ')
        if move == 'z':
            hero.move(0, 1, enemies, map_instance, chests)
        elif move == 's':
            hero.move(0, -1, enemies, map_instance, chests)
        elif move == 'q':
            hero.move(-1, 0, enemies, map_instance, chests)
        elif move == 'd':
            hero.move(1, 0, enemies, map_instance, chests)
        elif move == ',':
            map_instance.display(hero, enemies, chests)
        elif move == 'i':
            hero.display_inventory() 
            input("Press any key to continue...")
        elif move == 'm':
            save_game(hero, enemies, map_instance)
            break

if __name__ == "__main__":
    main()