# Code developed by Igor de Matos da Rosa
# Date: 2025-03-24
# Last update: 2025-03-25
# Código desenvolvido por Igor de Matos da Rosa
# Data: 24/03/2025
# Última atualização: 25/03/2025

# Question 1

# (en)Importing the required libraries
# (pt-br)Importa as bibliotecas necessárias
import os.path
import sys

# (en)Add the directory where the headers are located to sys.path
# (pt-br)Adiciona o diretório onde os headers estão localizado ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# (en)Add headers to the code
# (pt-br)Adiciona cabeçalhos para o código
from headers.pdf import pdf

# (en)URL described in the challenge
# (pt-br)URL descrita no desafio
pdf_manipulate = pdf(
    "https://www.gov.br",
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    )

# (en)Find the links to the PDF files
# (pt-br)Encontra os links para os arquivos PDF
pdf_manipulate.findPdfLinks(["Anexo I", "Anexo II"]);

# (en)List to store the PDF files
# (pt-br)Cria lista para armazenar os arquivos PDF e faz o download pelo cabeçalho
pdf_manipulate.downloadPdf()

# (en)Create a ZIP file with the downloaded files using the header
# (pt-br)Cria um arquivo ZIP com os arquivos baixados usando o cabeçalho
pdf_manipulate.setFileToZipAndZip("anexos.zip")