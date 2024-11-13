import os

os.system("")

class HealthBar:
    symbol_remaining = "█"
    symbol_lost = "░"
    border = "|"
    colors: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"
                    }
    
    def __init__(self, entity, lenght = 20, is_colored = True, color = "") -> None:
        self.entity = entity
        self.lenght = lenght
        self.current_value = entity.health
        self.max_value = entity.health_max
        
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]
    
    def update(self) -> None:
        self.current_value = self.entity.health
    
    def draw(self) -> None:
        remaining = round(self.current_value / self.max_value * self.lenght)
        lost = self.lenght - remaining
        
        print(f"{self.entity.name}'s HEALTH: {self.entity.health}/{self.entity.health_max}")
        print  (  f"{self.border}"
                f"{self.color if self.is_colored else ''}"
                f"{remaining * self.symbol_remaining}"
                f"{lost * self.symbol_lost}"
                f"{self.colors['default'] if self.is_colored else ''}"
                f"{self.border}")