# Oscar Fernando López Barrios
# Carné 20679
# Cifrado

import unidecode
from frecuency import frequency_analysis

alphabet = ('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')

def encrypt(keyword, text):

    encrypted_text = ''
    extended_keyword = keyword * (len(text) // len(keyword)) + keyword[:len(text) % len(keyword)]
    print(extended_keyword)
    for i in range(len(text)):
        if (text[i] != ' '):
            new_letter = unidecode.unidecode(text[i]).upper()
            new_letter_keyword = unidecode.unidecode(extended_keyword[i]).upper()
            letter = (alphabet.index(new_letter) + alphabet.index(new_letter_keyword)) % len(alphabet)
            encrypted_text += alphabet[letter]
        else:
            encrypted_text += ' '

    return encrypted_text

def decrypt(keyword, text):

    decrypted_text = ''
    extended_keyword = keyword * (len(text) // len(keyword)) + keyword[:len(text) % len(keyword)]
    for i in range(len(text)):
        if (text[i] != ' '):
            letter = (alphabet.index(text[i]) - alphabet.index(extended_keyword[i].upper())) % len(alphabet)
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
            keyword = input("Ingrese la keyword: ")
            encrypted_text = encrypt(keyword, text)
            print("El texto encriptado es el siguiente: ", encrypted_text)
            print("El analisis de frecuencias es el siguiente: ", frequency_analysis(encrypted_text, alphabet))
        elif (option == 2):
            print("\nDesencriptar")
            text = input("Ingrese el texto a desencriptar: ")
            keyword = input("Ingrese la keyword: ")
            print("El texto desencriptado es el siguiente: ", decrypt(keyword, text))
        elif (option == 3):
            condition = False
        else:
            print("\nIngrese otra opcion")


if __name__ == "__main__":
    main()