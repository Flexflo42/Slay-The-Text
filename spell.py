class Spell:
    def __init__(self, name, mana_cost, category, modifier):
        self.name = name
        self.spell_level = 1
        self.mana_cost = mana_cost
        self.modifier = modifier # Nutzbar für Buffs und Nerfs wie Rüstungsbrecher
        self.category= category

    def use_spell(self, user, target):
        
        print(f"{user.name} uses {self.name}!")
        # Kann weg, falls Combat Result als eigene Klasse implementiert werden sollte!

        if self.category == "attack":
            dmg = self.modifier * user.damage
            target.hp -= dmg
        
            print(f"{target.name} takes {dmg} damage!") # Temporär! Rüstung wird noch ignoriert

        elif self.category == "heal":
            heal_amount = self.modifier * user.magic
            user.hp += heal_amount

            print(f"{user.name} healed itself for {heal_amount} HP!")

        elif self.category == "damage_buff":
            user.damage += self.modifier

            print(f"{user.name} increased its damage by {self.modifier}!")

        elif self.category == "armor_debuff": #reduzierung jetzt prozentual
            armor_reduction = (target.armor * self.modifier)
            armor_reduction_int = int(armor_reduction)
            target.armor -= armor_reduction_int

            print(f"{user.name} reduced the armor from {target.name} by {armor_reduction_int}!")

        elif self.category == "armor_buff":
            user.armor += self.modifier

            print(f"{user.name} increased its armor by {self.modifier}!")


        # Anpassung wenn Spells mit neuen Effekten erstellt werden
        # Spells mit dem Monster Angriff dauerhaft erhöht zb oder starke Attacken mit Channeltime

tackle = Spell("Tackle", 10, "attack", 1)
bite = Spell("Bite", 10, "attack", 2)
slash = Spell("Slash", 25, "attack",3)
heal = Spell("Heal", 30, "heal", 1)
rage = Spell("Rage", 30, "damage_buff", 3)
armor_breaker = Spell("Armor Breaker", 20, "armor_debuff", 0.25)
armor_buff = Spell("Armor Buff", 20, "armor_buff", 3)


