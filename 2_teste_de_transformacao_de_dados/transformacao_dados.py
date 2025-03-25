# Code developed by Igor de Matos da Rosa
# Date: 2025-03-24
# Código desenvolvido por Igor de Matos da Rosa
# Data: 24-03-2025

# Question 2

# (en)Importing the necessary libraries
# (pt-br)Importando as bibliotecas necessárias
import os
import sys

# (en)Add the directory where the headers are located to sys.path
# (pt-br)Adiciona o diretório onde os headers estão localizado ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# (en)Add headers to the code
# (pt-br)Adiciona cabeçalhos para o código
from headers.pdf import pdf
from headers.csv import csv
from headers.filter_words import get_first_two_words

# (en)Path to PDF file
# (pt-br)Caminho para o arquivo PDF
pdf_manipulate = pdf(
    "", # Site
    "", # URL
    "../1_teste_de_web_scraping/pdf/" # Path
    )

# (en)Finding all PDF files in the directory have the word "Anexo_I" in the name.
# Also filters if the file contains 'Anexo_II' (if they exist)
# (pt-br)Encontrando todos os arquivos PDF no diretório que possuem a palavra "Anexo_I" no nome.
# Também filtra se o arquivo contém 'Anexo_II' (caso exista)
pdf_manipulate.findPdfFromPath("*Anexo_I*.pdf", "Anexo_II")

# (en)Find the fields of the subtitles "OD" and "AMB"
# (pt-br)Procura os campos da legendas "OD" e "AMB"
complete_description = pdf_manipulate.findIn("Legenda:", ["OD", "AMB"])

# (en)Check if we found any valid files
# (pt-br)Verificando se encontramos arquivos válidos
df = pdf_manipulate.extractTable(
    [
    "Procedimento", 
    "RN", 
    "Vigência", 
    get_first_two_words(complete_description["OD"]),
    get_first_two_words(complete_description["AMB"]),
    "HCO",
    "HSO",  
    "REF",
    "PAC",
    "DUT",
    "SubGrupo",
    "Grupo",
    "Capítulo"
    ]
)

# (en)Save the extracted data to a CSV file
# (pt-br)Salvar os dados extraídos em um arquivo CSV
csv_manipulate = csv(
    df,
    "dados_extraidos"
    )

csv_manipulate.saveCsv()

# (en)Name of the ZIP file
# (pt-br)Nome do arquivo ZIP
csv_manipulate.setTheZipAndZip("Teste_Igor-de-Matos-da-Rosa.zip")
