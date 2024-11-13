import keyboard
import os

from map import Map, Room
from entity import Hero, Ennemy
from weapon import sword

def main() -> None:
    hero = Hero("Hero", 100, 0, 0)
    enemy = Ennemy("Ennemy", 50, 1, 0, sword)
    
    map_instance = Map()
    map_instance.add_room(Room(0, 0, "Salle de départ"))
    map_instance.add_room(Room(1, 0, "Salle à l'est"))
    map_instance.add_room(Room(0, 1, "Salle au nord"))
    map_instance.add_room(Room(1, 1, "Salle nord-est"))
    map_instance.add_room(Room(-1, 0, "Salle à l'ouest"))

    while True:
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
            break

if __name__ == "__main__":
    main()