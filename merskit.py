if x == 1: #Här slumpas det fram monster i rummet
    

elif x == 2: 
        print("Det är en kista")
        
else: #Här slumpas det fram fälla i rummet
        print("Det är en fälla")
        
    
    level = level + 1 
    return level

vald = str(input("1. Dvärg 2. Alv 3. Tomte --> "))

vald != 1 and vald != 2 and vald != 3:

def kista_rum(spelare):
    
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
        spelare.hp -= 10
        print(f"Du förlorade 10 hälsa! Din nuvarande hälsa är: {spelare.hp}")
        if spelare.hp <= 0:
            print("Du har förlorat all din hälsa. Spelet är slut!")
        return spelare.hp
    

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



    

    def visa_rum_med_förstoringsglas():
        # En lista med varje rumstyp
        rum_lista = [monster_rum, kista_rum, falla_rum]
        # Slumpa ordningen på listan
        random.shuffle(rum_lista)
        # Hämta namnen på varje funktion
        rum_bakom_dörrar = [rum.__name__ for rum in rum_lista]
        print("Med ditt förstoringsglas ser du vad som finns bakom dörrarna:")
        print(f"[1] {rum_bakom_dörrar[0]} | [2] {rum_bakom_dörrar[1]} | [3] {rum_bakom_dörrar[2]}")
        return rum_lista
    
    def använda_inventory(hp, styrka):
    
    global inventory
    global objekt
    
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
        elif inventory[använda] == "Starkare svärd":
            styrka =+ 10
        elif inventory[använda] == "Förstoringsglas":
            objekt == "Förstoringsglas"


    return hp, styrka, objekt   
    
def visa_rum_med_förstoringsglas():
        
        rum_lista = [monster_rum, kista_rum, falla_rum]
        
        random.shuffle(rum_lista)
        
        rum_bakom_dörrar = [rum.__name__ for rum in rum_lista]
        print("Med ditt förstoringsglas ser du vad som finns bakom dörrarna:")
        print(f"[1] {rum_bakom_dörrar[0]} | [2] {rum_bakom_dörrar[1]} | [3] {rum_bakom_dörrar[2]}")
        return rum_lista                
# -----------kanske---------------