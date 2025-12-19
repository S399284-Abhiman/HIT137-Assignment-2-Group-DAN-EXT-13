# ===========================
# Function to encrypt text based on given shifts
# ===========================



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
    


def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        ch = f.read()
    
    encrypted = "".join(encrypt(c, shift1, shift2) for c in ch)

    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted)



      
    
    
