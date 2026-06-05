

class Progress:
    def __init__(self, name, value, cost, tier=0):
        self.name = name
        self.value = value
        self.cost = cost
        self.tier = tier











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

