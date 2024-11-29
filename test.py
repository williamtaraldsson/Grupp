import random


input("""Välkommen till Adventure with William.

Spel instruktioner:
Du kommer under spelets gång att behöva välja mellan 
tre olika alternativ. Detta görs genom att 
skriva en av de ovan nämnda siffrorna och sedan trycka enter.
      
Tryck enter för att fortsätta""")

print("Välj vilken karaktär du vill spela som:")
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
        """)

karak = karaktar("Dvärg", "Oliver", 75, 0, 17, 1, [])
karak2 = karaktar("Alv", "William", 115, 0, 10, 1, [])
karak3 = karaktar("Tomte", "Elton", 100, 0, 12, 1, [])

karak.print_karaktar_info()
karak2.print_karaktar_info()
karak3.print_karaktar_info()
        
class item:
    def __init__(self, item_namn, typ, styrka_bonus, hp_bonus, rustning_hp_bonus, item_message):
        self.item_namn = item_namn
        self.typ = typ
        self.styrka_bonus = styrka_bonus
        self.hp_bonus = hp_bonus
        self.rustning_hp_bonus = rustning_hp_bonus
        self.item_message = item_message

rustning_rostig = item("Rostig rustning", "rustning", 0, 0, 10, "I kistan fanns det en rostig rustning, detta ger dig lite skydd!")
rustning_riddar = item("Riddar rustning", "rustning", 0, 0, 15, "I kistan fanns det en riddarrustning, detta ger dig mer skydd!")
rustning_drak = item("Drakrustning", "rustning", 0, 0, 25, "I kistan fanns det en mäktig drakrustning, detta ger dig mycket skydd!")
svard_rostig = item("Rostigt svärd", "svärd", 10, 0, 0, "I kistan fanns det ett rostigt svärd, detta gör lite extra skada!")
svard_lang = item("Långsvärd", "svärd", 20, 0, 0, "I kistan fanns det ett långsvärd, detta gör mycket skada!")
svard_drake = item("Drakdödare", "svärd", 30, 0, 0, "I kistan fanns det Drakdödaren, ett kraftfullt svärd!")
halsa_kebab = item("kebabrulle", "hälsa", 0, 50, 0, "I kistan fanns det en kebabrulle, den ger dig mer hälsa!")

kist_objekt = [rustning_rostig, rustning_riddar, rustning_drak, svard_rostig, svard_lang, svard_drake, halsa_kebab]

def get_number(alternativ1, alternativ2, alternativ3):
    siffra = input(f"""
    [1] {alternativ1}
    [2] {alternativ2}
    [3] {alternativ3}
    
    Välj alternativ 1, 2 eller 3: 
    --> """)

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
    spelare = karak3
    print("Du valde Tomte")


monster_typer = ["Goblin", "Orc", "Jätte", "Häxa", "Död kung", "Baby drake", "Lönmördare", ]


def monster_rum(spelare, monster):

    global inventory
    index = 1

    if spelare.level >= 1 and spelare.level <= 3:
        monster_hp = random.randint(15, 25)
        monster_styrka = random.randint(5, 15)
    elif spelare.level > 3 and spelare.level <= 6:
        monster_hp = random.randint(25, 50)
        monster_styrka = random.randint(15, 25)
    elif spelare.level > 6 and spelare.level < 10:
        monster_hp = random.randint(50, 80)
        monster_styrka = random.randint(25, 35)
    else:
        monster_hp = 300
        monster_styrka = 70

        
        
    print(f"I rummet finns en {monster} med styrka: {monster_styrka} och hp: {monster_hp}")
    while spelare.hp > 0 and monster_hp > 0:
        #print(inventory)
            
        
        print(f"{monster} attackerar, blocka attacken")
        spelar_gärning = str(input("""Välj vart på din kropp du vill blocka
            [1] Vänster
            [2] Mitten
            [3] Höger
            
        Block --> """))

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
            if spelare.rustning_hp > 0: 
                skada = monster_styrka
                skada_kvar = skada - spelare.rustning_hp
                spelare.rustning_hp = spelare.rustning_hp - skada
                if spelare.rustning_hp <= 0:
                    print("Du blev träffad av monstret. Din rustning gick sönder!")
                    spelare.hp = spelare.hp - skada_kvar
                    print(f"Du har nu {spelare.hp} hp kvar")
                else:
                    print(f"Du blev träffad och rustningen tog all skada. Rustningen har nu {spelare.rustning_hp} hp")
            else:    
                spelare.hp = spelare.hp - monster_styrka
                if spelare.hp < 0:
                    spelare.hp = 0
                    print(f"Du blev träffad och tog {monster_styrka} skada, du har nu {spelare.hp} hp kvar")
                else:
                    print(f"Du blev träffad och tog {monster_styrka} skada, du har nu {spelare.hp} hp kvar")

        if spelare.hp > 0:    
            print(f"Du attackerar nu {monster}")
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
                monster_hp = monster_hp - spelare.styrka
                if monster_hp > 0:
                    print(f"Monstret blev träffat och tog {spelare.styrka} skada, monstret har nu {monster_hp} hp kvar.")
                else:
                    monster_hp = 0
                    print(f"Monstret blev träffat och tog {spelare.styrka} skada, monstret har nu {monster_hp} hp kvar.")
                    print("Grattis! Du dödade monstret")
        else:
            continue
            

    
    spelare.level = spelare.level + 1

    return spelare

def använda_inventory(spelare):
    if not spelare.inventory:
        print("Ditt inventory är tomt.")
        return spelare

    print("Ditt inventory:")
    for i, item in enumerate(spelare.inventory, start=1):
        print(f"[{i}] {item.item_namn}")

    while True:
        try:
            val = int(input("Vilket item vill du använda? (0 för att avbryta): ")) - 1
            if val == -1:
                print("Du valde att inte använda något.")
                return spelare
            elif 0 <= val < len(spelare.inventory):
                valt_item = spelare.inventory.pop(val)
                print(f"Du använder {valt_item.item_namn}.")
                # Använd effekterna av item
                spelare.hp += valt_item.hp_bonus
                spelare.styrka += valt_item.styrka_bonus
                spelare.rustning_hp += valt_item.rustning_hp_bonus
                break
            else:
                print("Ogiltigt val. Försök igen.")
        except ValueError:
            print("Ange ett giltigt nummer.")
    return spelare

def kista_rum(spelare, loot):
    print(loot.item_message)
    if loot is None or loot == "Fälla":
        if loot == "Fälla":
            spelare.hp -= 10
            print(f"Du förlorade 10 hälsa! Din nuvarande hälsa är {spelare.hp}")
        return spelare

    if len(spelare.inventory) >= 5:
        print("Ditt inventory är fullt.")
        while True:
            print("Ditt inventory:")
            for i, item in enumerate(spelare.inventory, start=1):
                print(f"[{i}] {item.item_namn}")
            try:
                val = int(input("Vilket item vill du byta ut? (0 för att inte ta loot): ")) - 1
                if val == -1:
                    print("Du valde att inte ta något från kistan.")
                    return spelare
                elif 0 <= val < len(spelare.inventory):
                    borttaget = spelare.inventory.pop(val)
                    print(f"Du slängde {borttaget.item_namn} och tog {loot.item_namn}.")
                    spelare.inventory.append(loot)
                    break
                else:
                    print("Ogiltigt val.")
            except ValueError:
                print("Ange ett giltigt nummer.")
    else:
        print(f"Du lägger till {loot.item_namn} i ditt inventory.")
        spelare.inventory.append(loot)

    return spelare

falla = ["Sten klot","Fallgrop", "Pilar", "Spjut", "Viloplats" ]

def falla_rum(spelare):
    falla_skada = random.randint(5,35)
    falla_namn = random.choice(falla)
    if falla_namn == "Viloplats":
        spelare.hp = spelare.hp + falla_skada
        print(f"Inne i rummet finns en Eldstad där du vilar och får {falla_skada} mer hp")
    else:
        print(f"Du öppnade dörren och där fanns {falla_namn} som skadade dig {falla_skada} hp")
        if spelare.rustning_hp > 0:
            if falla_skada <= spelare.rustning_hp:
                spelare.rustning_hp -= falla_skada
                print(f"Rustningen tog all skada. Rustningen har nu {spelare.rustning_hp} hp")
            else:
                skada_kvar = falla_skada - spelare.rustning_hp
                spelare.rustning_hp = 0
                spelare.hp -= skada_kvar
                print(f"Din rustning gick sönder! Du tar {skada_kvar} i skada.")

    return spelare



room_types = [monster_rum, kista_rum, falla_rum]




while spelare.hp > 0 and spelare.level <= 9:
    
    print(f"Du har {spelare.hp}hp")
    gärning = get_number("Gå vidare", "Stats & inventory", "Avsluta")
    if gärning == "1":
        get_number("Vänstra dörren", "Dörren rakt fram", "Högra dörren")
        rum_func = random.choice(room_types)
        if rum_func == monster_rum:
            rum_func(spelare, random.choice(monster_typer))
        elif rum_func == kista_rum:
            rum_func(spelare, random.choice(kist_objekt))
        else:
            rum_func(spelare)
    
    elif gärning == "2":
        spelare.print_karaktar_info()
        använda_inventory(spelare)

    elif gärning == "3":
        spelare.hp = 0


if spelare.level == 10:
    monster_rum(spelare.hp, spelare.styrka, spelare.level, "Drake")

else:
    print("Spelet är slut")