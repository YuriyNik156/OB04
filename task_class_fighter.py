# Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.

from abc import ABC, abstractmethod

# Создаем абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Создаем подклассы оружия Sword, Bow и Axe
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец совершает выстрел из лука.")

class Axe(Weapon):
    def attack(self):
        print("Боец наносит удар топором.")

class Nokia3310(Weapon):
    def attack(self):
        print("Боец бьет телефоном-кирпичом. Эпик!")

# Создаем класс бойца Fighter
class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, new_weapon:Weapon):
        self.weapon = new_weapon
        print(f"Боец выбирает оружие - {new_weapon.__class__.__name__}.")

    def attack(self):
        self.weapon.attack()

# Создаем класс монстра Monster
class Monster():
    def __init__(self):
        self.undefeated = True

    def attacked_by_fighter(self):
        self.undefeated = False
        print("Монстр побежден!")

# Механизм демонстрации боя между бойцом и монстром
fighter = Fighter(Axe())
monster = Monster()

print("Боец выбирает топор.")
fighter.attack()
monster.attacked_by_fighter()

print("Боец выбирает лук.")
fighter.change_weapon(Bow())
fighter.attack()
monster.attacked_by_fighter()

print("Боец выбирает копье.")
fighter.change_weapon(Nokia3310())
fighter.attack()
monster.attacked_by_fighter()