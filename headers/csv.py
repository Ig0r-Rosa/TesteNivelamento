# Code developed by Igor de Matos da Rosa
# Date: 2025-03-25
# Código desenvolvido por Igor de Matos da Rosa
# Data: 25/03/2025

# (en)This header is used to simplify the manipulation of csv
# (pt-br)Este cabeçalho é usado para simplificar a manipulação de csv

# (en)Import the required libraries
# (pt-br)Importa as bibliotecas necessárias
import os.path
import sys

# (en)Add the directory where the headers are located to sys.path
# (pt-br)Adiciona o diretório onde os headers estão localizado ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# (en)Class to create a ZIP file
# (pt-br)Classe para criar um arquivo ZIP
from headers.zip import zip

class csv(zip):
    
    # (en)Constructor
    # (pt-br)Construtor
    def __init__(self, data, name = ""):
        self.__dataFrame = data
        self.__path = "./data/" + name + ".csv"
    

    # (en)Save the extracted data to a CSV file
    # (pt-br)Salvar os dados extraídos em um arquivo CSV
    def saveCsv(self):
            
            # (en)Ensure the 'data' directory exists before saving the CSV
            # (pt-br)Garantir que o diretório 'data' exista antes de salvar o arquivo CSV
            os.makedirs(os.path.dirname(self.__path), exist_ok=True)
            self.__dataFrame.to_csv(self.__path, index=False)
            
            # (en)Show the path of the CSV file
            # (pt-br)Mostra o caminho do arquivo CSV
            print(f"\n✅ The CSV file is created in directory {self.__path}!")


    # (en)Set the files to zip and zip
    # (pt-br)Define os arquivos para zipar e zipa
    def setTheZipAndZip(self, zip_name = ".zip"):
         self._files_to_zip = [self.__path]
         self.zip_files(zip_name)


    