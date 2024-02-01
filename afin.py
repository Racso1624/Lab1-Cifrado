import unidecode
from math import gcd

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
            letter = (pow(key_a, -1) * (alphabet.index(i) - key_b)) % len(alphabet)
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
            print("El texto encriptado es el siguiente: ", encrypt(key_a, key_b, text))
        elif (option == 2):
            print("\nDesencriptar")
            text = input("Ingrese el texto a desencriptar: ")
            key = int(input("Ingrese la key: "))
            print("El texto desencriptado es el siguiente: ", decrypt(key_a, key_b, text))
        elif (option == 3):
            condition = False
        else:
            print("\nIngrese otra opcion")


if __name__ == "__main__":
    main()