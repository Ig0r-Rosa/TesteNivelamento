# Code developed by Igor de Matos da Rosa
# Date: 2025-03-25
# Código desenvolvido por Igor de Matos da Rosa
# Data: 25/03/2025

# (en)This header is used to simplify the zip process
# (pt-br)Este cabeçalho é usado para simplificar o processo de zip

# (en)Import the required library
# (pt-br)Importa a biblioteca necessária
from zipfile import ZipFile
from os import path

class zip:

    # (en)Constructor
    # (pt-br)Construtor
    def __init__(self):
        self._files_to_zip = []


    # (en)Add files to the list to be zipped and zip
    # (pt-br)Adiciona arquivos à lista para serem zipados e zipa
    def zip_files(self, zip_name, zip_folder = "/"):

        # (en)If the folder does not exist, create it
        # (pt-br)Se a pasta não existe, cria ela
        if not path.exists(zip_folder):
            path.makedirs(zip_folder, exist_ok=True)

        # (en)Zip the files
        # (pt-br)Zipa os arquivos
        with ZipFile(zip_name, 'w') as zip:
            for file in self._files_to_zip:
                zip.write(file, path.join(zip_folder, path.basename(file)))

        # (en)Show the path of the ZIP file
        # (pt-br)Mostra o caminho do arquivo ZIP
        print(f"\n✅ The Zip file is created in directory {zip_folder + zip_name}!")
            