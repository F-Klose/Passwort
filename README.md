---
marp: true
---
# Mini Projekt Password generator 
Agenda : 
1. was ist das Projekt
2. wie soll es fuktionieren 
3. was haben wir bisher 
4. was fehlt noch 
5. fazit 

---
1. Projekt Password was ist das ?

- ein kleines programm das passörter generirt 
- die passwörter verschlüsselt
- die passwörter und die schlüssel speichert speichert 
- eine funktion die bei bedarf die passwörter entschlüsselt 
- eine main die alles zusammen führt 
- eine flask api
---

2. wie ist der Plan
- der plan war eine generirung von passwörtern die in einer datendank gespeichert werden um sie
         einigermaßen sicher zu speichern haben wir uns daführ entschieden eine verschlüsselung 
         einzu bezihen damit das nicht den zeit rahmen sprengt haben wir dafür eine erweiterte cesar
        verschibung verwendet den schlüssel wollten wir mit einer einfach matematischen operation selber auch unklar in die datenbank bringen (z.b. alle schlüssel werden mit + 3 gespecihert und bei abrufen mit - 3 )

---
3. Was haben wir bisher 

- wir können paswörter erstellen 
- wir können ver und entschlüsseln 
- wir inizialisiren die DB automatisch wen nicht vorhaneden 
- wir haben eine main.py die die ersten funktionen zusammen führt 
- wir haben eine readme die unser projekt vorstellt 
---
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
---
4. Was haben wir noch nicht geschafft:

- unsere main muss fertig gestellt werden 
- die funktionen muessen angebasst werden das der schlüssel(unklar) gespeichert wird und der anwendungsfall
- die passwort ausgabe und die entschlüsselung muss noch so angepasst werden das der schluessel unklar
    bleiben kann 


---

5. fazit:
- arbeit am Projekt
- projekt zukunft 
- projekt abschluss 

---

zusatz :

das projekt ist  in einer rudimentären version erreich bar unter :

-> https://passwort.onrender.com/api/helloworld <-

---



Website-Deployment:
--> https://passwort.onrender.com
--> Pfad anhängen: /api/helloworld



