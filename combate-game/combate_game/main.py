from colorama import init, Fore, Style
from random import randint
from enum import Enum


init(autoreset=True)


class AttackType(Enum):
    SUPER_ATTACK = "Super Attack"
    MAGIC_ATTACK = "Magic Attack"


class EnemyType(Enum):
    FIRE = "Fire"
    ICE = "Ice"
    EARTH = "Earth"
    WIND = "Wind"


class Character:
    def __init__(self, name: str, health: int, level: int) -> None:
        self.name: str = name
        self._health: int = health
        self.level: int = level

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, health: int) -> None:
        self._health = max(health, 0)

    @property
    def is_dead(self) -> bool:
        return self._health <= 0

    def show_stats(self) -> str:
        return f"\nName: {self.name}\nHealth: {self.health}\nLevel: {self.level}\n"

    def attack(self, other: "Character") -> None:
        damage: int = randint(self.level * 2, self.level * 4)
        other.health -= damage
        print(
            f"\n{Fore.YELLOW}{self.name} attacked {other.name} for {damage} damage{Style.RESET_ALL}\n"
        )


class Hero(Character):
    def __init__(
        self, attack_type: AttackType, name: str, health: int, level: int
    ) -> None:
        super().__init__(name, health, level)
        self.attack_type: AttackType = attack_type

    def show_stats(self) -> str:
        return f"{super().show_stats()}\nAttack Type: {self.attack_type.value}"

    def magic_attack(self, enemy: "Character") -> None:
        damage: int = randint(self.level * 5, self.level * 8)
        enemy.health -= damage
        print(
            f"\n{Fore.CYAN}{self.name} used a magic attack on {enemy.name} for {damage} damage{Style.RESET_ALL}\n"
        )


# Enemy
class Enemy(Character):
    def __init__(
        self, name: str, health: int, level: int, enemy_type: EnemyType
    ) -> None:
        super().__init__(name, health, level)
        self.enemy_type: EnemyType = enemy_type

    def show_stats(self) -> str:
        return f"{super().show_stats()}\nEnemy Type: {self.enemy_type.value}"


# Battle
class Battle:
    """
    This class is responsible for managing the battle between the hero and the enemy.
    """

    def __init__(self, hero: Hero, enemy: Enemy) -> None:
        self.hero: Hero = hero
        self.enemy: Enemy = enemy

    def start_battle(self) -> None:
        print(f"Battle started between {self.hero.name} and {self.enemy.name}")
        while not self.hero.is_dead and not self.enemy.is_dead:
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

            if not self.enemy.is_dead:
                self.enemy.attack(self.hero)

        if self.hero.is_dead:
            print(f"\n{Fore.RED}{self.enemy.name} wins the battle{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.GREEN}{self.hero.name} wins the battle{Style.RESET_ALL}")


hero: Hero = Hero(
    name="Arus", health=200, level=10, attack_type=AttackType.SUPER_ATTACK
)
enemy: Enemy = Enemy(name="Mago", health=100, level=10, enemy_type=EnemyType.FIRE)


battle: Battle = Battle(hero, enemy)
battle.start_battle()
