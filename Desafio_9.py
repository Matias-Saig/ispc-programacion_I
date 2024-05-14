""" 
    9 - Anagrama. Escribe una función que reciba dos palabras y retorne
    verdadero o falso según sean o no anagramas.
"""

# soporte expresiones regulares
import re

# preguntas
def query_words(msg):
    reg_exp = r"[0-9\s]"
    while True:    
        control = input(msg).lower()
        if re.search(reg_exp, control) == None: 
            return control
        else:
            print("Las palabras no pueden contener números ni espacios\n")

# control de preguntas
def ctrl_words():
    while True:
        word_1 = query_words("Cual es la primer palabra?: ")
        word_2 = query_words("Con que palabra se forma el anagrama?: ")

        if word_1 == word_2:
            print(f"'{word_1}' y '{word_2}' son misma palabra y no pueden formar un anagrama\n")
        else:
            return [word_1, word_2]

# ordenar letras
def sort_words(words):
    compare = []
    for character in words:
        new = "".join(sorted(character))
        compare.append(new)
    return compare

# comparar preguntas ordenadas
def compare_word(words, sort_words):
    if sort_words[0] == sort_words[1]:
        print(f"\nLas palabras '{words[0]}' y '{words[1]}' forman un anagrama!")
    else:
        print(f"\nLas palabras '{words[0]}' y '{words[1]}' NO son un anagrama")
    
# ejecución
print("Anagrama \n")
origin_words = ctrl_words()
words_to_compare = sort_words(origin_words)
compare_word(origin_words, words_to_compare)