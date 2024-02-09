# Oscar Fernando López Barrios
# Carné 20679
# Cifrado

import matplotlib.pyplot as plt
import math

official_frequency_analysis = {
    "A": 0.1253,
    "B": 0.0142,
    "B": 0.0468,
    "D": 0.0586,
    "E": 0.1368,
    "F": 0.0069,
    "G": 0.0101,
    "H": 0.0070,
    "I": 0.0625,
    "J": 0.0044,
    "K": 0.0002,
    "L": 0.0497,
    "M": 0.0315,
    "N": 0.0671,
    "Ñ": 0.0031,
    "O": 0.0868,
    "P": 0.0251,
    "Q": 0.0088,
    "R": 0.0687,
    "S": 0.0798,
    "T": 0.0463,
    "U": 0.0393,
    "V": 0.0090,
    "W": 0.0001,
    "X": 0.0022,
    "Y": 0.0090,
    "Z": 0.0052,
}

def frequency_analysis(text, alphabet):

    frequency_analysis_data = {}
    for letter in alphabet:
        frequency_analysis_data[letter] = 0

    for letter in text:
        if letter in alphabet:
            frequency_analysis_data[letter] += 1

    return { letter: round(frequency_analysis_data[letter] / len(text), 4) for letter in alphabet }

def frecuency_visual_comparison(frequency_result):

    letters = sorted(set(official_frequency_analysis.keys()) & set(frequency_result.keys()))

    official_values = [official_frequency_analysis[key] for key in letters]
    result_values = [frequency_result[key] for key in letters]

    fig, ax = plt.subplots()

    bar_size = 0.35
    values = range(len(letters))
    official_bars = ax.bar(values, official_values, bar_size, label='Oficiales')
    result_bars = ax.bar([i + bar_size for i in values], result_values, bar_size, label='Resultados')

    for i, value in enumerate(official_values):
        ax.text(i, value + 0.01, f"{value:.4f}", ha='center', va='bottom', rotation=90, fontsize=8)

    for i, value in enumerate(result_values):
        ax.text(i + bar_size, value + 0.01, f"{value:.4f}", ha='center', va='bottom', rotation=90, fontsize=8)

    ax.set_xticks([i + bar_size / 2 for i in values])
    ax.set_xticklabels(letters)
    ax.set_ylabel('Valores')
    ax.set_title('Comparación de Valores de Frecuencia')
    ax.legend()

    plt.show()

def text_entropy(text):

    text = text.upper()

    text_probability = [(text.count(char) / len(text)) for char in set(text)]
    alphabet_probability = [(official_frequency_analysis.get(char, 0.0001)) for char in set(text)]

    entropy_result = sum([(x * math.log2(x / y)) for x, y in zip(text_probability, alphabet_probability)])

    return entropy_result