class Spell:
    def __init__(self, name, mana_cost, category, modifier, spell_level=1):
        self.name = name
        self.mana_cost = mana_cost
        self.category= category
        self.modifier = modifier # Nutzbar für Buffs und Nerfs wie Rüstungsbrecher
        self.spell_level = spell_level
        # um spells exakt addressieren zu können, z.B. wenn man den Spellnamen zur Laufzeit ändern möchte können IDs hilfreich sein

    def use_spell(self, user, target):
        
        print(f"{user.name} uses {self.name}!")
        # Kann weg, falls Combat Result als eigene Klasse implementiert werden sollte!

        if self.category == "attack":
            value = self.modifier + (self.spell_level * 0.25) 
            dmg = value * user.damage
            reduced_dmg = dmg - (dmg * self.armor_calc(target))           
            reduced_dmg_int = round(reduced_dmg)
            target.hp -= reduced_dmg_int #wenn Zeit noch so polieren, dass die HP nicht unter 0 gehen kann
        
            print(f"{target.name} takes {reduced_dmg_int} damage!") 

        elif self.category == "heal":
            value = self.modifier + (self.spell_level * 0.25)
            heal_amount = self.modifier * user.magic
            heal_amount_int = round(heal_amount)

            if heal_amount_int + user.hp > user.max_hp:  #Damit die HP nicht durch Heilung über max_hp hinaus geht
                heal_amount_int = user.max_hp - user.hp
                user.hp += heal_amount_int                 #user.hp = user.max_hp alternativ möglich, dann aber zweite print funktion nötig
            else:
                user.hp += heal_amount_int

            print(f"{user.name} healed itself for {heal_amount_int} HP!")

        elif self.category == "damage_buff":
            value = self.modifier + (self.spell_level * 2) 
            user.damage += value 

            print(f"{user.name} increased its damage by {value}!")

        elif self.category == "armor_debuff": #reduzierung jetzt prozentual
            value = self.modifier + (self.spell_level * 0.10)
            armor_reduction = (target.armor * value)
            armor_reduction_int = round(armor_reduction)
            target.armor -= armor_reduction_int

            print(f"{user.name} reduced the armor from {target.name} by {armor_reduction_int}!")

        elif self.category == "armor_buff":
            value = round(self.modifier + (self.spell_level * 1.5))
            user.armor += value

            print(f"{user.name} increased its armor by {value}!")

        # Anpassung wenn Spells mit neuen Effekten erstellt werden

    def armor_calc(self, target):
        damage_reduction = target.armor / (target.armor + 15) #bei 15 armor ist die reduktion bei 50% -> deminishing returns
        return damage_reduction
    
    

        

# Bitte Helm tragen, ab hier beginnt die Factory-Straße

def slash(level=1):
    return Spell("Slash", 10, "attack", 0.75, level)

def bite(level=1):
    return Spell("Bite", 20, "attack", 1.25, level)

def power_slash(level=1):
    return Spell("Power Slash", 30, "attack", 20.25, level)

def heal(level=1):
    return Spell("Heal", 30, "heal", 0.75, level)

def rage(level=1):
    return Spell("Rage", 20, "damage_buff", 8, level)

def crush_armor(level=1):
    return Spell("Crush Armor", 20, "armor_debuff", 0.25, level)

def armor_spell(level=1):
    return Spell("Armor Spell", 20, "armor_buff", 2.5, level)

# Player und Monster erhalten so seperate Objekte die individuell angepasst werden können -> SpellUpgrades









