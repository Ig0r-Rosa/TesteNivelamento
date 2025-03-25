# Code developed by Igor de Matos da Rosa
# Date: 2025-03-25
# Código desenvolvido por Igor de Matos da Rosa
# Data: 25/03/2025

# (en)This header is used to simplify the manipulation of pdfs
# (pt-br)Este cabeçalho é usado para simplificar a manipulação de pdfs

# (en)Import the required libraries
# (pt-br)Importa as bibliotecas necessárias
import os.path
import sys
import requests
import glob
import pdfplumber
import pandas as pd

# (en)Library to extract data from HTML and XML files
# (pt-br)Biblioteca para extrair dados de arquivos HTML e XML
from bs4 import BeautifulSoup

# (en)Add the directory where the headers are located to sys.path
# (pt-br)Adiciona o diretório onde os headers estão localizado ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# (en)Class to create a ZIP file
# (pt-br)Classe para criar um arquivo ZIP
from headers.zip import zip

class pdf(zip):

    # (en)Constructor
    # (pt-br)Construtor
    def __init__(self, site = "", url= "", path = ""):
        self.__path = path
        self.__site = site
        self.__url = url
        self.__pdf_links = []
        self.__pdf_files = []


    # (en)Find the links to the PDF files
    # (pt-br)Encontra os links para os arquivos PDF
    def findPdfLinks(self, link_name = []):

        # (en)Create a directory to store the downloaded files
        # (pt-br)Cria um diretório para armazenar os arquivos baixados
        os.makedirs("pdf", exist_ok=True)

        # (en)Send a request to the URL
        # (pt-br)Envia uma requisição para a URL
        response = requests.get(self.__url)

        # (en)Check if the request was successful
        # (pt-br)Verifica se a requisição foi bem sucedida
        response.raise_for_status()

        # (en)Parse the HTML content of the page
        # (pt-br)Analisa o conteúdo HTML da página
        soup = BeautifulSoup(response.text, "html.parser")

        # (en)Find all the links in the page
        # (pt-br)Encontra todos os links na página
        for link in soup.find_all("a", href=True): # <a href=".pdf">...</a>
            link_text = link.get_text(strip=True)

            # (en)Check if the link contains link_name
            # (pt-br)Verificar se o link contém o link_name
            for name in link_name:
                if (name in link_text) and link["href"].endswith(".pdf"):  
                    href = link["href"]

                    # (en)Check if the link is relative
                    # (pt-br)Verifica se o link é relativo
                    if href.startswith("/"): 
                        href = self.__site + href
                    self.__pdf_links.append(href)

                    # (en)Protect to repeat the same link
                    # (pt-br)Protege para não repetir o mesmo link
                    break

        # (en)Show the PDF links
        # (pt-br)Mostra os links dos PDFs
        for pdf_link in self.__pdf_links:
            print("📌 Link:", pdf_link)


    # (en)Download the PDF files
    # (pt-br)Armazena os links para os arquivos PDF
    def downloadPdf(self):

        # (en)Create a directory to store the downloaded files
        # (pt-br)Cria um diretório para armazenar os arquivos baixados
        os.makedirs("pdf", exist_ok=True)

        # (en)Download the PDF files
        # (pt-br)Baixa os arquivos PDF
        for pdf_link in self.__pdf_links:
            pdf_name = pdf_link.split("/")[-1]
            pdf_path = os.path.join("pdf", pdf_name)

            # (en)Send a request to the PDF link
            # (pt-br)Envia uma requisição para o link do PDF
            response = requests.get(pdf_link)

            # (en)Check if the request was successful
            # (pt-br)Verifica se a requisição foi bem sucedida
            response.raise_for_status()

            # (en)Save the PDF file
            # (pt-br)Salva o arquivo PDF
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(response.content)

            # (en)Show the path of the downloaded PDF file
            # (pt-br)Mostra o caminho do arquivo PDF baixado
            print(f"\n✅ The PDF file is downloaded in directory {pdf_path}!")

            # (en)Add the path to the list
            # (pt-br)Adiciona o caminho à lista
            self.__pdf_files.append(pdf_path)


    # (en)Get the PDF files
    # (pt-br)Obtém os arquivos PDF
    def getPdfFiles(self):
        return self.__pdf_files
    

    # (en)Get the PDF links
    # (pt-br)Obtém os links dos PDFs
    def getPdfLinks(self):
        return self.__pdf_links
    
    # (en)Set the files to zip and zip
    # (pt-br)Define os arquivos para zipar e zipa
    def setFileToZipAndZip(self, zipFileName = "pdf.zip"):
        self._files_to_zip = self.__pdf_files
        self.zip_files(zipFileName)
    

    # (en)Find the PDF files from the path
    # (pt-br)Encontra os arquivos PDF do caminho
    def findPdfFromPath(self, nameFile = "/*.pdf", removeFiles = ""):
        self.__pdf_files = glob.glob(self.__path + nameFile)

        # (en)Remove files that contain removeFiles
        # (pt-br)Remove arquivos que contém removeFiles
        if removeFiles != "":
            self.__pdf_files = [file for file in self.__pdf_files if removeFiles not in file]

    
    def extractTable(self, columns):

        # (en)Check if there are PDF files
        # (pt-br)Verifica se existem arquivos PDF
        if self.__pdf_files:
            # (en)Opening the PDF file
            # (pt-br)Abrindo o arquivo PDF
            with pdfplumber.open(self.__pdf_files[0]) as pdf:

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
            df = pd.DataFrame(all_data, columns=columns)

            # (en)Show the first lines to check if the extraction was done correctly
            # (pt-br)Mostra as primeiras linhas para verificar se a extração foi feita corretamente
            print(df.head())
            
            # (en)Return the DataFrame
            # (pt-br)Retorna o DataFrame
            return df
        
        else:
            print("❌ No valid PDF files found!")
            return None
        

    # (en)Find the legends in the PDF files
    # (pt-br)Encontra as legendas nos arquivos PDF
    def findIn(self, findField = "" ,fields = []):
        legends = {}
        for file in self.__pdf_files:
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()

                    # (en)Search for keywords and capture the descriptions
                    # (pt-br)Procura pelas palavras-chave e captura as descrições
                    if findField in text:
                        for field in fields:
                            # (en)Ensure the field is found after the findField keyword
                            # (pt-br)Verifica se o campo é encontrado após a palavra-chave findField
                            if field in text:
                                try:
                                    # (en)Capture the description after the field and handle exceptions
                                    # (pt-br)Captura a descrição após o campo e trata exceções
                                    start_idx = text.split(findField)[1]
                                    legends[field] = start_idx.split(field)[1].split("\n")[0].strip()
                                except IndexError:
                                    legends[field] = "Descrição não encontrada"
        return legends

    