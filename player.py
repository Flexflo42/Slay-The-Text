class Player:
    def __init__(self, name, hp, phy_damage):
        self.name = name
        self.hp = hp
        self.phy_damage = phy_damage
        self.spell_list = [] # muss irgendwie gefüllt werden


    def upgrade_skill(self, spell_name):
        # spell mithilfe des Namens upgraden
        for spell in self.spell_list:
            if spell.name = spell_name:
                spell.spell_level += 1
                print(f"{spell.name} ist jetzt Level {spell.spell_level}")
                return
        print(f"Zauber '{spell_name} nicht gefunden")

        