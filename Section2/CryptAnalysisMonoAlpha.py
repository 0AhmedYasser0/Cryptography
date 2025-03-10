import sys

def main():
    # Read the encrypted text from standard input
    ciphertext = sys.stdin.read()
    
    # Initialize frequency counts for each letter (a-z)
    counts = {chr(ord('a') + i): 0 for i in range(26)}
    
    # Calculate frequency of each letter in the ciphertext
    for c in ciphertext.lower():
        if c.isalpha():
            counts[c] += 1
    
    # Sort the letters by frequency (descending), then alphabetically for ties
    sorted_letters = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    cipher_order = [letter for letter, _ in sorted_letters]
    
    # Standard English letter frequency order (most to least common)
    english_freq = 'etaoinshrdlcumwfgypbvkjxqz'
    
    # Create substitution key based on frequency analysis
    substitution_key = {}
    for cipher_char, english_char in zip(cipher_order, english_freq):
        substitution_key[cipher_char] = english_char
    
    # Decrypt the ciphertext using the substitution key
    decrypted = []
    for char in ciphertext:
        if char.isalpha():
            # Convert to lowercase for substitution, then use the key
            decrypted_char = substitution_key[char.lower()]
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    
    decrypted_text = ''.join(decrypted)
    print(decrypted_text)

if __name__ == "__main__":
    main()