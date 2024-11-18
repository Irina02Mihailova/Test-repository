from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец выбирает меч.")
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец выбирает лук.")
        print("Боец наносит удар из лука.")

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def battle(self):
        self.weapon.attack()
        print("Монстр побежден!")

class Monster():
    pass

sword = Sword()

bow1 = Bow()

fighter = Fighter(sword)

fighter.battle()

fighter.change_weapon(bow1)

fighter.battle()