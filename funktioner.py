import random

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
            if spelar_gärning in ["1","2","3"]:
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
                    spelare.rustning_hp = 0
                    spelare.inventory.pop()
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
                if spelar_gärning in ["1", "2", "3"]:
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

def kista_rum(spelare, loot):

    print("""I rummet du valde finns det en kista.
          Du går fram emot kistan och öppnar den""")
    
    print(loot.item_message)
    
    if loot is None:  # Om loot är tomt
        print("Kistan var tom. Du hittade inget av värde.")
        return spelare
    
    if loot.typ == "fälla":
        spelare.hp += loot.hp_bonus  
        print(f"Det var en fälla! Du tog {abs(loot.hp_bonus)} skada.")
        print(f"Din nuvarande hälsa är {spelare.hp}")
        return spelare
    

    if len(spelare.inventory) >= 5:
        while True:
            print("""Ditt inventory är fullt, vill du slänga något eller gå vidare?
                [1]Släng ett föremål från ditt inventory
                [2]Gå vidare utan att ta upp det du hittade i kistan
                  """)
            val = input("Gör ditt val här -->")
            
            if val in ["1", "2"]:
                break
            else:
                print("Det du skrev var inte ett heltal mellan 1 och 2, välj ett nummer mellan 1 och 2")
                continue
        for i, item in enumerate(spelare.inventory, start=1):
            print(f"[{i}] {item.item_namn}")

        if val == "1":
            while True:
                try:
                    index = int(input("Vilken plats vill du slänga? [1-5]: ")) - 1
                    if 0 <= index < len(spelare.inventory):
                        borttaget = spelare.inventory.pop(index)
                        print(f"Du slängde {borttaget.item_namn} från ditt inventory.")
                        spelare.styrka = spelare.styrka - borttaget.styrka_bonus
                        break
                    else:
                        print("Ogiltigt index. Välj mellan 1 och 5.")
                except ValueError:
                    print("Ange ett giltigt heltal.")
            spelare.inventory.append(loot)
            
        
        if val == "2":
            print("Du går vidare utan att ta med dig ditt föremål")
        
    
    elif len(spelare.inventory) < 5:
        spelare.inventory.append(loot)
        print(f"Du la till {loot.item_namn} i ditt inventory")

    return spelare


def falla_rum(spelare, falla_namn):
    falla_skada = random.randint(5,35)
    
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
        else:
            spelare.hp -= falla_skada
            print(f"Du tog {falla_skada} i skada.")
    return spelare


def använda_inventory(spelare):
    
    while True:
        print("""Vill du använda något från ditt inventory?
        [1] Ja, jag vill använda något från mitt inventory
        [2] Gå vidare utan att använda något från ditt inventory""")
        
        val = input("Gör ditt val --> ")
        if val in ["1", "2"]:
            break
        else:
            print("Ogiltigt val. Vänligen välj 1 eller 2.")

    if val == "1":
        if not spelare.inventory:
            print("Ditt inventory är tomt.")
        else:
            print("Ditt inventory:")
            for i, item in enumerate(spelare.inventory, start=1):
                print(f"[{i}] {item.item_namn:<16}: {item.styrka_bonus} extra styrka, "
                      f"{item.hp_bonus} extra hp, {item.rustning_hp_bonus} extra rustning.")
            
            while True:
                try:
                    använda = int(input(f"Vilket av dina items vill du använda? (1 - {len(spelare.inventory)}) --> ")) - 1
                    if 0 <= använda < len(spelare.inventory):
                        if spelare.inventory[använda].item_type == "äta":
                            item = spelare.inventory.pop(använda)
                            spelare.hp += item.hp_bonus
                        elif item.anvanda_ganger > 0:
                            print("Du har redan använt detta item en gång.")
                        else:                            
                            spelare.styrka += item.styrka_bonus
                            spelare.rustning_hp += item.rustning_hp_bonus
                            item.anvanda_ganger += 1
                            print(f"Du använde {item.item_namn}.")
                            print(f"""Dina nya stats: 
                                HP={spelare.hp}
                                Styrka={spelare.styrka} 
                                Rustning HP={spelare.rustning_hp}""")
                        break
                    else:
                        print(f"Ogiltigt val. Ange ett nummer mellan 1 och {len(spelare.inventory)}.")
                except ValueError:
                    print("Ogiltig inmatning. Vänligen ange ett giltigt heltal.")

    return spelare


def get_number(alternativ1, alternativ2, alternativ3):
    siffra = input(f"""
    [1] {alternativ1}
    [2] {alternativ2}
    [3] {alternativ3}
    
    Välj alternativ 1, 2 eller 3: 
    --> """)

    while True:
        if siffra in ["1", "2", "3"]:
            break
        else:
            print("Det du skrev var inte ett heltal mellan 1 och 3, välj ett nummer mellan 1 och 3")
        siffra = str(input("1, 2 eller 3 -->"))
    return siffra