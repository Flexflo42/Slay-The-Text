import random
rarity_chance = 20


class SpellUpgrade:
    def __init__(self, name, spell_level, level_up=1, rarity="common"):
        self.name = name
        self.spell_level = spell_level
        self.level_up = level_up
        self.rarity = rarity







def rarity_calculation(): # Wenn ein Wert zwischen 1 und 100, gleich oder geringer als 20 ist wird das Upgrade verstärkt, aka 20% Wahrscheinlichkeit
    value = random.randint(1, 100) # is en bissel komisch aber geht
    if value <= rarity_chance // 3:
        return "epic"
    elif value <= rarity_chance:
        return "rare"
    else:
        return "common"


    



def upgrade(name, spell_level): # Factory Funktion
    return SpellUpgrade(name, spell_level)







    

# level_up_normal = SpellUpgrade ("Level Up +1", 1)
# level_up_rare = SpellUpgrade ("Level Up +2", 2)
# level_up_epic = SpellUpgrade ("Level Up +3", 3)


