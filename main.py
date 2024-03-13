
class AttackStrategy:
    def attack(self):
        pass

class SamuraiAttack(AttackStrategy):
    def attack(self):
        print("Seleccionaste Samurai. Aquí están algunas opciones de ataque:")
        options = [
            "1. Cubrirse (Escudo de caballero viejo)",
            "2. Atacar (Uchigatana)",
            "3. Rodar"
        ]
        print("\n".join(options))
        choice = input("Selecciona una opción: ")
        print("Realizando movimiento:", options[int(choice) - 1])

class ArcherAttack(AttackStrategy):
    def attack(self):
        print("Seleccionaste Arquero. Aquí están algunas opciones de ataque:")
        options = [
            "1. Cubrirse (Parma de luz solar)",
            "2. Atacar (Arco Grande del Matadragones)",
            "3. Rodar"
        ]
        print("\n".join(options))
        choice = input("Selecciona una opción: ")
        print("Realizando movimiento:", options[int(choice) - 1])

class KnightAttack(AttackStrategy):
    def attack(self):
        print("Seleccionaste Caballero. Aquí están algunas opciones de ataque:")
        options = [
            "1. Cubrirse (Escudo de Drangleic)",
            "2. Atacar (Espadón de luz de luna)",
            "3. Rodar"
        ]
        print("\n".join(options))
        choice = input("Selecciona una opción: ")
        print("Realizando movimiento:", options[int(choice) - 1])

class Unit:
    def __init__(self, attack_strategy):
        self.attack_strategy = attack_strategy

    def set_attack_strategy(self, attack_strategy):
        self.attack_strategy = attack_strategy

    def attack(self):
        self.attack_strategy.attack()

def choose_attack_strategy():
    print("Elige una estrategia de ataque:")
    print("1. Samurai (Katana)")
    print("2. Arquero (flechas)")
    print("3. Caballero (espada larga)")
    choice = input("Selecciona una opción: ")
    if choice == "1":
        return SamuraiAttack()
    elif choice == "2":
        return ArcherAttack()
    elif choice == "3":
        return KnightAttack()
    else:
        print("Opción no válida. Seleccionando samurai por defecto.")
        return SamuraiAttack()

chosen_strategy = choose_attack_strategy()
unit = Unit(chosen_strategy)
unit.attack()