import unidecode

alphabet = ('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')

def encrypt(key, text):

    encrypted_text = ''
    for i in text:
        if (i != ' '):
            new_letter = unidecode.unidecode(i).upper()
            letter = (alphabet.index(new_letter) + key) % len(alphabet)
            encrypted_text += alphabet[letter]
        else:
            encrypted_text += ' '

    return encrypted_text

def decrypt(key, text):

    decrypted_text = ''
    for i in text:
        if (i != ' '):
            letter = (alphabet.index(i) - key) % len(alphabet)
            decrypted_text += alphabet[letter]
        else:
            decrypted_text += ' '

    return decrypted_text