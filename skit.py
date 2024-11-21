import random

input("Tryck på enter för att fortsätta")

print("""Välkommen till Adventure with William
Välj vilken karaktär du vill spela som""")

class karaktar:
    def __init__ (self, ras, namn, hp, styrka, level):
        self.ras = ras
        self.namn = namn
        self.hp = hp
        self.styrka = styrka
        self.level = level

    def print_karaktar_info(self):
        print(f"""Ras: {self.ras}
        Namn: {self.namn}
        Hp: {self.hp}
        Styrka: {self.styrka}
        Level: {self.level}""")
        print(self.ras, self.namn, self.hp, self.styrka, self.level)

karak = karaktar("Dvärg", "Oliver", 75, 15, 1)
karak2 = karaktar("Alv", "William", 125, 5, 1)
karak3 = karaktar("Tomte", "Elton", 100, 10, 1)
rustning = 0

inventory = []

vald = str(input("1. Dvärg 2. Alv 3. Tomte --> "))


while True:
    if vald in str([1,2,3]):
        spelare = vald
        break
    else:
        print("Det du skrev var inte ett heltal mellan 1 och 3, välj ett nummer mellan 1 och 3")
    vald = str(input("1, 2 eller 3 -->"))
    


spelare = vald
if spelare == 1:
    spelare = karak
    print("Du valde Dvärg")
elif spelare == 2:
    spelare = karak2
    print("Du valde Alv")
elif spelare == 3:
    spealre = karak3
    print("Du valde Tomte")


monster_typer = ["Goblin", "Orc", "Neos forehead", "Martins glänsande skalp", "Skatteverket", "Troll", "Spöke", "Jätte", "Häxa",]

def monster_rum(ras, namn, hp, styrka, level):
    print(""""Bakom dörren du valde finns ett monster""")
    
    while hp and monster_hp:
        print("Monstret attackerar, blocka attacken")
        spelar_gärning = str(input("välj mellan 1, 2, eller 3 för att blocka"))
        monster_gärning = random.randint(1,3)
        if spelar_gärning == monster_gärning:
            print("Du blockade och tog ingen skada.")
        else:
            hp = hp - monster_styrka
        


def kista_rum(input_lista):
    print("I rummet du valde finns det en kista")
    print("Du går fram emot kistan och öppnar den")
    loot
    slump_nummer = random.randint(1,3)
    if slump_nummer == 1:
        print("I kistan fanns det en kebabrulle, den ger dig mer hälsa!")
    loot = "kebab"
    if slump_nummer == 2:
        print("I kistan fanns det rustingsdel, detta ger dig mer skydd emot dina fiender!")
        loot = "Rustningsdel"
    if slump_nummer == 3:
        print("I kistan fanns det ett starkare svärd, detta gör mer skada emot dina fiender")
        loot = "Starkare svärd"
    if slump_nummer == 4:
        print("I kistan finns det förstoringsglas, detta kan du använda för att se vad som finns bakom dörrarna")
        loot = "Förstoringsglas"

def fälla_rum(ras, namn, hp, styrka):
    print(9)

# def get_user_input():
#     try:
#         tal = int(input("Ditt val -->"))
#     except ValueError:
#         print("Det är inte ett heltal.")
#         return 0        
#     except:
#         print("Något gick fel.")
#         return 0
#     return tal

while True:
    n=int(input("""Vad vill du göra?
              
    [1] Gå vidare
    [2] Invetory & stats
    [3] Avsluta"""))
    print(get_user_input())
    
    if n in str([1,2,3]):
        break
    else:
        print("Det du skrev var inte ett heltal mellan 1 och 3, välj ett nummer mellan 1 och 3")
        continue
