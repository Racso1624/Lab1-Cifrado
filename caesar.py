# Oscar Fernando López Barrios
# Carné 20679
# Cifrado

import unidecode

alphabet = ('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')

def frequency_analysis(text):

    frequency_analysis_data = {}
    for letter in alphabet:
        frequency_analysis_data[letter] = 0

    for letter in text:
        if letter in alphabet:
            frequency_analysis_data[letter] += 1

    return { letter: round(frequency_analysis_data[letter] / len(text), 3) for letter in alphabet }

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

def main():
    print("Bienvenido al Sistema de Encriptación y Desencriptación")
    print("Tiene las siguientes opciones:")
    print("1) Encriptar")
    print("2) Desencriptar")
    print("3) Salir")

    condition = True
    while(condition):
        option = int(input("\nIngrese la opción que desee: "))
        if (option == 1):
            print("\nEncriptar")
            text = input("Ingrese el texto a encriptar: ")
            key = int(input("Ingrese la key: "))
            encrypted_text = encrypt(key, text)
            print("El texto encriptado es el siguiente: ", encrypted_text)
            print("El analisis de frecuencias es el siguiente: ", frequency_analysis(encrypted_text))
        elif (option == 2):
            print("\nDesencriptar")
            text = input("Ingrese el texto a desencriptar: ")
            key = int(input("Ingrese la key: "))
            print("El texto desencriptado es el siguiente: ", decrypt(key, text))
        elif (option == 3):
            condition = False
        else:
            print("\nIngrese otra opcion")


if __name__ == "__main__":
    main()