import spell
import random
import spellupgrade


class Player:
    def __init__(self, name, max_hp, hp, max_mana, mana, damage, magic, armor, spell_list):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.max_mana = max_mana
        self.mana = mana
        self.damage = damage
        self.damage_default = damage
        self.magic = magic
        self.magic_default = magic
        self.armor = armor
        self.armor_default = armor
        self.spell_list = spell_list


    def choose_upgrade(self): # 
        valid_list = []

        for spell in self.spell_list:
            if spell.spell_level < 5:
                valid_list.append(spell)

        selection = random.sample(valid_list, min(len(valid_list), 3 )) #Es werden aus der Liste 3 Elemente gewählt, oder weniger wenn die liste kürzer ist

        #print(selection[0].name) # test
        #print(len(selection)) # test
        
        upgrade_list = []
        
        for spell in selection:   # Objekte der Klasse SpellUpgrade werden erzeugt und in einer Liste gespeichert (Zugriff über Index)
            upgrade = spellupgrade.upgrade(spell.name, spell.spell_level)
            upgrade_list.append(upgrade)

        #print(len(upgrade_list))  # test
        #print(upgrade_list[2].name) # test
        
        print(f"You can upgrade one of your spells. Choose wisely:")
        counter = 0
        for upgrade in upgrade_list:
            counter +=1
            result = spellupgrade.rarity_calculation()

            if result == "epic":
                if upgrade.spell_level <= 2: # Aktuell hat man einfach Pech gehabt, wenn eine zu hohe Fähigkeit ein epic upgrade bekommen würde, ggf noch anpassen
                    upgrade.level_up = 3
                    upgrade.rarity = "epic"
                    
                    print(f"{counter}: Epic Upgrade! '{upgrade.name}' for {upgrade.level_up} levels")

            elif result == "rare":
                if upgrade.spell_level <= 3:
                    upgrade.level_up = 2
                    upgrade.rarity = "rare" 
                
                    print(f"{counter}: Rare Upgrade! '{upgrade.name}' for {upgrade.level_up} levels")             
            else:
                print(f"{counter}: '{upgrade.name}' for {upgrade.level_up} level")
        
        while True:
            try:
                choice = int(input("Select one of the numbers: "))

                if 1<= choice <= min(3, len(upgrade_list)): # Wenn die Liste nur noch zwei oder weniger Elemente hat darf 2 oder 3 nicht gewertet werden
                    self.level_up(upgrade_list[choice-1].name, upgrade_list[choice-1].level_up)
                    
                    break
                else: 
                    print(f"Please select a number between 1 and {len(upgrade_list)}!") # Erster Edge Case: Falscher int eingegeben


            except ValueError:
                print(f"Please select a number between 1 and {len(upgrade_list)}!") # Zweiter Edge Case: Kein int eingegeben



    def level_up(self, name, level_up):
        for spell in self.spell_list:
            if name == spell.name:
                spell.spell_level += level_up
                print(f"{spell.name}:+{spell.spell_level - level_up} got upgraded to {spell.name}:+{spell.spell_level}")
                #print(spell.name, spell.spell_level) # test


    def pay_mana(self, spell):
        self.mana -= spell.mana_cost


    def reset_stats(self):
        self.hp = self.max_hp
        self.mana = self.max_mana
        self.armor = self.armor_default
        self.damage = self.damage_default
        self.magic = self.magic_default


def create_player():
    return Player("Player", 100, 100, 100, 100, 20, 20, 5,
            [spell.slash(), spell.power_slash(), spell.heal(), spell.armor_spell(), spell.crush_armor(), spell.rage()])
    


        