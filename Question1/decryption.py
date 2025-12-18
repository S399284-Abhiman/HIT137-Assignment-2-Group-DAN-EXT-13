# decryption logic for the modified Caesar cipher

def decrypt(text, shift1, shift2):
    if "a" <= text <= "z":
        
        if text >= "n":
            return chr((ord(text) - ord("a") - shift1 * shift2) % 26 + ord("a"))
        
        else:
            return chr((ord(text) - ord("a") + (shift1 + shift2)) % 26 + ord("a"))

    elif "A" <= text <= "Z":
        
        if text >= "N":
            return chr((ord(text) - ord("A") - shift1) % 26 + ord("A"))
        
        else:
            return chr((ord(text) - ord("A") + shift2 ** 2) % 26 + ord("A"))
    

    else:
        return text


def shift_string(text, shift1, shift2):
    return "".join(decrypt(c, shift1, shift2) for c in text)


def main():
    
    encrypted_text = input("Enter the encrypted text: ")
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    
    decrypted_text = shift_string(encrypted_text, shift1, shift2)
    
    
    print("Decrypted text:", decrypted_text)



if __name__ == "__main__":
    main()
