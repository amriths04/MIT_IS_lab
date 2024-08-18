def additive_encrypt(plaintext, key):
    ciphertext = ""
    plaintext = plaintext.replace(" ", "").upper()

    for char in plaintext:
        if char.isalpha():
            num = ord(char) - ord('A')
            encrypted_num = (num + key) % 26
            encrypted_char = chr(encrypted_num + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    
    return ciphertext

def additive_decrypt(ciphertext, key):
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            num = ord(char) - ord('A')
            decrypted_num = (num - key) % 26
            decrypted_char = chr(decrypted_num + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

plaintext = "I am learning information security"
key = 20

ciphertext = additive_encrypt(plaintext, key)
print("Encrypted Message:", ciphertext)

decrypted_message = additive_decrypt(ciphertext, key)
print("Decrypted Message:", decrypted_message)
