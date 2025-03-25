# Code developed by Igor de Matos da Rosa
# Date: 2025-03-24
# Código desenvolvido por Igor de Matos da Rosa
# Data: 24-03-2025

# Question 2

# (en)Importing the necessary libraries
# (pt-br)Importando as bibliotecas necessárias
import pdfplumber
import pandas as pd
import os
import glob
import zipfile

# (en)Path to PDF file
# (pt-br)Caminho para o arquivo PDF
pdf_path = "../1_teste_de_web_scraping/downloads/"

# (en)Finding all PDF files in the directory have the word "Anexo_I" in the name
# (pt-br)Encontrando todos os arquivos PDF no diretório que possuem a palavra "Anexo_I" no nome
pdf_files = glob.glob(os.path.join(pdf_path, "*Anexo_I*.pdf"))

# (en)Filtering files that contain 'Anexo_II' (if they exist)
# (pt-br)Filtrar os arquivos que contenham 'Anexo_II' (caso existam)
pdf_files = [file for file in pdf_files if "Anexo_II" not in file]

# (en)Check if we found any valid files
# (pt-br)Verificando se encontramos arquivos válidos
if pdf_files:

    # (en)Opening the PDF file
    # (pt-br)Abrindo o arquivo PDF
    with pdfplumber.open(pdf_files[0]) as pdf:

        # (en)List to store all extracted tables
        # (pt-br)Lista para armazenar todas as tabelas extraídas
        all_tables = []

        # (en)Iterating through all pages of the PDF
        # (pt-br)Iterar por todas as páginas do PDF
        for page in pdf.pages:

            # (en)Extracting the table from the page
            # (pt-br)Extrair a tabela da página
            table = page.extract_table()

            # (en)Check if a table was successfully extracted
            # (pt-br)Verifique se uma tabela foi extraída com sucesso
            if table:
                # (en)Add the table to the list
                # (pt-br)Adicionar a tabela à lista
                all_tables.append(table)

# (en)Combine all tables into a single DataFrame (using pandas)
# (pt-br)Combine todas as tabelas em um único DataFrame (usando pandas)
all_data = []
for table in all_tables:

    # (en)Ignore the first line (header) repeated on each page
    # (pt-br)Ignore a primeira linha (cabeçalho) repetida em cada página
    for row in table[1:]:
        all_data.append(row)

# (en)Create the DataFrame
# (pt-br)Criar o DataFrame
df = pd.DataFrame(all_data, columns=[
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
    ])

# (en)Show the first lines to check if the extraction was done correctly
# (pt-br)Mostra as primeiras linhas para verificar se a extração foi feita corretamente
print(df.head())

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
