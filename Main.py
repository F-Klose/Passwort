# Führt alle Funktionen für einen nahtlosen Demonstrationslauf zusammen.
# Das Skript generiert ein Passwort, verschlüsselt, speichert,
# ruft es ab, entschlüsselt es und gibt die Ergebnisse aus.
import setup_db
import encryption
import decryption
from utils import safe_password ,output_password
import generate_random_password

def main():
    """Führt den kompletten Ablauf zur Demonstration in einem Schritt durch."""
    
    # Datenbank-Setup wird als erster Schritt automatisch ausgeführt
    setup_db.init_db()
    
    # Schritt 1: Passwort generieren
    new_password = generate_random_password.generate_random_password(8)
    print("Passwort wurde generiert.")
    print("Generiertes Passwort:", new_password)

    # Schritt 2: Benutzerinput für Schlüssel und Anwendungsfall
    try:
        key = int(input("Bitte geben Sie einen Schlüssel (Zahl) für die Verschlüsselung ein: "))
        anwendungsfall = input("Bitte geben Sie den Anwendungsfall für das Passwort ein (z.B. 'Login'): ")
    except ValueError:
        print("Fehler: Der Schlüssel muss eine ganze Zahl sein. Das Skript wird beendet.")
        return
    print("eingegebener schluessel:   ",key)
    # Schritt 3: Passwort verschlüsseln
    encrypted_password = encryption.encryption(new_password, key)
    print("Passwort wurde verschlüsselt.")
    print("Verschlüsseltes Passwort:", encrypted_password)
    # Schritt 4: Schlüssel für die Speicherung anpassen und speichern
    key_for_storage = key + 3
    print("schluessel der in der DB steht:   ",key_for_storage)
    safe_password(encrypted_password, key_for_storage, anwendungsfall) 
    print("Passwort, Schlüssel und Anwendungsfall wurden in der Datenbank gespeichert.")
    
    # Schritt 5: Demonstriert nun den Abruf und die Entschlüsselung ---
    print("\n--- Start der automatischen Demonstration ---")
    
    # Schritt 6: Daten aus der Datenbank abrufen
    password_data = output_password()

    if password_data:
        encrypted_password_from_db, key_from_db, app_from_db = password_data
        
        # Schritt 7: Schlüssel für die Entschlüsselung wieder anpassen
        key_for_decryption = key_from_db - 3
        
        # Schritt 8: Passwort entschlüsseln
        decrypted_password = decryption.decryption(encrypted_password_from_db, key_for_decryption)
        
        # Schritt 9: Ausgabe der entschlüsselten Informationen
        print("Passwort entschlüsselt.")
        print("-" * 20)
        print(f"Anwendungsfall: {app_from_db}")
        print(f"Passwort: {decrypted_password}")
        print("-" * 20)
    else:
        print("Kein Datensatz in der Datenbank gefunden, keine Entschlüsselung möglich.")
        
if __name__ == "__main__":
    main()
