# ===========================
# Function to decrypt text based on previous shifts and encrypted text file
# ===========================





def decrypt(text, shift1, shift2):
    if "a" <= text <= "z":
        first = chr((ord(text) - ord("a") - (shift1 * shift2)) % 26 + ord("a"))
        if "a" <= first <= "m":
            return first

        second = chr((ord(text) - ord("a") + (shift1 + shift2)) % 26 + ord("a"))
        if "n" <= second <= "z":
            return second

    elif "A" <= text <= "Z":
        first = chr((ord(text) - ord("A") + shift1) % 26 + ord("A"))
        if "A" <= first <= "M":
            return first

        second = chr((ord(text) - ord("A") - (shift2 ** 2)) % 26 + ord("A"))
        if "N" <= second <= "Z":
            return second


    return text


def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r", encoding="utf-8") as f:
        ch = f.read()
    
    decrypted = "".join(decrypt(c, shift1, shift2) for c in ch)

    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted)
