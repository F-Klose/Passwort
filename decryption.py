<<<<<<< HEAD:entschluesselung.py
def entschluesselung(text, shift):
    """
    Entschlüsselt einen Text, der mit der modifizierten Caesar-Verschlüsselung verschlüsselt wurde.
    Jeder erste Buchstabe wird mit -shift, jeder zweite mit +shift verschoben.
    """
=======
from curses.ascii import isprint
#TODO: siehe unten offene tasks für decryption.py
# noch nicht fertig aus alt projekt zum überarbeiten entnommen
# caesar verschlüsselung muss hier wieder zurück gesetzt werden nach schussel wert aus DB 
# mit cout -> ist count durch 2 teil bar dann wird der wert in negative gesetzt 



def caesar_cipher(text, shift):
>>>>>>> 0bc394f219c0e948e0b4a8297c6c9aec5b8e59bf:decryption.py
    text = text.lower()
    text = text.replace("ä", "ae").replace("ü", "ue").replace("ö", "oe")
    result = []
    for idx, char in enumerate(text):
        if char.isalpha():
            shift_base = ord('a')
            # Jeder erste Buchstabe wird negativ, jeder zweite positiv verschoben
            actual_shift = -shift if idx % 2 == 0 else shift
            new_char = chr(((ord(char) - shift_base + actual_shift) % 26) + shift_base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)
<<<<<<< HEAD:entschluesselung.py

if __name__ == "__main__":
    text = input("Text zum Entschlüsseln: ")
    shift = int(input("Verschiebung: "))
    print(entschluesselung(text, shift))
=======
def count_erfassung(text, chars):
    counts = {char: text.count(char) for char in chars}
    return counts 
print("")
print("")
text = input("hier kannst du deinen text der ver oder entschlüsselt werden soll einfügen")
print("")
print("")
chars_to_count = ['e', 'q']
counts = count_erfassung(text, chars_to_count)
print("")
print(f"\nim text gibt es so viele e und q")
print("")
print("")
for char, count in counts.items():
    print(f"'{char}': {count} mal ")
while True:
    try:
        shift = int(input("\nUm wie viele stellen soll verschoben werden????"))
        break
    except ValueError:
        print("ungueltig!!")
        print("")
        print(" noch mal ")
        print("")
shifted_text = caesar_cipher(text, shift) 
e15_wörter = ''.join(shifted_text.split()[5])
print("")
print(f"\n kurzer auszug aus dem Text: \n{e15_wörter}")
print("")
further_shift = input("\noch eine verschibung vornehmen?")
print("")
print("")
if further_shift == "ja":
    caesar_cipher()
else:
    whole_text = input("\nsoll der ganze text angezeigt werden(ja/nein)")
    if whole_text == "ja":
        print(f"\n \n{shifted_text}")
    else:   
        print("fertig")


caesar_cipher()
>>>>>>> 0bc394f219c0e948e0b4a8297c6c9aec5b8e59bf:decryption.py
