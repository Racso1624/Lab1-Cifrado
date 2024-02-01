# Oscar Fernando López Barrios
# Carné 20679
# Cifrado

import unidecode
from math import gcd
from frecuency import frequency_analysis

alphabet = ('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')

def encrypt(key_a, key_b, text):

    encrypted_text = ''
    for i in text:
        if (i != ' '):
            new_letter = unidecode.unidecode(i).upper()
            letter = ((alphabet.index(new_letter) * key_a) + key_b) % len(alphabet)
            encrypted_text += alphabet[letter]
        else:
            encrypted_text += ' '

    return encrypted_text

def decrypt(key_a, key_b, text):

    decrypted_text = ''
    for i in text:
        if (i != ' '):
            letter = int((pow(key_a, -1, len(alphabet)) * (alphabet.index(i) - key_b))) % len(alphabet)
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
            key_a = int(input("Ingrese la key A: "))
            key_b = int(input("Ingrese la key B: "))
            mcd_result = gcd(key_a, len(alphabet))
            if (mcd_result != 1):
                print("El factor comun entre la llave A y la cantidad de letras del alfabeto debe ser 1")
                return
            encrypted_text = encrypt(key_a, key_b, text)
            print("El texto encriptado es el siguiente: ", encrypted_text)
            print("El analisis de frecuencias es el siguiente: ", frequency_analysis(encrypted_text, alphabet))
        elif (option == 2):
            print("\nDesencriptar")
            text = input("Ingrese el texto a desencriptar: ")
            key_a = int(input("Ingrese la key A: "))
            key_b = int(input("Ingrese la key B: "))
            mcd_result = gcd(key_a, len(alphabet))
            if (mcd_result != 1):
                print("El factor comun entre la llave A y la cantidad de letras del alfabeto debe ser 1")
                return
            print("El texto desencriptado es el siguiente: ", decrypt(key_a, key_b, text))
        elif (option == 3):
            condition = False
        else:
            print("\nIngrese otra opcion")


if __name__ == "__main__":
    main()