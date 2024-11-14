import time
import os
import json

from map import Map, Room
from entity import Hero, Ennemy
from weapon import sword, axe, dager, fist  # Importer toutes les armes

SAVE_FILE = "savegame.json"

def display_menu() -> str:
    os.system('cls')
    print("=== MENU ===")
    print("1. Start Game")
    print("2. Load Game")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def save_game(hero, enemy, map_instance) -> None:
    game_state = {
        "hero": {
            "name": hero.name,
            "health": hero.health,
            "x": hero.x,
            "y": hero.y,
            "weapon": hero.weapon.name
        },
        "enemy": {
            "name": enemy.name,
            "health": enemy.health,
            "x": enemy.x,
            "y": enemy.y,
            "weapon": enemy.weapon.name
        },
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
    
    enemy = Ennemy(game_state["enemy"]["name"], game_state["enemy"]["health"], game_state["enemy"]["x"], game_state["enemy"]["y"], sword)
    enemy.weapon = next(w for w in [sword, axe, dager, fist] if w.name == game_state["enemy"]["weapon"])
    
    map_instance = Map()
    for room_data in game_state["map"]:
        map_instance.add_room(Room(room_data["x"], room_data["y"], room_data["description"]))
    
    return hero, enemy, map_instance

def main() -> None:
    hero, enemy, map_instance = None, None, None
    while True:
        choice = display_menu()
        if choice == '1':
            hero = Hero("Hero", 100, 0, 0)
            enemy = Ennemy("Ennemy", 50, 1, 0, sword)
            map_instance = Map()
            map_instance.add_room(Room(0, 0, "Salle de départ"))
            map_instance.add_room(Room(1, 0, "Salle à l'est"))
            map_instance.add_room(Room(0, 1, "Salle au nord"))
            map_instance.add_room(Room(1, 1, "Salle nord-est"))
            map_instance.add_room(Room(-1, 0, "Salle à l'ouest"))
            break
        elif choice == '2':
            try:
                hero, enemy, map_instance = load_game()
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
        time.sleep(2)
        os.system('cls')
        
        move = input('Enter direction (z/q/s/d) or , to display map, m to exit: ')
        
        if move == 'z':
            hero.move(0, 1, [enemy], map_instance)
        elif move == 's':
            hero.move(0, -1, [enemy], map_instance)
        elif move == 'q':
            hero.move(-1, 0, [enemy], map_instance)
        elif move == 'd':
            hero.move(1, 0, [enemy], map_instance)
        elif move == ',':
            map_instance.display(hero)
        elif move == 'm':
            save_game(hero, enemy, map_instance)
            break

if __name__ == "__main__":
    main()