# Maexchen Python WPF

This is a school project for the Python WPF. It's the game the bar dice game Maexchen implmented in Python with Pygame


## Requirements
pygame <br>
Python 3.11


## Installation
```shell
git clone https://github.com/dreace1/maexchen.git
pip install pygame
cd maexchen
```

## Run 
### Frontend
```shell
python maexchen_view.py
```
### Backend
```shell
python maexchen_logic.py
```

## Dokumentation (German):
Als Projekt wurde von uns das Würfelspiel [Maexchen](https://de.wikipedia.org/wiki/Mäxchen) ausgewählt.

### Durchführung
Wir haben uns dazu entschieden, mit der pygame Library zu arbeiten, da diese bereits viele Funktionen bietet um Spiele in python zu Implementieren.

### Aufteilung
Wir haben das Projekt in Frontend und Backend aufgeteilt. Dabei hat sich Hannes um das Frontend gekümmert und Leon um das Backend.

### Probleme
Leider war es anfangs nicht so trivial die Library zu verwenden. Deswegen ist der momentane Stand noch nicht final. Das Frontend und das Backend muss noch verbunden werden. Außerdem fehlt bspw. eine Highscore Tabelle und Spielerwahl.

### Frontend
Wenn man das Spiel startet landet man direkt im Spiel, um zu Würfeln muss die Leertaste gedrückt werden. Daraufhin startet eine Animation und es werden zwei Würfelergebnise angezeigt.

### Modul Aufteilung
Frontend Module sind mit den Suffix `_view` und Backend Module mit dem Suffix `logic` aufgeteilt.

### ToDo
- Frontend mit Backend verbinden
- Spiel starten Menu mit Spieler wahl (Name usw.)
- Highscore Liste -> DB Anbindung/JSON Datei
- Refactoring
- Spiel Flow: Runden, Wechsel des Spielers, Punktevergabe, Gewinner
- Animation des Würfelns ggf. noch verbessern
- Unit Testing