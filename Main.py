# zusammen führer aller dateien
# DB_setup.py
# verschluesselung.py
# entschluesselung.py
# ausgabe.py
# in der "Main.py" werden die dateien zusammen geführt und ausgeführt
# die dateien sind so aufgebaut das sie einzeln getestet werden können
import setup_db
import encryption
import decryption
import output
import utils
import generate_random_password
key = 0 # anpassen an schlüssel der eingegeben wird 
def main():
    setup_db.init_db()
    print("Datenbank eingerichtet.")
    
    new_password = generate_random_password.generate_random_password(8)
    print("Passwort generiert.")

    encrypted_password = encryption.encryption(new_password, 3)
    print("Passwort wurde verschlüsselt mit der gewünschten Verschiebung.")
    
    utils.safe_password(encrypted_password)
    print("Verschlüsseltes Passwort wurde in der Datenbank gespeichert.")
    
#TODO: Weiterführen... 

if __name__ == "__main__":
    main()
