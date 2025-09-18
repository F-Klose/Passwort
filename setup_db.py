import sqlite3
import os
DB_PATH =  os.path.join(os.path.dirname(__file__), 'data', 'passwords.db')




# hier wird geprüft ob datenbank vorhanden ist und wenn nicht wird sie 
def init_db():
    """
    Initialisiert die SQLite-Datenbank und erstellt die Tabelle für die Passwörter.
    Diese Funktion wird beim Start des Programms aufgerufen, um sicherzustellen,
    dass die Datenbank und die erforderlichen Tabellen vorhanden sind.
    Wenn die Tabelle bereits existiert, wird sie nicht erneut erstellt.
    Außerdem werden Einträge der passwörter mit ihren schlüsseln gesammelt.
    """
    #falls Db nicht da neue erstellen
    if not os.path.exists(DB_PATH):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS keys (
            Password TEXT PRIMARY KEY,
            Key TEXT NOT NULL,
            App TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print(f"✅ Datenbank erfolgreich initialisiert: {DB_PATH}")

#TODO: Tests schreiben für die Funktionen
#TODO: Funktion zum löschen der DB hinzufügen
#TODO: init_db() Zeile 36 - Funktion nicht mehr brauchbar - wie soll man damit umgehen?
#init_db()