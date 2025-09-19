import _sqlite3
import os


DB_PATH ='data/passwords.db' 


def safe_password():
    """Saves a password to the database."""
    conn = _sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('INSERT INTO passwords (password, key, App) VALUES (?,?,?)', (password, key, App))
    conn.commit()
    conn.close()
    

def output_password():
    """Outputs saved password from the database."""
    conn = _sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('SELECT * FROM passwords')
    conn.commit()
    conn.close()
    print(f"""✅ Passwort erfolgreich ausgegeben: {DB_PATH}""")
    
#TODO: Tests schreiben für die Funktionen