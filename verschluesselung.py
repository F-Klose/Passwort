from curses.ascii import isprint

# noch nicht fertig aus alt projekt zum überarbeiten entnommen
# caesar verschlüsselung
# verschiebung der buchstaben im alphabet um n stellen
# z.b. 3 stellen: a->d, b->e, c->f
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
shifted_text = cesar_verschiebung(text, shift) 
e15_wörter = ''.join(shifted_text.split()[5])
print("")
print(f"\n kurzer auszug aus dem Text: \n{e15_wörter}")
print("")
further_shift = input("\noch eine verschibung vornehmen?")
print("")
print("")
if further_shift == "ja":
    cesar_verschiebung()
else:
    whole_text = input("\nsoll der ganze text angezeigt werden(ja/nein)")
    if whole_text == "ja":
        print(f"\n \n{shifted_text}")
    else:   
        print("fertig")


cesar_verschiebung()