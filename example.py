class Weapon:
    def __init__(self, name, power, weight):
        self.name = name
        self.power = power #between 0 and 100
        self.durability = 1 #between 0 and 1
        self.weight = weight #between 0 and 100

    def damage(self):
        return self.power * self.durability

class Player:
    def __init__(self, player_name, weapon):
        self.name = player_name
        self.weapon = weapon
        self.hp = 50

    def attack(self, other_player):
        other_player.hp -= 10
        print(f"{self.name} attacked {other_player.name} with {self.weapon}!")
        return self

    def heal(self):
        self.hp += 5
        print(f"{self.name} used a healing potion!")

axe = Weapon("Battle Axe", 22, 20)
sword = Weapon("Long Sword", 15, 3)
knife = Weapon("Knife", 5, 1)

connor = Player("Connor", sword)
kendra = Player("Kendra", knife)
john = Player("John", axe)

print(connor.weapon.power)