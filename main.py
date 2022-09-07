# Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "-", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

def get_key_from_value(d, target):
    for key, value in d.items():
        if value == target:
            return key
    return None

# It can translate natural text to morse code and vice versa
def morse_decoder(text):
    morse_alphabet = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----.", "0": "-----"
    }

    text = text.upper()
    converted_text = ""
    if "A" in text or "E" in text or "I" in text or "O" in text or "U" in text:
        for c in text:
            if c == " ":
                converted_text += " "
            else:
                converted_text += morse_alphabet[c]
                converted_text += " "
    else:
        current_letter = ""
        for c in text:
            if c == " ":
                key = get_key_from_value(morse_alphabet, current_letter)
                if key:
                    converted_text += key
                else:
                    converted_text += " "
                current_letter = ""
            else:
                current_letter += c
        
        converted_text += get_key_from_value(morse_alphabet, current_letter)

    return converted_text


print(morse_decoder("Hello World 3"))
print(morse_decoder(".... . .-.. .-.. ---  .-- --- .-. .-.. -..  ...--"))
