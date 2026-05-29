### Installation
Ein Python Virtual Environment muss aktiviert werden, um einen Ort zu haben, an dem Pakete isoliert vom System (also auch anderen Projekten) installiert werden können.
```python3 -m venv myvenvname```
```source myvenvname/bin/activate``` 

Sobald man im Virtual Environment ist kann man mit Python's Packetmanager 'pip' das Paket installieren
```pip install pygame```

Wenn VSCode oder ähnliches sich über ein fehlendes Modul beschwert, ist wahrscheinlich der Python Interpreter falsch ausgewählt. Der Interpreter kann manuell im CLI übergeben werden.
```Interpreter Probleme : ./myvenvname/bin/python main.py (oder andere Datei, die ausgeführt werden soll)```