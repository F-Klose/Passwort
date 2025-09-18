from curses.ascii import isprint

# noch nicht fertig aus alt projekt zum überarbeiten entnommen
# caesar verschlüsselung
# verschiebung der buchstaben im alphabet um n stellen
# z.b. 3 stellen: a->d, b->e, c->f
# mit cout -> ist count durch 2 teil bar dann wird der wert in negative gesetzt 
result = []
count = 0

"""

func verschluesselung(text, shift):
    text = text.lower()
    text = text.replace("ä", "ae").replace("ü", "ue").replace("ö", "oe")
    result = []
    for char in text:
        if count % 2 == 0:
            shift = shift
        else:
            shift = -shift
        shift_base = 97# ASCII-Wert von 'a'
"""
    
def cesar_verschiebung(text, shift):
    text = text.lower()
    text = text.replace("ä", "ae").replace("ü", "ue").replace("ö", "oe")
    result = []
    for char in text:
        if char.isalpha():
            shift_base = 97
            #chr(((ord(c) - ord("a") +1) % 26) + ord("a"))if c.islower() else c for c in ab])
            new_char = chr(((ord(char) - shift_base + shift) % 26) + shift_base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)
