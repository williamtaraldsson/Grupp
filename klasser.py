class karaktar:
    def __init__ (self, ras, namn, hp, rustning_hp, styrka, level, inventory):
        self.ras = ras
        self.namn = namn
        self.hp = hp
        self.rustning_hp = rustning_hp
        self.styrka = styrka
        self.level = level
        self.inventory = inventory

    def print_karaktar_info(self):
        print(f"""
        Ras: {self.ras}
        Namn: {self.namn}
        Hp: {self.hp}
        Styrka: {self.styrka}
        Level: {self.level}
        Rustning: {self.rustning_hp}
        """)

class item:
    def __init__(self, item_namn, typ, styrka_bonus, hp_bonus, rustning_hp_bonus, item_message, item_type):
        self.item_namn = item_namn
        self.typ = typ
        self.styrka_bonus = styrka_bonus
        self.hp_bonus = hp_bonus
        self.rustning_hp_bonus = rustning_hp_bonus
        self.item_message = item_message
        self.item_type = item_type