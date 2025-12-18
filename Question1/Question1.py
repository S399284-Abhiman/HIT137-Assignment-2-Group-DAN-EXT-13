# Simple encryption and decryption using Caesar cipher

def encrypt(text, shift1, shift2):
    if "a" <= text <= "z":
        if text <= "m":
            return chr((ord(text) - ord("a") + shift1 * shift2) % 26 + ord("a"))
        else:
            return chr((ord(text) - ord("a") - (shift1 + shift2)) % 26 + ord("a"))

    elif "A" <= text <= "Z": 
        if text <= "M":
            return chr((ord(text) - ord("A") - shift1) % 26 + ord("A"))
        else:
            return chr((ord(text) - ord("A") + shift2 ** 2) % 26 + ord("A"))
    
    else:
        return text
    


def shift_string(text, shift1, shift2):
    return "".join(encrypt(c, shift1, shift2) for c in text)

testtext = input("Enter your text:")
shift1 = int(input("enter shift1 value:"))
shift2 = int(input("enter shift2 value:"))

shifted_text = shift_string(testtext, shift1, shift2)
print("Shifted text:", shifted_text)



         
    
    
