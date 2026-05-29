import dungeon
import player as pl # ja frag mich nicht, warum das jetzt so nötig war :)
import monster
import random
import time

# Später noch sleep() einbauen um die Ausgaben im Terminal etwas "natürlicher" zu machen

def select_opponent(dungeon_current):

    if 1 <= dungeon_current.current_battle <= 3:
        return random.choice([monster.goblin(), monster.slime()])
    
    if 4 <= dungeon_current.current_battle <= 6:
        return random.choice([monster.cavetroll(), monster.cliffracer()])
    
    if 7 <= dungeon_current.current_battle <= 9:
        return random.choice([monster.giant_mudcrab(), monster.basilisk()])
    


def input_numbers(length):
    while True:
        try:
            choice = int(input("Select one of the numbers: "))
            if 1 <= choice <= length:
                return choice
            else:
                print(f"Please select a number between 1 and {length}!")
        except ValueError:
            print(f"Please select a number between 1 and {length}!")



def print_battle_status(player, opponent):  # clear terminal noch einbauen? Gibt es eine Funktion die in allen gängigen Terminals funktioniert?
    
    print(f"\n{50*"-"}") # Lange Linie für die Optik
    print(f"{player.name} | HP: {player.hp}/{player.max_hp} | Mana: {player.mana}/{player.max_mana}") #Armor, Damage und Magic könnten noch angezeigt werden

    print(f"\n{opponent.name} | HP: {opponent.hp}/{opponent.max_hp}")
    print(f"{50*"-"}\n")
    time.sleep(1)



def print_spells(player):
    print()
    for counter, spell in enumerate(player.spell_list, start=1):   # durch enumerate wird gleichzeitig die liste durchgegangen und der zähler hochgezählt
        print(f"{counter}: {spell.name} +{spell.spell_level} [{spell.mana_cost}]", end=" | ") # sollte spätestens bei mehr als 6 spells in 2 zeilen kommen (verzweigung nutzen?)
    print()
    print()



def select_spell(player):

    while True:
        choice = input_numbers(len(player.spell_list))
        mana_check(player, choice)

        if  mana_check(player, choice) == True:
            return player.spell_list[choice-1]
        else: 
            print("Not enough Mana!")



def mana_check(player, choice):
    if player.spell_list[choice-1].mana_cost <= player.mana:
        return True
    else:
        return False



def victory_screen():
    time.sleep(1)
    print("\nThe dungeon grows silent...\n")
    time.sleep(2)
    print("-" * 40)
    print(12 * " " + "VICTORY ACHIEVED")
    print("-" * 40)
    print("\n")
    time.sleep(3)




def combat(player, opponent): 
    print(f"\nA {opponent.name} appeared. Prepare yourself!")
    print_battle_status(player, opponent) # inklusive sleep()   

    while True:

        print_spells(player)
        choice = select_spell(player)
        player.pay_mana(choice)
        choice.use_spell(player, opponent)  # spell.Spell.use_spell(choice, player, opponent) -> Macht an sich dasselbe, die aktuelle Lösung ist deutlich cleaner
        time.sleep(1) # kann auch in use_spell() rein
        print_battle_status(player, opponent)

        if opponent.hp <= 0:
            print(f"{opponent.name} was defeated!\n")
            return "Victory"
        else:
            selected = opponent.choose_spell()
            selected.use_spell(opponent, player)
            time.sleep(1)
            print_battle_status(player, opponent)

            if player.hp <= 0:
                print("You were defeated")
                return "Defeat"
            print("Next Turn!")   



def start_run():

    dungeon_current = dungeon.Dungeon(9) # Parameter bestimmt wie viele Kämpfe gespielt werden 
    player = pl.create_player()
    # Metaprogression laden

    while dungeon_current.current_battle < dungeon_current.total_battles:

        dungeon_current.current_battle += 1

        print("\nYou enter the next room...") # sollte noch alternative sätze bekommen
        time.sleep(2)
        opponent = select_opponent(dungeon_current)
        combat_result = combat(player, opponent)

        if combat_result == "Victory":
            player.reset_stats() # hier nach oder nach choose_upgrade() wäre ein clear terminal sinnvoll
            player.choose_upgrade()
            time.sleep(2)
        else:
            print(f"You delved too greedily and too deep... \nMaybe you will be luckier in your next life.")
            return #Status des runs könnte noch returnt werden

    victory_screen()   
    
           

            
         


        
