import spell
import random

class Monster:
    def __init__(self, name, pool, max_hp, hp, damage, magic, armor, initiative, behavior, spell_list):
        self.name = name
        self.pool = pool
        self.max_hp = max_hp
        self.hp = hp
        self.damage = damage
        self.magic = magic
        self.armor = armor
        self.initiative = initiative
        self.behavior = behavior
        self.spell_list = spell_list # skills als Liste hinzufügen
        self.turn_counter = 0  # ist das nötig, ggf im Combatloop nutzen

    def choose_spell(self):
       #könnte im aktuellen Zustand auch zusammengefasst werden zb durch AND verknüpfungen, so kann das
       #verhalten aber ggf. noch stärker individualsiert werden

        if self.behavior == "random":
            return random.choice(self.spell_list)
        elif self.behavior == "aggresive": #jeder zweite Angriff ist besonders stark
            if self.turn_counter % 2 == 0:
                return self.spell_list[0]
            else:
                return random.choice(self.spell_list[1:7])
        elif self.behavior == "defensive": #Jeder dritte spell erhöht die rüstung
            if self.turn_counter % 3 == 0:
                return self.spell_list[0]
            else:
                return random.choice(self.spell_list[1:7])
        elif self.behavior == "healer": #anpassen?
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



        
    


goblin = Monster ("Goblin", 1, 50, 50, 10, 10, 5, 50, "random", spell_list=[Spell("Tackle"),Spell("Heal")])
                  #spell_list =[spell.tackle, spell.heal])
# slime = #healer
# cliffracer = #aggresive
# cavetroll = #furious
# giantMudcrab =#defensive
# serpent= #armorbreaker

# print (spell.tackle.name) 
# print (type(slime.spell_list))


print (goblin.choose_spell())

print (goblin.spell_list)