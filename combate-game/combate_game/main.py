from colorama import init, Fore, Style
from random import randint


init(autoreset=True)


class Character:
    def __init__(self, name: str, health: int, level: int):
        self.__name = name
        self.__health = health
        self.level = level

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_level(self):
        return self.level

    def show_stats(self):
        return f"\nName: {self.get_name()}\nHealth: {self.get_health()}\nLevel: {self.get_level()}\n"

    def attack(self, enemy: "Character"):
        damage = randint(self.get_level() * 2, self.get_level() * 4)
        enemy.update_health(damage)
        print(
            f"\n{Fore.YELLOW}{self.get_name()} attacked {enemy.get_name()} for {damage} damage{Style.RESET_ALL}\n"
        )

    def update_health(self, damage: int):
        self.__health -= damage
        if self.__health <= 0:
            self.__health = 0
            print(f"{Fore.RED}{self.get_name()} has been defeated{Style.RESET_ALL}")


# Hero
class Hero(Character):
    def __init__(self, name: str, health: int, level: int, attack_type: str):
        super().__init__(name, health, level)
        self.__attack_type = attack_type

    def get_attack_type(self):
        return self.__attack_type

    def show_stats(self):
        return f"{super().show_stats()}\nAttack Type: {self.get_attack_type()}"

    def magic_attack(self, enemy: "Character"):
        damage = randint(self.get_level() * 5, self.get_level() * 8)
        enemy.update_health(damage)
        print(
            f"\n{Fore.CYAN}{self.get_name()} used a magic attack on {enemy.get_name()} for {damage} damage{Style.RESET_ALL}\n"
        )


# Enemy
class Enemy(Character):
    def __init__(self, name: str, health: int, level: int, enemy_type: str):
        super().__init__(name, health, level)
        self.__enemy_type = enemy_type

    def get_enemy_type(self):
        return self.__enemy_type

    def show_stats(self):
        return f"{super().show_stats()}\nEnemy Type: {self.get_enemy_type()}"


# Battle
class Battle:
    """
    This class is responsible for managing the battle between the hero and the enemy.
    """

    def __init__(self, hero: Hero, enemy: Enemy):
        self.hero = hero
        self.enemy = enemy

    def start_battle(self):
        print(
            f"Battle started between {self.hero.get_name()} and {self.enemy.get_name()}"
        )
        while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
            print(f"Hero details: {self.hero.show_stats()}")
            print(f"Enemy details: {self.enemy.show_stats()}")

            input("Press Enter to attack...")
            attack_type: str = input(
                "Choose attack type: (1) Super Attack, (2) Magic Attack: "
            )

            if attack_type == "1":
                self.hero.attack(self.enemy)
            elif attack_type == "2":
                self.hero.magic_attack(self.enemy)
            else:
                print("Invalid attack type")

            if self.enemy.get_health() > 0:
                self.enemy.attack(self.hero)

        if self.hero.get_health() > 0:
            print(
                f"\n{Fore.GREEN}{self.hero.get_name()} wins the battle{Style.RESET_ALL}"
            )

        else:
            print(
                f"\n{Fore.RED}{self.enemy.get_name()} wins the battle{Style.RESET_ALL}"
            )


hero = Hero(name="Arus", health=200, level=10, attack_type="Super Attack")
enemy = Enemy(name="Mago", health=100, level=10, enemy_type="Fire")


battle = Battle(hero, enemy)
battle.start_battle()
