import string

def create_playfair_matrix(keyword):
    keyword = keyword.replace(" ", "").upper().replace("J", "I")
    matrix_list = []
    for ch in keyword:
        if ch not in matrix_list and ch in string.ascii_uppercase:
            matrix_list.append(ch)
    for ch in string.ascii_uppercase:
        if ch == 'J':
            continue
        if ch not in matrix_list:
            matrix_list.append(ch)
    return matrix_list

def process_message(message):
    message = message.upper().replace(" ", "").replace("J", "I")
    processed = []
    i = 0
    while i < len(message):
        if message[i] not in string.ascii_uppercase:
            i += 1
            continue
        if i == len(message) - 1:
            processed.extend([message[i], 'X'])
            i += 1
        else:
            next_idx = i + 1
            while next_idx < len(message) and message[next_idx] not in string.ascii_uppercase:
                next_idx += 1
            if next_idx >= len(message):
                processed.extend([message[i], 'X'])
                i += 1
            else:
                ch1, ch2 = message[i], message[next_idx]
                if ch1 == ch2:
                    processed.extend([ch1, 'X'])
                    i += 1
                else:
                    processed.extend([ch1, ch2])
                    i = next_idx + 1
    return processed

def playfair_cipher(matrix_list, text, mode):
    positions = {ch: (i // 5, i % 5) for i, ch in enumerate(matrix_list)}
    result = []
    for i in range(0, len(text), 2):
        ch1, ch2 = text[i], text[i+1]
        r1, c1 = positions[ch1]
        r2, c2 = positions[ch2]
        if r1 == r2:
            shift = 1 if mode == 'E' else -1
            c1 = (c1 + shift) % 5
            c2 = (c2 + shift) % 5
        elif c1 == c2:
            shift = 1 if mode == 'E' else -1
            r1 = (r1 + shift) % 5
            r2 = (r2 + shift) % 5
        else:
            c1, c2 = c2, c1
        new_ch1 = matrix_list[r1 * 5 + c1]
        new_ch2 = matrix_list[r2 * 5 + c2]
        result.append(new_ch1)
        result.append(new_ch2)
    return ''.join(result)

# Main program
keyword = input("Enter the keyword: ")
matrix = create_playfair_matrix(keyword)
print("\nPlayfair Matrix (5x5):")
for i in range(5):
    print(' '.join(matrix[i*5:(i+1)*5]))

mode = input("\nDo you want to (E)ncrypt or (D)ecrypt? ").upper()
while mode not in ['E', 'D']:
    mode = input("Invalid choice. Enter 'E' or 'D': ").upper()

message = input("Enter the message: ")
processed = process_message(message)
output = playfair_cipher(matrix, processed, mode)
print("\nResult:", output)