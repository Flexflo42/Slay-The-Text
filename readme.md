# Dokumentation

Eine umfassende Projektdokumentation inklusive Spielanleitung befindet sich in der PDF "Dokumentation" im Ordner "Dokumentation". 

# Installation
Ein Python Virtual Environment muss aktiviert werden, um einen Ort zu haben, an dem Pakete isoliert vom System (also auch anderen Projekten) installiert werden können.

## Linux

Erstellen:
```python3 -m venv myvenvname```

Navigieren:
```source myvenvname/bin/activate``` 

Sobald man im Virtual Environment ist kann man mit Python's Packetmanager 'pip' das Paket installieren
```pip install pygame```

Wenn VSCode oder ähnliches sich über ein fehlendes Modul beschwert, ist wahrscheinlich der Python Interpreter falsch ausgewählt. Der Interpreter kann manuell im CLI übergeben werden.
```Interpreter Probleme : ./myvenvname/bin/python main.py (oder andere Datei, die ausgeführt werden soll)```

Deaktivieren:
```deactivate```


## Windows
Navigieren Sie in der cmd.exe oder Powershell in den Projektordner

Erstellen:
```python3 -m venv myvenvname```

Aktivieren:
In cmd.exe
```myvenvname\Scripts\activate.bat```
In PowerShell
```myvenvname\Scripts\Activate.ps1``` 

Sobald man im Virtual Environment ist kann man mit Python's Packetmanager 'pip' das Paket installieren
```pip install pygame```

Wenn VSCode oder ähnliches sich über ein fehlendes Modul beschwert, ist wahrscheinlich der Python Interpreter falsch ausgewählt. Der Interpreter kann manuell im CLI übergeben werden.
```Interpreter Probleme : myvenvname\Scripts\python.exe main.py (oder andere Datei, die ausgeführt werden soll)```

Deaktivieren:
```deactivate```