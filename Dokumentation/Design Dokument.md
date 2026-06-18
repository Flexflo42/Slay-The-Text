**MVP:**
Terminal-based Rogue-lite mit rundenbasierten Kämpfen
Ein Spielcharakter gegen ein bis drei Gegner
Nach jedem erfolgreichen Kampf Auswahl von 1 aus 3 Belohnungen
Jeder Erfolgreicher Kampf gewährt Metawährung (Essenz).
Essenz zur Freischaltung von dauerhaften Upgrades in einem eigenen Menü -> vor bzw. nach Run -> Essenz und Upgrades müssen gespeichert werden (CSV, JSON)
Begrenzung auf max. 6 Stats für Spieler und Gegner
Gegner werden zufällig gewürfelt aus 3 Pools (jeder Pool ist stärker)
Gegner wählt (vorerst) zufällig eine seiner 4 Fähigkeiten
Max 10 Gegnertypen
Spieler kann aus vorerst 4 Fähigkeiten auswählen
Kampfergebnisse werden im Terminal angezeigt
Mana und HP werden (vorerst) nach jedem Kampf wiederhergestellt

**Nicht Teil des MVPs:**
Weitere Encounter wie Händler
Nutzbare Items wie Tränke
Spezielle Mana Mechaniken (Mana regeniert nicht automatisch dafür managenerierende Fähigkeiten)
Overload / Ultimative Fähigkeiten
Erwerbare Fähigkeiten / Spells
Boss Gegner mit Mechaniken
Weitere spielbare Charaktere
Statuseffekte wie Gift, Blutung etc.

### Spells
-> eine Klasse für Spieler und Monster (mit default Werten arbeiten, ggfs auch mit args und kwargs)
-> wie mit Mana umgehen? Aktuell Monster kein Mana stat aber selber skill pool

**Must have:**
Einfacher Angriff: Damage * Damagestat
Einfache Heilung: Heilwert oder prozentual von HP
-> Bei Spieler mit Magic Wert skalieren
Perma Dmg Buff: Damagestat + Buff
Rüstung reduzieren: targetarmor - Wert
-> mit Angriff kombinieren?

**Optional:**

Stun /Betäubung (Trefferwahrscheinlichkeit? / hohe Manakosten): Target 1/2 Runden keine Spells
Sehr starker Angriff mit Channeltime: 1 oder 2 Runden warten = Nuke (unterbrechbar?)

### Monster

? Mehrere Monsterpools um ansteigenden Schwierigkeitsgrad zu erreichen:
-> Kämpfe 1-3 Pool 1, Kämpfe 4-6 Pool 2, etc
