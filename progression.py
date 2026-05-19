class LevelSystem:
    def __init__(self):
        self.xp = 0
        self.level = 1

    def gain_xp(self, amount):
        self.xp += amount
        xp_amount_needed = 
        print(f"[XP] {self.xp} Nur noch {xp_amount_needed} bis zum nächsten Level")
        
        """Level 1 benötigt: 30xp
           Level 2 benötigt: 2 * 30xp = 60xp
           Level 3 benötigt: 3 * 30xp = 90xp
           ...
        """
        if self.xp >= self.level * 30:
            # (work in progress) xp von Spieler wird resettet mit jedem Levelup, also sollte die Anzahl die man kriegt am besten 15 oder 30 sein. 
            self.xp = 0
            self.level += 1
            print(f"LEVEL UP!!! Level {self.level}")
            
            # True, False Rückgabe für mögliche Funktion, die darauf basiert ob ein Levelup stattgefunden hat (z.B. Stat Upgrades)
            return True   # Levelup wurde gemacht
        return False    # Kein Levelup hat stattgefunden

