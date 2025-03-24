# Code developed by Igor de Matos da Rosa
# Date: 2025-03-24
# Código desenvolvido por Igor de Matos da Rosa
# Data: 24/03/2025

# Question 1

# (en)Importing the required libraries
# (pt-br)Importa as bibliotecas necessárias
import os
import requests

# (en)Library to extract data from HTML and XML files
# (pt-br)Biblioteca para extrair dados de arquivos HTML e XML
from bs4 import BeautifulSoup

# (en)Library to zip the files
# (pt-br) Biblioteca para zipar os arquivos
from zipfile import ZipFile

# (en)URL described in the challenge
# (pt-br)URL descrita no desafio
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# (en)Create a director to store the downloaded files
# (pt-br)Cria um diretório para armazenar os arquivos baixados
os.makedirs("downloads", exist_ok=True)

# (en)Send a request to the URL
# (pt-br)Envia uma requisição para a URL
response = requests.get(URL)

# (en)Check if the request was successful
# (pt-br)Verifica se a requisição foi bem sucedida
response.raise_for_status()

# (en)Parse the HTML content of the page
# (pt-br)Analisa o conteúdo HTML da página
soup = BeautifulSoup(response.text, "html.parser")

# (en)Store the links to the PDF files
# (pt-br)Armazena os links para os arquivos PDF
pdf_links = []

# (en)Find all the links in the page
# (pt-br)Encontra todos os links na página
for link in soup.find_all("a", href=True): # <a href=".pdf">...</a>
    link_text = link.get_text(strip=True)

    # (en)Check if the link contains "Anexo-I" or "Anexo-II"
    # (pt-br)Verificar se o link contém "Anexo-I" ou "Anexo-II"
    if ("Anexo I" in link_text or "Anexo II" in link_text) and link["href"].endswith(".pdf"):  
        href = link["href"]

        # (en)Check if the link is relative
        # (pt-br)Verifica se o link é relativo
        if href.startswith("/"): 
            href = "https://www.gov.br" + href
        pdf_links.append(href)

# (en)Show the PDF links
# (pt-br)Mostra os links dos PDFs
for pdf_link in pdf_links:
    print("📌 Link:", pdf_link)

# (en)List to store the PDF files
# (pt-br)Lista para armazenar os arquivos PDF
pdf_files = []

# (en)Download the PDF files
# (pt-br)Baixar os arquivos PDF
for pdf_url in pdf_links:
    pdf_name = pdf_url.split("/")[-1] 
    pdf_path = os.path.join("downloads", pdf_name)

    # Fazer o download do PDF
    response = requests.get(pdf_url)

    # (en)Save the file to disk
    # (pt-br)Salva o arquivo no disco
    with open(pdf_path, "wb") as file:
        file.write(response.content)

    # (en)Show the message of success
    # (pt-br)Mostra a mensagem de sucesso
    print(f"✅ Downloaded: {pdf_name}")

    # (en)Add the path to the list
    # (pt-br)Adiciona o caminho à lista
    pdf_files.append(pdf_path)


# (en)Create a ZIP file with the downloaded files
# (pt-br)Cria um arquivo ZIP com os arquivos baixados
zip_filename = "anexos_ANS.zip"
with ZipFile(zip_filename, "w") as zipf:
    for file in pdf_files:
        zipf.write(file, os.path.basename(file))

# (en)Show the path of the ZIP file
# (pt-br)Mostra o caminho do arquivo ZIP
print(f"\n{zip_filename}")