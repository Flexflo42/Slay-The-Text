Metawährung: Seelen/Essenz
Upgradeliste
-> beide sind persistente Daten, sie bleiben über runs hinaus erhalten (CSV-Datei)
-> ggfs ist JSON besser geeignet, da objektstrukturen genutzt werden können

Nach jedem besiegten Gegner +1 Metawährung \* Gegnerstufe
### Upgradeliste
-> maximal 5 Arten in 3-5 Stufen

- HP: +5,10,15,20,25
- Mana: +5,10,15,20,25
- Armor: +1,2,3,4,5
- Damage (Physical): +1,2,3,4,5
- Damage (Magical) +1,2,3,4,5 (beinflusst heilung?)

- Mehr währung +1,2
- höhere wahrscheinlichkeit für bessere upgrades + 10, 20, 30, 40, 50 %

### Ablauf

**Spielstart**
- CSV lesen
- Werte in Variablen/Objekte laden
**Run spielen**
- Werte beeinflussen das Gameplay
**Nach dem Run**
- Währung hinzufügen
- evtl. Upgrade kaufen
**Speichern**
- neue Werte zurück in CSV schreiben

-> Upgrade Menü eigener Punkt neben "neuen Run starten"
? wie das Gameplay beinflussen, Werte direkt in Spielerklasse schreiben?
? Wann genau speichern, und wann Werte neu reinladen zb nach Runstart

### Klassenstruktur
Währung und Upgradeliste in Klassen
ggfs zwei klassen: upgradeshop und metaprogression

