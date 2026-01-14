# ===========================
# Function to verify that decrypted text matches original text
# ===========================




def verify():
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        original = f.read()
    
    with open("decrypted_text.txt", "r", encoding="utf-8") as f:
        decrypted = f.read()
    
    if original == decrypted:
        print("Verification successful: Decrypted text matches original.")
    else:
        print("Verification failed: Decrypted text does NOT match original.")
