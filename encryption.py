from curses.ascii import isprint
#TODO: siehe unten offene tasks für encryption.py
# noch nicht fertig aus alt projekt zum überarbeiten entnommen
# caesar verschlüsselung
# verschiebung der buchstaben im alphabet um n stellen
# z.b. 3 stellen: a->d, b->e, c->f
# mit cout -> ist count durch 2 teil bar dann wird der wert in negative gesetzt
result = []

"""

"""
<<<<<<< HEAD:verschluesselung.py
def verschluesselung(text, shift):
    result = []
    count = 0
=======
    
def caesar_cipher(text, shift):
>>>>>>> 0bc394f219c0e948e0b4a8297c6c9aec5b8e59bf:encryption.py
    text = text.lower()
    text = text.replace("ä", "ae").replace("ü", "ue").replace("ö", "oe")
    for idx, char in enumerate(text):
        if char.isalpha():
            shift_base = ord('a')
            # Jeder zweite Buchstabe wird negativ verschoben
            actual_shift = shift if idx % 2 == 0 else -shift
            new_char = chr(((ord(char) - shift_base + actual_shift) % 26) + shift_base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    text = input("Text zum Entschlüsseln: ")
    shift = int(input("Verschiebung: "))
    print(verschluesselung(text, shift))