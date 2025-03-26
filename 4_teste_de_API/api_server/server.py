# Code developed by Igor de Matos da Rosa
# Date: 2025-03-26
# Código desenvolvido por Igor de Matos da Rosa
# Data: 26/03/2025

# Question 4

# (en)Importing the required libraries
# (pt-br)Importa as bibliotecas necessárias
from flask import Flask, jsonify, request
import pandas as pd

# (en)Initializing the Flask application
# (pt-br)Inicia o aplicativo Flask
app = Flask(__name__)

# (en) Load the CSV data
# (pt-br) Carregar os dados do arquivo CSV
# Ensure the file path is correct, and delimiters are appropriately set.
df = pd.read_csv('./data/Relatorio_cadop.csv', delimiter=';')

# (en)Search all fields in .csv file
# (pt-br)Pesquisa em todos os campos do arquivo .csv
# ex: http://127.0.0.1:5000/search_all?query=Unimed
@app.route('/search_all', methods=['GET'])
def search_all():

    # (en)Retrieve the search query from the request parameters
    # (pt-br)Recupere a consulta de pesquisa dos parâmetros da solicitação
    search_term = request.args.get('query', '')

    # (en)Validate if the search term is provided
    # (pt-br)Validar se o termo de pesquisa foi fornecido
    if not search_term:
        return jsonify({'error': 'Query parameter is required'}), 400

    # (en)Perform a case-insensitive search across all columns
    # (pt-br)Realiza uma busca sem considerar maiúsculas/minúsculas em todas as colunas
    results = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False, na=False).any(), axis=1)]
    
    # (en)Return the results as a JSON response
    # (pt-br)Retorna os resultados como uma resposta JSON
    return jsonify(results.to_dict(orient='records'))
# -------------------- #


# (en)Search a specific field in the .csv file
# (pt-br)Pesquisa em um campo específico do arquivo .csv
# ex: http://127.0.0.1:5000/search_Cidade?query=São Paulo
@app.route('/search_<campo>', methods=['GET'])
def search_field(campo):

    # (en) Retrieve the search query from the request parameters
    # (pt-br) Recupere a consulta de pesquisa dos parâmetros da solicitação
    search_term = request.args.get('query', '')

    # (en) Validate if the search term is provided
    # (pt-br) Validar se o termo de pesquisa foi fornecido
    if not search_term:
        return jsonify({'error': 'Query parameter is required'}), 400

    # (en) Check if the specified field exists in the dataframe
    # (pt-br) Verifica se o campo especificado existe no dataframe
    if campo not in df.columns:
        return jsonify({'error': f'Column "{campo}" not found'}), 404

    # (en) Perform a case-insensitive search within the specified field
    # (pt-br) Realiza uma busca sem considerar maiúsculas/minúsculas no campo especificado
    results = df[df[campo].astype(str).str.contains(search_term, case=False, na=False)]
    
    # (en) Return the results as a JSON response
    # (pt-br) Retorna os resultados como uma resposta JSON
    return jsonify(results.to_dict(orient='records'))
# -------------------- #


# (en) Run the Flask app
# (pt-br) Inicia o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)