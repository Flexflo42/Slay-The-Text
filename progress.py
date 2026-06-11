import run

class Progress:

    def __init__(self, name, value, cost, tier=0):
        self.name = name
        self.value = value
        self.cost = cost
        self.tier = tier
        # max tier/level als attribut einfügen bei optionen die weniger als 5 upgrade haben -> funktionen anpassen

class Progress_System: # eine klasse für ein objekt um die währung und die liste für die upgrades zu halten

    def __init__(self, progress_list, currency = 0):
        self.progress_list = progress_list
        self.currency = currency


    def get_value(self, index): #während der spielererstellung anwenden, in factory aufrufen. Der Wert mit dem zb die HP zum Start zusätzlich erhöht wird
        return self.progress_list[index].tier * self.progress_list[index].value 


    def print_current_unlocks(self):
        print()
        for item in self.progress_list:
            print(f"{item.name} +{item.tier * item.value}", end = " | ")
        print("\n\n")


    def print_available_unlocks(self):
        print()
        for counter, item in enumerate(self.progress_list, start=1): # Bei enumerate muss der Index (hier counter) immer zuerst genannt werden, Dadurch kann die listenposition mitangezeigt werden
            if item.tier >= 5:
                print (f"{counter}: {item.name} +{(item.tier) * item.value} (Max.)", end = " | ") # gerne bezeichnung max umändern
            else:
                print(f"{counter}: {item.name} +{(item.tier + 1) * item.value} ({item.cost * (item.tier +1)} Essence)", end = " | ") # +1 damit Kosten/Wert der zu kaufenden stufe angezeigt werden
        print("\n")
        print(f"You have {self.currency} Essence to buy upgrades with.")
        print()

    
    def buy_upgrade(self, choice):
        choice -= 1                                    # Damit der richtige Index der Liste angesprochen wird
        if self.progress_list[choice].tier >= 5:
            print ("This upgrade is already maxed out.")

        elif (self.progress_list[choice].cost * (self.progress_list[choice].tier + 1)) <= self.currency:
            self.currency -= (self.progress_list[choice].cost * (self.progress_list[choice].tier + 1))
            self.progress_list[choice].tier += 1

        else:
            print ("Not enough essence, please choose another upgrade.")



#Factory Functions

def progress_hp():
    return Progress ("HP", 10, 2)

def progress_mana():
    return Progress ("Mana", 10, 2)

def progress_damage():
    return Progress ("Damage", 3, 2)

def progress_magic():
    return Progress ("Magic", 3, 2)

def progress_armor():
    return  Progress ("Armor", 1, 2)


def progress_player(currency = 0):
    return Progress_System (
        [progress_hp(),
        progress_mana(),
        progress_damage(),
        progress_magic(),
        progress_armor()], currency
    )

progress_status = progress_player(10) # default value 0



def upgrade_menu():
    print ("Here you can unlock permanent upgrades for your runs, with the currency you earned after won battles.")
    print ()
    select_menu()


def select_menu():
    while True:
        choice = input("Insert '1' to see your current unlocks,'2' to see upgrades you can buy, or '3' to exit this menu: ")
        match choice:
            case "1":
                progress_status.print_current_unlocks() # ggf noch anzeigen wennn ein upgrade auf max ist
            case "2":
                shop()  
            case "3":
                # save funktion einbauen ggf mit abfrage vorher
                break
            case _:
                print("Invalid Option, please try again.")
            

def shop():
    while True:
        progress_status.print_available_unlocks()
        choosen_upgrade = run.input_numbers(len(progress_status.progress_list), 1) # da die existierende input funktion genutzt wird, ist es aktuell nicht möglich hier den direkten exit zu machen 
        if choosen_upgrade <= 0:
            return
        else:
            progress_status.buy_upgrade(choosen_upgrade)

