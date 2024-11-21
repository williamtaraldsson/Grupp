import random

input("Tryck på enter för att fortsätta")

print("""Välkommen till Adventure with William
      Välj vilken karaktär du vill spela som""")

class karaktar:
    def __init__ (self, ras, namn, hp, styrka):
        self.ras = ras
        self.namn = namn
        self.hp = hp
        self.styrka = styrka

    def print_karaktar_info(self):
        print(self.ras, self.namn, self.hp, self.styrka)

karak = karaktar("Dvärg", "Oliver", 100, 10)
karak2 = karaktar("Alv", "William", 100, 5)
karak3 = karaktar("Tomte", "Elton", 100, 0)

karak.print_karaktar_info()
karak2.print_karaktar_info()
karak3.print_karaktar_info()

vald = int(input("1. Dvärg 2. Alv 3. Tomte --> "))

while vald != 1 and vald != 2 and vald != 3:
    if vald == 1 or vald == 2 or vald == 3:
        spelare = vald
    else:
        print("Det du skrev var inte ett heltal mellan 1 och 3, välj ett nummer mellan 1 och 3")
    vald = int(input("1, 2 eller 3 -->"))

spelare = vald
if spelare == 1:
    spelare = karak
elif spelare == 2:
    spelare = karak2
elif spelare == 3:
    spealre = karak3

def monster_rum(ras, namn, hp, styrka):
    print("hej")


def kista_rum(ras, namn, hp, styrka):
    print("hej")


def fälla_rum(ras, namn, hp, styrka):
    print(9)

    
room_selection_number = random.randint(1,3)


https://prod.liveshare.vsengsaas.visualstudio.com/join?268E7394D4753BBCF009EBB396062F0AB675