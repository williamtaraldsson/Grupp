import random
import funktioner
import klasser


input("""Välkommen till Adventure with William.

Spel instruktioner:
Du kommer under spelets gång att behöva välja mellan 
tre olika alternativ. Detta görs genom att 
skriva en av de ovan nämnda siffrorna och sedan trycka enter.
      
Tryck enter för att fortsätta""")

print("Välj vilken karaktär du vill spela som:")


karak = klasser.karaktar("Dvärg", "Oliver", 75, 0, 17, 1, [])
karak2 = klasser.karaktar("Alv", "William", 115, 0, 10, 1, [])
karak3 = klasser.karaktar("Tomte", "Elton", 100, 0, 12, 1, [])

karak.print_karaktar_info()
karak2.print_karaktar_info()
karak3.print_karaktar_info()
        


rustning_rostig = klasser.item("Rostig rustning", "rustning", 0, 0, 10, "I kistan fanns det en rostig rustning, detta ger dig lite skydd!")
rustning_riddar = klasser.item("Riddar rustning", "rustning", 0, 0, 15, "I kistan fanns det en riddarrustning, detta ger dig mer skydd!")
rustning_drak = klasser.item("Drakrustning", "rustning", 0, 0, 25, "I kistan fanns det en mäktig drakrustning, detta ger dig mycket skydd!")
svard_rostig = klasser.item("Rostigt svärd", "svärd", 10, 0, 0, "I kistan fanns det ett rostigt svärd, detta gör lite extra skada!")
svard_lang = klasser.item("Långsvärd", "svärd", 20, 0, 0, "I kistan fanns det ett långsvärd, detta gör mycket skada!")
svard_drake = klasser.item("Drakdödare", "svärd", 30, 0, 0, "I kistan fanns det Drakdödaren, ett kraftfullt svärd!")
halsa_kebab = klasser.item("kebabrulle", "hälsa", 0, 50, 0, "I kistan fanns det en kebabrulle, den ger dig mer hälsa!")
falla_item = klasser.item("Fälla", "fälla", 0, -10, 0, "Det var en fälla i kistan! Du tar skada!")


kist_objekt = [rustning_rostig, rustning_rostig, rustning_rostig, rustning_riddar, rustning_riddar, rustning_drak, svard_rostig, svard_rostig, svard_rostig, svard_lang, svard_lang, svard_drake, halsa_kebab, halsa_kebab, falla_item, None]


    
vald = funktioner.get_number("Dvärg", "Alv", "Tomte")

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


falla = ["Sten klot","Fallgrop", "Pilar", "Spjut", "Viloplats" ]




room_types = ["kista_rum", "kista_rum", "falla_rum", "monster_rum", "monster_rum", "monster_rum"]


while spelare.hp > 0 and spelare.level <= 9:
    
    print(f"Du har {spelare.hp}hp och din rustning har {spelare.rustning_hp} sköld")
    gärning = funktioner.get_number("Gå vidare", "Stats & inventory", "Avsluta")
    if gärning == "1":
        funktioner.get_number("Vänstra dörren", "Dörren rakt fram", "Högra dörren")
        rum_func = random.choice(room_types)
        if rum_func == "monster_rum":
            funktioner.monster_rum(spelare, random.choice(monster_typer))
        elif rum_func == "kista_rum":
            funktioner.kista_rum(spelare, random.choice(kist_objekt))
        else:
            funktioner.falla_rum(spelare, random.choice(falla))
    
    elif gärning == "2":
        spelare.print_karaktar_info()
        for i, item in enumerate(spelare.inventory, start=1):
            print(f"[{i}] {item.item_namn}")
        funktioner.använda_inventory(spelare)

    elif gärning == "3":
        spelare.hp = 0


if spelare.level == 10:
    funktioner.monster_rum(spelare, "Drake")

else:
    print("Spelet är slut")

