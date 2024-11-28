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

def get_number(alternativ1, alternativ2, alternativ3):
    siffra = input(f"""
    [1] {alternativ1}
    [2] {alternativ2}
    [3] {alternativ3}
    
    Välj alternativ 1, 2 eller 3 --> """)

    while True:
        if siffra in "123":
            break
        else:
            print("Det du skrev var inte ett heltal mellan 1 och 3, välj ett nummer mellan 1 och 3")
        siffra = str(input("1, 2 eller 3 -->"))
    return siffra
    
vald = get_number("Dvärg", "Alv", "Tomte")

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

def använda_inventory(hp):
    
    global inventory
    
    while True:
            print("""Vill du använda något från ditt inventory?
            [1] Ja, jag vill använda något från mitt inventory
            [2] Gå vidare utan att använda något från ditt inventory""")
    
            val = input("Gör ditt val --> ")
            if val in ["1", "2"]:
                break
            else:
                print("Det du skrev var inte 1 eller 2, välj 1 eller 2.")
                continue

    if val == "1":  
        print("Ditt inventory:")
        for i, item in enumerate(inventory, start=1):
            print(f"[{i}] {item}")
        
        använda = int(input("vilket av dina items vill du använda?"))
        if inventory[använda] == "Kebab":
            hp =+ 50
        elif inventory[använda] == "Rustningsdel":
            hp =+ 25
    
    return hp
                

def monster_rum(hp, styrka, level):

    global inventory
    index = 1

    monster_typ = random.choice(monster_typer)
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
    while hp > 0 and monster_hp > 0:
        print(inventory)
            
        
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
    
            

    
            
        


def kista_rum(hp):
    
    global inventory

    print("""I rummet du valde finns det en kista"
          Du går fram emot kistan och öppnar den""")
    
    loot_items = [
        ("Kebab", "I kistan fanns det en kebabrulle, den ger dig mer hälsa!"),
        ("Rustningsdel", "I kistan fanns det en rustningsdel, detta ger dig mer skydd mot dina fiender!"),
        ("Starkare svärd", "I kistan fanns det ett starkare svärd, detta gör mer skada mot dina fiender!"),
        ("Förstoringsglas", "I kistan finns det ett förstoringsglas, detta kan du använda för att se vad som finns bakom dörrarna!"),
        (None, "Du öppnar kistan, men den är tom... Otur!"),
        ("Fälla", "Det är en fälla! Kistan sprutar ut gift och du förlorar hälsa!")
    ]

    loot, message = random.choice(loot_items)
    print(message)
    

    if loot is None:
        print("Det finns inget att lägga till i ditt inventory. Spelet forsätter.")
        return
    
    if loot == "Fälla":
        hp -= 10
        print(f"Du förlorade 10 hälsa! Din nuvarande hälsa är: {hp}")
        if hp <= 0:
            print("Du har förlorat all din hälsa. Spelet är slut!")
        return hp
    

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

    


falla = ["Sten klot","Fallgrop", "Pilar", "Spjut", "Viloplats" ]

def falla_rum(hp, styrka, level):
    falla_skada = random.randint(5,35)
    falla_namn = random.choice(falla)
    if falla_namn == "Viloplats":
        hp = hp + falla_skada
        print(f"Inne i rummet finns en Eldstad där du vilar och får {falla_skada} mer hp")
    else: 
        hp = hp - falla_skada
        print(f"Du öppnade dörren och där fanns {falla_namn}som skadade dig {falla_skada} hp")
    return hp, styrka, level



room_types = [monster_rum, kista_rum, falla_rum]


while spelare.hp > 0 or spelare.level == 9:
    print()
    gärning = get_number("Gå vidare", "Stats & inventory", "Avsluta")
    if gärning == "1":
        get_number("Vänstra dörren", "Dörren rakt fram", "Högra dörren")
        rum_func = random.choice(room_types)
        rum_func(spelare.hp, spelare.styrka, spelare.level)
