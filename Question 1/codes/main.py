# ===========================
# Main program to execute encryption, decryption, and verification
# ===========================




from encryption import encrypt_file
from decryption import decrypt_file
from verification import verify


def main():
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypt_file(shift1, shift2)
    decrypt_file(shift1, shift2)
    verify()


if __name__ == "__main__":
    main()

