def decryption(text, shift):
    """
    Entschlüsselt einen Text, der mit der modifizierten Caesar-Verschlüsselung verschlüsselt wurde.
    Jeder erste Buchstabe wird mit -shift, jeder zweite mit +shift verschoben.
    """
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

if __name__ == "__main__":
    text = input("Text zum Entschlüsseln: ")
    shift = int(input("Verschiebung: "))
    print(decryption(text, shift))