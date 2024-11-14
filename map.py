import os
import keyboard

class Room:
    def __init__(self, x, y, description=""):
        self.x = x
        self.y = y
        self.description = description

    def __repr__(self):
        return f"Room({self.x}, {self.y}, '{self.description}')"


class Map:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[(room.x, room.y)] = room

    def display(self, hero, enemies):
        os.system('cls')
        if not self.rooms:
            print("La carte est vide.")
            return
        
        min_x = min(room.x for room in self.rooms.values())
        max_x = max(room.x for room in self.rooms.values())
        min_y = min(room.y for room in self.rooms.values())
        max_y = max(room.y for room in self.rooms.values())

        print("Map:")
        print("")
        for y in range(max_y, min_y - 1, -1):
            row = ""
            for x in range(min_x, max_x + 1):
                if (x, y) in self.rooms:
                    if x == hero.x and y == hero.y:
                        row += "[O]"
                    elif any(x == enemy.x and y == enemy.y for enemy in enemies):
                        row += "[X]"
                    else:
                        row += "[ ]"
                else:
                    row += "   "
            print("            " + row)
        print("")
        print("")
        current_room = self.rooms.get((hero.x, hero.y))
        if current_room:
            print(f"You are in: {current_room.description}")
        print("Press '$' to exit the map.")
        keyboard.wait('$')
        os.system('cls')
        return