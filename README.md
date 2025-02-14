# Willkommen System 2.0

## Überblick
Das **Willkommen System 2.0** ist ein Discord-Bot, der neue Mitglieder automatisch begrüßt. Er sendet eine Willkommensnachricht in einen vordefinierten Kanal und eine Direktnachricht mit weiteren Informationen und Links zur Server-Einweisung.

## Funktionen
- Automatische Begrüßung neuer Mitglieder mit einer Willkommensnachricht im Server-Kanal.
- Versand einer Direktnachricht mit wichtigen Informationen und Links.
- Einbindung eines Bildes in die Willkommensnachricht.
- Zählung der Server-Mitglieder.
- Bereitstellung eines Regelbestätigungsprozesses mit einem PIN-Code.

## Voraussetzungen
- Ein Discord-Bot-Token
- Die `discord.py`-Bibliothek (Async-Version)
- Die ID des Willkommenskanals
- Eine Bilddatei für die Begrüßung

## Installation
1. Stelle sicher, dass Python (Version 3.8 oder höher) installiert ist.
2. Installiere die `discord.py`-Bibliothek mit folgendem Befehl:
   ```sh
   pip install discord
   ```
3. Füge den Bot zu deinem Discord-Server hinzu und aktiviere `Intents`.

## Einrichtung
1. Ersetze `TOKEN_HIER` in der Datei durch deinen Bot-Token.
2. Setze die `WELCOME_CHANNEL_ID` auf die ID deines gewünschten Willkommenskanals.
3. Speichere das gewünschte Begrüßungsbild unter dem in `IMAGE_FILE_NAME` angegebenen Namen.
4. Starte den Bot mit:
   ```sh
   python bot.py
   ```

## Anpassung
- Du kannst den Begrüßungstext oder die eingebundenen Links direkt im Code anpassen.
- Falls du einen anderen Befehlsprefix verwenden möchtest, ändere `command_prefix="!"` in eine andere Zeichenfolge.

## Fehlerbehebung
Falls der Bot nicht funktioniert:
- Stelle sicher, dass der Bot die richtigen Berechtigungen hat.
- Überprüfe, ob die Kanal-ID und der Bot-Token korrekt sind.
- Falls das Bild nicht gesendet wird, stelle sicher, dass es sich im richtigen Verzeichnis befindet.

## Lizenz
Dieses Projekt steht unter der MIT-Lizenz.
