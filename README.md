
# Mini-Projekt: Password Generator

**Agenda:**

1. Projektüberblick
2. Funktionsweise
3. Aktueller Stand
4. Offene Punkte
5. Fazit & Ausblick

---

## 1. Projektüberblick

* Entwicklung eines kleinen Programms zur **Passwortgenerierung**.
* **Verschlüsselung** der Passwörter zur sicheren Speicherung.
* Speicherung von Passwörtern und zugehörigen Schlüsseln in einer Datenbank.
* Möglichkeit zur **Entschlüsselung** bei Bedarf.
* Eine zentrale `main.py` verbindet alle Funktionen.
* Bereitstellung über eine **Flask-API** für Webzugriff.

---

## 2. Funktionsweise

* Passwörter werden generiert und in einer Datenbank gespeichert.
* Zur Sicherheit werden die Passwörter mit einer **erweiterten Caesar-Verschlüsselung** verschlüsselt.
* Schlüssel werden vereinfacht „maskiert“ gespeichert (z. B. durch einfache mathematische Operationen wie +3 beim Speichern und -3 beim Abrufen).
* Ziel: Praktische Sicherheit innerhalb eines überschaubaren Projektumfangs.

---

## 3. Aktueller Stand

* Passwörter können generiert, verschlüsselt und entschlüsselt werden.
* Die Datenbank wird bei Bedarf automatisch initialisiert.
* `main.py` verbindet die Grundfunktionen.
* Projekt-README dokumentiert Aufbau und Funktionen.

```python
def decryption(text, shift):
    text = text.lower()
    text = text.replace("ä", "ae").replace("ü", "ue").replace("ö", "oe")
    result = []
    for idx, char in enumerate(text):
        if char.isalpha():
            shift_base = ord('a')
            actual_shift = -shift if idx % 2 == 0 else shift
            new_char = chr(((ord(char) - shift_base + actual_shift) % 26) + shift_base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)
```

---

## 4. Offene Punkte

* Fertigstellung und Optimierung der `main.py`.
* Anpassung der Funktionen zur **sicheren und unklaren Speicherung der Schlüssel**.
* Optimierung der Passwortausgabe und Entschlüsselung, sodass die Schlüssel weiterhin verborgen bleiben.

---

## 5. Fazit & Ausblick

* Grundlegende Funktionen sind implementiert.
* Das Projekt bietet Potenzial für **erweiterte Sicherheitsfeatures** und eine umfassendere API.
* Ziel: Abschluss des Projekts nach Umsetzung der offenen Punkte und stabiler Webintegration.

---

## Zusatzinformationen

* **Rudimentäre Version verfügbar unter:**

  * API: [https://passwort.onrender.com/api/helloworld](https://passwort.onrender.com/api/helloworld)
  * Website: [https://passwort.onrender.com](https://passwort.onrender.com)

---
