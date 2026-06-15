import spell
import random

class Monster:

    def __init__(self, name, pool, max_hp, hp, damage, magic, armor, behavior, spell_list):
        self.name = name
        self.pool = pool
        self.max_hp = max_hp
        self.hp = hp
        self.damage = damage
        self.magic = magic
        self.armor = armor
        self.behavior = behavior
        self.spell_list = spell_list # skills als Liste hinzufügen
        self.turn_counter = 0 

    def choose_spell(self):
       #könnte im aktuellen Zustand auch zusammengefasst werden zb durch AND verknüpfungen, so kann das
       #verhalten aber ggf. noch stärker individualsiert werden
        self.turn_counter += 1

        if self.behavior == "random":
            return random.choice(self.spell_list)
        elif self.behavior == "agressive": #jeder zweite Angriff ist besonders stark
            if self.turn_counter % 2 == 0:
                return self.spell_list[0]
            else:
                return random.choice(self.spell_list[1:7])
        elif self.behavior == "defensive": #Jeder dritte spell erhöht die rüstung
            if self.turn_counter % 3 == 0:
                return self.spell_list[0]
            else:
                return random.choice(self.spell_list[1:7])
        elif self.behavior == "healer": #jeder zweite spell healt
            if self.turn_counter % 2 == 0:
                return self.spell_list[0]
            else:
                return random.choice(self.spell_list[1:7])
        elif self.behavior == "furious": #Jeder zweite spell erhöht den Schaden dauerhaft
            if self.turn_counter % 2 == 0:
                return self.spell_list[0]
            else:
                return random.choice(self.spell_list[1:7])
        elif self.behavior == "armorbreaker": #der erste angriff zerstört rüstung, der dritte schallert
            if self.turn_counter % 3 == 1:
                return self.spell_list[0]
            elif self.turn_counter % 3 == 0:
                return self.spell_list[1]
            else:
                return random.choice(self.spell_list[2:7])

# die gegner im 2. oder 3. Pool könnten Fähigkeiten mit höheren Stufen bekommen, besonders bei skills die nicht mit den stats skalieren
# spell factories müssen dann Parameter erhalten können, über einen weiteren paramter könnte auch der Name des Skills angepasst werden

def goblin():
    return Monster ("Goblin", 1, 50, 50, 15, 10, 5, "random", spell_list =[spell.slash(), spell.bite(), spell.heal()])

def slime():
    return Monster ("Slime", 1, 120, 120, 15, 15, 5, "healer", [spell.heal(), spell.slash(), spell.bite(), spell.armor_spell()])

def cliffracer():
    return Monster ("Cliffracer", 2, 120, 120, 15, 15, 5, "agressive", [spell.power_slash(), spell.slash(), spell.armor_spell(), spell.crush_armor()])

def cavetroll():
    return Monster ("Cavetroll", 2, 150, 150, 20, 15, 7, "furious", [spell.rage(), spell.slash(), spell.bite(), spell.crush_armor()])

def giant_mudcrab():
    return Monster ("Giant Mudcrab", 3, 200, 200, 25, 30, 10, "defensive", [spell.armor_spell(), spell.slash(), spell.bite(), spell.heal()])

def basilisk():
    return Monster ("Basilisk", 3, 200, 200, 30, 30, 7, "armorbreaker", [spell.crush_armor(), spell.power_slash(), spell.slash(), spell.heal(), spell.rage()])


# Bossgegner fehlt noch, ggf in eigene Klasse die von Monster erbt






