import string
import random
import sys

def decrypt(ciphertext, key):
    decrypt_map = dict(zip(string.ascii_lowercase, key))
    decrypted = []
    for char in ciphertext.lower():
        if char in decrypt_map:
            decrypted.append(decrypt_map[char])
        else:
            decrypted.append(char)
    return ''.join(decrypted)

def generate_random_key():
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return alphabet

def main():
    ciphertext = input("Enter encrypted message: ").strip()
    
    attempt = 1
    try:
        while True:
            key = generate_random_key()
            plaintext = decrypt(ciphertext, key)
            
            print(f"Attempt #{attempt}")
            print(f"Key: {''.join(key)}")
            print(f"Decrypted: {plaintext}\n")
            sys.stdout.flush()  # إفراز buffer الإخراج فورًا
            attempt += 1
            
    except KeyboardInterrupt:
        print("\nBrute force interrupted by user!")

if __name__ == "__main__":
    main()