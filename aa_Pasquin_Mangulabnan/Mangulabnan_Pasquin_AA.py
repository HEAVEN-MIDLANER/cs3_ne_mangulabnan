class Game:
    def __init__(self, turn=1,game_end=False):
        self.game_end= game_end
        self.turn= turn
class Plant:
    def __init__(self, name, health, damage):
        self.name= name
        self.health= health
        self.damage= damage
        
    def attack(self, zombie):
        if self.health > 0:
            zombie.take_damage(self.damage)
            print(f"{self.name} attacked {zombie.name} for {self.damage} damage")
        else:
            print(f"{self.name} is defeated and cannot attack")
    def take_damage(self, amount):
        self.health = self.health-amount
        if self.health < 0 :
            self.health= 0
        print(f"{self.name} Health: {self.health}")
class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name= name
        self.health= health
        self.damage= damage
        self.distance= distance
        
    def move(self, steps):
        if self.health > 0:
            self.distance = self.distance - steps
            if self.distance < 0:
                self.distance = 0
            print(f"{self.name} moved forward Distance: {self.distance}")
    def attack(self, plant):
        if self.distance == 0 and self.health > 0 and plant.health > 0:
            plant.take_damage(self.damage)
            print(f"{self.name} attacked {plant.name} for {self.damage} damage")
    def take_damage(self, amount):
        self.health = self.health - amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} Health: {self.health}")
def main():
    game = Game()
    plant1 = Plant("Peashooter", 15, 5)
    plant2 = Plant("Snow Pea", 15, 3)
    zombie = Zombie("Zombie", 35, 10, 2)
    print("MINI PLANTS VS ZOMBIES")
    
    while not game.game_end:
        print(f"TURN {game.turn}")
        print(f"{plant1.name} HP: {plant1.health} |{plant2.name} HP: {plant2.health} |{zombie.name} HP: {zombie.health} |Distance: {zombie.distance}")
        
        if plant1.health > 0:
            choice = input(f"Press Enter to make {plant1.name} attack or type pass: ")
            if choice = "pass":
                plant1.attack(zombie)
                
        if zombie.health <= 0:
            print("Zombie defeated! Plants win!")
            game.game_end = True
            break
        if plant2.health > 0:
            choice = input(f"Press Enter to make {plant2.name} attack or type pass: ")
            if choice != "pass":
                plant2.attack(zombie)
                
        if zombie.health <= 0:
            print("Zombie defeated! PLANTS win!")
            game.game_end = True
            break
        print("zombie turn:")
        if zombie.distance > 0:
            zombie.move(1)
        else:
            if plant1.health > 0:
                zombie.attack(plant1)
            elif plant2.health > 0:
                zombie.attack(plant2)
        if plant1.health <= 0 and plant2.health <= 0:
            print("All plants destroyed! zombie wins!")
            game.game_end = True
            break
        game.turn = game.turn + 1
main()