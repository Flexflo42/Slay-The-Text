import run

class Progress:
    def __init__(self, name, value, cost, tier=0):
        self.name = name
        self.value = value
        self.cost = cost
        self.tier = tier
        # max tier/level als attribut einfügen bei optionen die weniger als 5 upgrade haben -> funktionen anpassen




#Factory Functions

def progress_hp():
    return Progress ("HP", 10, 1)

def progress_mana():
    return Progress ("Mana", 10, 1)

def progress_armor():
    return  Progress ("Armor", 1, 1)

def progress_damage():
    return Progress ("Damage", 3, 1)

def progress_magic():
    return Progress ("Magic", 3, 1)




progress_list = [progress_hp(), progress_mana(), progress_armor(), progress_damage(), progress_magic()]

currency = 0


def get_value(index): #während der spielererstellung anwenden, in factory aufrufen
    return progress_list[index].tier * progress_list[index].value


def print_current_unlocks():
    print()
    for item in progress_list:
        print(f"{item.name} +{item.tier * item.value}", end = " | ")
    print()
    print()



def print_available_unlocks():
    print()
    for item, counter  in enumerate(progress_list, start=1): 
        if item.tier >= 5:
            print (f"{counter}: {item.name} +{(item.tier +1) * item.value} (Max.)", end = " | ") # gerne bezeichnung max umändern
        else:
            print(f"{counter}: {item.name} +{(item.tier + 1) * item.value} ({item.cost * item.tier} Essence)", end = " | ")
    print()
    print()
    


def buy_upgrade(choice):
    if progress_list[choice].tier >= 5:
        print ("This upgrade is already maxed out.")
    elif (progress_list[choice].cost * progress_list[choice].tier) >= currency:
        progress_list[choice].tier += 1
        currency -= (progress_list[choice].cost * progress_list[choice].tier)
    else:
        print ("Not enough essence, please choose another upgrade.")
    
    




def select_menu():
    while True:
        choice = input("Insert '1' to see your current unlocks,'2' to see upgrades you can buy, or '3' to exit this menu: ")
        match choice:
            case "1":
                print_current_unlocks() # ggf noch anzeigen wennn ein upgrade auf max ist
            case "2":
                print_available_unlocks()
                choosen_upgrade = run.input_numbers(len(progress_list)) # da die existierende input funktion genutzt wird, ist es aktuell nicht möglich hier den direkten exit zu machen 
                buy_upgrade(choosen_upgrade)
            case "3":
                # save funktion einbauen ggf mit abfrage vorher
                break
            case _:
                print("Invalid Option, please try again.")
            



def upgrade_menu():
    print ("Here you can unlock permanent upgrades for your runs, with the currency you earned after won battles.")
    print (f"\nCurrently you have {currency} Essence to buy upgrades with.\n")
    select_menu()