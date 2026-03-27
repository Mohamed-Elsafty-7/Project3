import string

ALPHABET_LOWER = string.ascii_lowercase
ALPHABET_UPPER = string.ascii_uppercase


def encrypt(text: str, shift: int) -> str:
    """Encrypt text using Caesar cipher."""
    result = ""
    shift = shift % 26 
    
    for char in text:
        if char.lower() in ALPHABET_LOWER:
            is_upper = char.isupper()
            alphabet = ALPHABET_UPPER if is_upper else ALPHABET_LOWER
            
            original_index = alphabet.index(char)
            new_index = (original_index + shift) % 26
            result += alphabet[new_index]
        else:
            result += char 
    return result


def decrypt(text: str, shift: int) -> str:
    """Decrypt text using Caesar cipher."""
    result = ""
    shift = shift % 26
    
    for char in text:
        if char.lower() in ALPHABET_LOWER:
            is_upper = char.isupper()
            alphabet = ALPHABET_UPPER if is_upper else ALPHABET_LOWER
            
            current_index = alphabet.index(char)
            original_index = (current_index - shift) % 26
            result += alphabet[original_index]
        else:
            result += char
    return result


def main():
    print("=== Caesar Cipher Tool ===\n")
    
    while True:
        print("What do you want to do?")
        print("1. Encrypt a message")
        print("0. Decrypt a message")
        choice = input("Enter your choice (1/0): ").strip()
        
        if choice not in ["0", "1"]:
            print("Invalid input! Please choose 0 or 1.\n")
            continue
        
        message = input("\nEnter the message: ")
        
        while True:
            try:
                shift = int(input("Enter the shift number: "))
                break
            except ValueError:
                print("Please enter a valid number for shift!")
        
        if choice == "1":
            result = encrypt(message, shift)
            print(f"\nEncrypted message: {result}\n")
        else:
            result = decrypt(message, shift)
            print(f"\nDecrypted message: {result}\n")
        
        while True:
            again = input("Do you want to continue? (y/n): ").strip().lower()
            if again in ["y", "n", "yes", "no"]:
                break
            print("Please enter y or n!")
        
        if again in ["n", "no"]:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()