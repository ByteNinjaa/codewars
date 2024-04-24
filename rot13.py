def rot13(message):
    ciphered = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                ciphered += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                ciphered += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            ciphered += char
    return ciphered
