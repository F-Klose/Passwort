from curses.ascii import isprint

# noch nicht fertig aus alt projekt zum überarbeiten entnommen
# caesar verschlüsselung
# verschiebung der buchstaben im alphabet um n stellen
# z.b. 3 stellen: a->d, b->e, c->f
# mit cout -> ist count durch 2 teil bar dann wird der wert in negative gesetzt 
result = []

"""
#TODO Doku schreiben
"""
def encryption(text, shift):
    result = []
    count = 0
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
    print(encryption(text, shift))