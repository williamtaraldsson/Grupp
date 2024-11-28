import random

input("Tryck på enter för att fortsätta")

input("""Välkommen till Adventure with William.
Spel instruktioner:
Du kommer under spelets gång att behöva välja mellan 
tre olika alternativ. Detta görs genom att 
skriva en av de ovan nämnda siffrorna och sedan trycka enter""")

print("Välj vilken karaktär du vill spela som")
class karaktar:
    def __init__ (self, ras, namn, hp, styrka, level):
        self.ras = ras
        self.namn = namn
        self.hp = hp
        self.styrka = styrka
        self.level = level

    def print_karaktar_info(self):
        print(f"""
        Ras: {self.ras}
        Namn: {self.namn}
        Hp: {self.hp}
        Styrka: {self.styrka}
        Level: {self.level}
        """)
        

karak = karaktar("Dvärg", "Oliver", 75, 17, 1)
karak2 = karaktar("Alv", "William", 115, 10, 1)
karak3 = karaktar("Tomte", "Elton", 100, 12, 1)
rustning = 0
karak.print_karaktar_info()
karak2.print_karaktar_info()
karak3.print_karaktar_info()

inventory = []

vald = str(input("1. Dvärg 2. Alv 3. Tomte --> "))

def get_number(alternativ1, alternativ2, alternativ3):
    input()

    while True:
        if siffra in "123":
            break
        else:
            print("Det du skrev var inte ett heltal mellan 1 och 3, välj ett nummer mellan 1 och 3")
        siffra = str(input("1, 2 eller 3 -->"))
    return siffra
    
vald = get_number(vald)

spelare = vald
if spelare == "1":
    spelare = karak
    print("Du valde Dvärg")
elif spelare == "2":
    spelare = karak2
    print("Du valde Alv")
elif spelare == "3":
    spealre = karak3
    print("Du valde Tomte")


monster_typer = ["Goblin", "Orc", "Jätte", "Häxa", "Död kung", "Baby drake", "Lönmördare", ]

def monster_rum(ras, namn, hp, styrka, level):
    monster_typ = random.randint(monster_typer)
    if level >= 1 and level <= 3:
        monster_hp = random.randint(15, 25)
        monster_styrka = random.randint(5, 15)
    elif level > 3 and level <= 6:
        monster_hp = random.randint(25, 50)
        monster_styrka = random.randint(15, 25)
    elif level > 6 and level < 10:
        monster_hp = random.randint(50, 80)
        monster_styrka = random.randint(25, 35)
        
    print(f"Bakom dörren du valde finns en {monster_typ} med styrka: {monster_styrka} och hp: {monster_hp}")
    while hp > 0 or monster_hp > 0:
        print(f"{monster_typ} attackerar, blocka attacken")
        spelar_gärning = str(input("""Välj vart på din kropp du vill blocka
            [1] Vänster
            [2] Mitten
            [3] Höger
            
        Block -->"""))

        while True:
            if spelar_gärning in "123":
                break
            else:
                print("Det du skrev var inte ett heltal mellan 1 och 3, välj ett nummer mellan 1 och 3")
                spelar_gärning = input("1, 2 eller 3 -->")

        monster_gärning = str(random.randint(1,3))
        if spelar_gärning == monster_gärning:
            print("Du blockade och tog ingen skada.")
        else:
            hp = hp - monster_styrka
            print(f"Du blev träffas och tog {monster_styrka} hp, du har nu {hp} hp kvar")
            
        print(f"Du attackerar nu {monster_typ}")
        spelar_gärning = input("""Välj vart du vill attackera
            [1] Vänster
            [2] Mitten
            [3] Höger
            
        Attack -->""")

        while True:
            if spelar_gärning in "123":
                break
            else:
                print("Det du skrev var inte ett heltal mellan 1 och 3, välj ett nummer mellan 1 och 3")
                spelar_gärning = str(input("1, 2 eller 3 -->"))

        monster_gärning = str(random.randint(1,3))
        if spelar_gärning == monster_gärning:
            print("Monstret blockade din attack.")
        else:
            monster_hp = monster_hp - styrka
            print(f"Monstret blev träffat och tog {styrka} hp, monstret har nu {monster_hp} hp kvar.")
    
    return hp, level
    
            

    
            
        


def kista_rum():
    print("I rummet du valde finns det en kista")
    print("Du går fram emot kistan och öppnar den")
    global inventory
    
    loot_items = [
        ("kebab", "I kistan fanns det en kebabrulle, den ger dig mer hälsa!"),
        ("Rustningsdel", "I kistan fanns det en rustningsdel, detta ger dig mer skydd mot dina fiender!"),
        ("Starkare svärd", "I kistan fanns det ett starkare svärd, detta gör mer skada mot dina fiender!"),
        ("Förstoringsglas", "I kistan finns det ett förstoringsglas, detta kan du använda för att se vad som finns bakom dörrarna!")
    ]
    
    loot, message = random.choice(loot_items)
    print(message)
    
    if len(inventory) >= 5:
        while True:
            print("""Ditt inventory är fullt, vill du slänga något eller gå vidare?
                [1]Släng ett föremål från ditt inventory
                [2]Gå vidare utan att ta upp det du hittade i kistan
                  """)
            n = input("Gör ditt val här -->")
            
            if n in ["1","2"]:
                break
            else:
                print("Det du skrev var inte ett heltal mellan 1 och 2, välj ett nummer mellan 1 och 2")
                continue
        
        if n == 1:
            while True:
                try:
                    index = int(input("Vilken plats vill du slänga? [1-5]: ")) - 1
                    if 0 <= index < len(inventory):
                        borttaget = inventory.pop(index)
                        print(f"Du slängde {borttaget} från ditt inventory.")
                        break
                    else:
                        print("Ogiltigt index. Välj mellan 1 och 5.")
                except ValueError:
                    print("Ange ett giltigt heltal.")
            inventory.append(loot)
            
        
        if n == 2:
            print("Du går vidare utan att ta med dig ditt föremål")
            return inventory
    
    elif len(inventory) < 5:
        inventory.append(loot)
        print("Du la till " + loot + " i ditt inventory")
        return inventory

    


fälla = ["Sten klot","Fallgrop", "Pilar", "Spjut",  ]

def fälla_rum(ras, namn, hp, styrka):
    fälla_skada = random.randint(5,35)
    fälla_namn = random.randint(fälla)

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

input
gärning = get_number()


https://prod.liveshare.vsengsaas.visualstudio.com/join?1272A86540D93B1152E9DDF65FC904DFE7D3