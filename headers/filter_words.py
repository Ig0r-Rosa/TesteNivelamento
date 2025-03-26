# Code developed by Igor de Matos da Rosa
# Date: 2025-03-25
# Código desenvolvido por Igor de Matos da Rosa
# Data: 25/03/2025

# (en)This header is used to simplify the manipulation of words
# (pt-br)Este cabeçalho é usado para simplificar a manipulação de palavras

# (en)Importing the necessary libraries
# (pt-br)Importando as bibliotecas necessárias
import re

# (en)Function to get the first two words of a string
# (pt-br)Divida a string em palavras e pegue as duas primeiras
def get_first_two_words(text):
    words = re.findall(r'\b\w+\b', text)
    return ' '.join(words[:2])