# Oscar Fernando López Barrios
# Carné 20679
# Cifrado

import unidecode
from frecuency import frequency_analysis, frecuency_visual_comparison, test_text_metric

alphabet = ('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
top_alphabet_letter = "E"

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

def brute_force_decrypt(file_route):

    with open(file_route, 'r', encoding="utf-8") as file:
        ciphertext = file.read()
    
    frequency_analysis_result = frequency_analysis(ciphertext, alphabet)

    decrypt_result_metric = {}
    text_result = {}

    top_frecuency_letter = max(frequency_analysis_result.items(), key=lambda item: item[1])[0]
    letter_displacement = alphabet.index(top_frecuency_letter) - alphabet.index(top_alphabet_letter)

    if (letter_displacement < 0):
        letter_displacement = len(alphabet) + letter_displacement

    for i in range(len(alphabet)):

        key = letter_displacement % len(alphabet)
        key_text = decrypt(key, ciphertext)
        key_text_metric = test_text_metric(key_text)

        text_result[key] = key_text
        decrypt_result_metric[key] = key_text_metric
        letter_displacement += 1

    final_results = dict(sorted(decrypt_result_metric.items(), key=lambda item: item[1]))
    final_keys = list(final_results.keys())

    with open("results/results-caesar-bruteforce.txt", "w", encoding="utf-8") as file:
        for key in final_keys:
            file.write(f"key number {key}: {text_result[key]}\n")

def main():
    print("Bienvenido al Sistema de Encriptación y Desencriptación")
    print("Tiene las siguientes opciones:")
    print("1) Encriptar")
    print("2) Desencriptar")
    print("3) Bruteforce")
    print("4) Salir")

    condition = True
    while(condition):
        option = int(input("\nIngrese la opción que desee: "))
        if (option == 1):
            print("\nEncriptar")
            text = input("Ingrese el texto a encriptar: ")
            key = int(input("Ingrese la key: "))
            encrypted_text = encrypt(key, text)
            frequency_analysis_result =  frequency_analysis(encrypted_text, alphabet)
            print("El texto encriptado es el siguiente: ", encrypted_text)
            print("El analisis de frecuencias es el siguiente: ", frequency_analysis_result)
            frecuency_visual_comparison(frequency_analysis_result)
        elif (option == 2):
            print("\nDesencriptar")
            text = input("Ingrese el texto a desencriptar: ")
            key = int(input("Ingrese la key: "))
            print("El texto desencriptado es el siguiente: ", decrypt(key, text))
        elif (option == 3):
            print("\nBruteforce")
            file_route = input("Ingrese la ruta del archivo a desencriptar: ")
            brute_force_decrypt(file_route)
        elif (option == 4):
            condition = False
        else:
            print("\nIngrese otra opcion")


if __name__ == "__main__":
    main()