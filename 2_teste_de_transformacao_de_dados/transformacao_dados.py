# Code developed by Igor de Matos da Rosa
# Date: 2025-03-24
# Código desenvolvido por Igor de Matos da Rosa
# Data: 24-03-2025

# Question 2

# (en)Importing the necessary libraries
# (pt-br)Importando as bibliotecas necessárias
import os
import sys
import zipfile

# (en)Add the directory where the headers are located to sys.path
# (pt-br)Adiciona o diretório onde os headers estão localizado ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# (en)Add headers to the code
# (pt-br)Adiciona cabeçalhos para o código
from headers.pdf import pdf

# (en)Path to PDF file
# (pt-br)Caminho para o arquivo PDF
pdf_manipulate = pdf(
    "", # Site
    "", # URL
    "../1_teste_de_web_scraping/pdf/" # Path
    )

# (en)Finding all PDF files in the directory have the word "Anexo_I" in the name
# Also filters if the file contains 'Anexo_II' (if they exist)
# (pt-br)Encontrando todos os arquivos PDF no diretório que possuem a palavra "Anexo_I" no nome.
# Também filtra se o arquivo contém 'Anexo_II' (caso exista)
pdf_manipulate.findPdfFromPath("*Anexo_I*.pdf", "Anexo_II")

# (en)Check if we found any valid files
# (pt-br)Verificando se encontramos arquivos válidos
df = pdf_manipulate.extractTable(
    [
    "Procedimento", 
    "RN", 
    "Vigência", 
    "OD",
    "AMB",
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
csv_path = "./data/dados_extraidos.csv"

# (en)Ensure the 'data' directory exists before saving the CSV
# (pt-br)Garantir que o diretório 'data' exista antes de salvar o arquivo CSV
os.makedirs(os.path.dirname(csv_path), exist_ok=True)
df.to_csv(csv_path, index=False)

#(en)Directory of csv file
#(pt-br)Diretório do arquivo csv
print(f"✅ Data save in: {csv_path}")

# (en)Name of the ZIP file
# (pt-br)Nome do arquivo ZIP
zip_filename = "./Teste_Igor-de-Matos-da-Rosa.zip"

# (en)Compress the CSV into the ZIP file
# (pt-br)Compactar o CSV no arquivo ZIP
with zipfile.ZipFile(zip_filename, "w") as zipf:
    zipf.write(csv_path, "dados_extraidos.csv")

# (en)Show the message that the ZIP file was created
# (pt-br)Mostra a mensagem que o arquivo ZIP foi criado
print(f"✅ ZIP created in: {zip_filename}")
