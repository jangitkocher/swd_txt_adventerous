# Text Adventure
Final assignment of the Modul "Software Design"

## Start the application
```bash
docker-composse up -d
pip install -r requirements.txt
python app/main.py
```

## General

## Requirements
Mit der Rolle des (unregistrieten) Benutzers, Spielers und registrierten Benutzers sind sowohl männliche, weibliche als auch divers Personen gemeint.

Aufgabe Text Adventure:

Zum gemütlichen Zeitvertreib soll es eine Text Adventure App geben, bei der man sich als Spieler auf einer Karte bewegen kann.

Innerhalb der App gibt es drei Rollen, der Benutzer, der Spieler und der registierte Benutzer.

Beim Starten der Applikation gibt es mehrere Möglichkeiten:

- Der Benutzer, kann nach einem Text Adventure anhand des Titels suchen.
- Der Benutzer, kann sich eine Übersicht der Text Adventures anzeigen lassen, immer nur 5 gleichzeitig.
--- Vielleicht eine Funktion danach die nächsten 5 Text Adventures zu sehen.
--- In der Übersicht soll ebenfalls ersichtlich sein, wie groß die Karte ist, bspw.: (6 x 9 Felder)
- Der aktuelle Benutzer, kann sich Anmelden mit Benutzername und Passwort.
- Der aktuelle Benutzer, kann sich registrieren.
--- Falls der Benutzer, bereits registriert ist anhand des Benutzernamen, soll es nicht möglich sein, sich nochmals mit dem gleichen Benutzernamen registieren zu können.

Bei der Registrierung ist es erforderlich einen Benutzernamen (alphanumerisch, keine Sonderzeichen) und ein Passwort anzugeben.
Registrierte Benutzer werden dann entsprechend persistiert.
Nochmals: Ein bereits registrtierten Benutzer kann sich nicht nochmals Registrieren.

Mit dem Benutzernamen und Passwort kann sich ein registrierter Benutzer anmelden.
Entsprechende Sicherheitsvorkehrungen, dass das Passwort nicht sichtbar ist, usw... sind nicht erforderlich, aber gewünscht. Stichwort hierbei: bspw. Hashing Sha256

Sobald der Benutzer ein Text Adventure ausgesucht hat, wird er automatisch zum Spieler.
Das Text Adventure startet am definierten Startpunkt des Spiels, der aktuelle Standort wird ausgegeben, z.B.

Spiel startet...
Du befindest dich am Alexanderplatz.

Danach bekommt der Spieler die Möglichkeit in eine Himmelsrichtung zu gehen, die Art und Weise wie er dies tut ist euch überlassen.
Nach Auswahl einer Himmelsrichtung wird der Spieler zum neuen Standort geführt und der Standort wird ausgegeben, bspw.:
Du bist nach Osten gelaufen und befindest dich am Brandenburger Tor.

Sobald der Spieler am Rand der Karte angekommen ist, kann dieser nicht mehr in die Richtung laufen und es soll entsprechend ausgegeben werden, bspw.:
Du bist am Rand angekommen und kannst nicht in die Himmelsrichtung laufen.

Das Spiel würde endlos so weitergehen, allerdings hat der Spieler immer die Möglichkeit das Spiel zu beenden und kommt wieder auf den Anfangsbildschirm.

Der registierte Benutzer hat erstmal die gleichen Möglichkeiten wie der unregistriete Benutzer außer Registrieren und Anmelden.

Zu dem kann dieser ein Text Adventure Spiel anlegen und dieses definieren.
Dabei gibt dieser zu erstmal den Titel des Spiels und die Größe der Karte an.

Die Größe der Karte berechnet sich aus einem X mal Y Feld, bspw. (3 mal 4 Felder), bedeutet 3 Feld breit 4 Felder hoch, insgesamt 12 Felder.
Danach wird der Startpunkt des Spielers bestimmt, bspw. (1 / 1), bedeutet links oben, in Himmelsrichtung Norden und Westen befinden sich Ränder.

Danach müssen die einzelnen Standort der einzelnen Koordinaten eintragen werden, bspw.:
- (1/1) - Alexanderplatz
- (1/2) - Brandenburger Tor
- (1/3) - Reichstag
....
- (3/4) - Tiergarten

Sobald alle Koordinaten eintragen sind, kann der registierte Benutzer das Text Adventure freigeben.
Lasst bei der Erstellung einer Karte eurer Kreativität freien Lauf, auch was das User Interface nachher betrifft.
Stellt die Karte vielleicht grafisch dar, die Beispiele sollen lediglich als Beispiele dienen und sind nicht verpflichtend.

Wichtig, innerhalb des Programmcodes oder innerhalb der Datenlogik muss hinterlegt sein, welche Koordinate neben welcher anderen Koordinate liegt.

Als letztes hat der registierte Benutzer die Möglichkeit Statistiken zu seinen Text Adventures einzusehen.
Dieser soll die Möglichkeit erhalten zu sehen, wie viele Spieler sein Text Adventure schon gespielt haben und 
wie viele Züge, also Auswählen einer Himmelsrichtung, diese durchschnittlich auf seiner Karte verbracht haben.
