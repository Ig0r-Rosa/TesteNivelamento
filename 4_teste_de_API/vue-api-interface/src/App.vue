# Code developed by Igor de Matos da Rosa
# Date: 2025-03-26
# Código desenvolvido por Igor de Matos da Rosa
# Data: 26/03/2025

# Question 4

<template>
  <!-- (en)Main application container -->
  <!-- (pt-br)Container principal da aplicação -->
  <div id="app">

    <!-- (en)Page title -->
    <!-- (pt-br)Título da página -->
    <h1>Consulta de Operadoras de Saúde</h1>

    <!-- (en)Search form section -->
    <!-- (pt-br)Seção do formulário de pesquisa -->
    <div class="search-container">
      <div class="search-inputs">

        <!-- (en)Field selection dropdown -->
        <!-- (pt-br)Dropdown para seleção do campo -->
        <select v-model="campoSelecionado" class="search-select">
          <option value="all">Todos os campos</option>
          <option v-for="campo in camposDisponiveis" :key="campo" :value="campo">
            {{ formatarNomeCampo(campo) }}
          </option>
        </select>
        
        <!-- (en)Search input field -->
        <!-- (pt-br)Campo de entrada para pesquisa -->
        <input 
          type="text" 
          v-model="termoPesquisa" 
          placeholder="Digite o termo de busca..."
          class="search-input"
          @keyup.enter="buscarDados"
        >
        
        <!-- (en)Search button -->
        <!-- (pt-br)Botão de pesquisa -->
        <button @click="buscarDados" class="search-button">
          Pesquisar
        </button>
      </div>
    </div>

    <!-- (en)Results section -->
    <!-- (pt-br)Seção de resultados -->
    <div v-if="carregando" class="loading">
      Carregando...
    </div>

    <div v-else>

      <!-- (en)Results found -->
      <!-- (pt-br)Resultados encontrados -->
      <div v-if="operadoras && operadoras.length > 0">
        <h2>Resultados ({{ operadoras.length }})</h2>
        
        <!-- (en)Loop through each operator result -->
        <!-- (pt-br)Loop através de cada resultado de operadora -->
        <div v-for="(operadora, index) in operadoras" :key="index" class="result-card">
          <h3>{{ operadora.Nome_Fantasia || operadora.Razao_Social }}</h3>
          <ul>

            <!-- (en)Display each field/value pair -->
            <!-- (pt-br)Exibe cada par campo/valor -->
            <li v-for="(valor, chave) in operadora" :key="chave">
              <strong>{{ formatarNomeCampo(chave) }}:</strong> 
              <span v-if="valor === null || valor === undefined">-</span>
              <span v-else>{{ valor }}</span>
            </li>
          </ul>
        </div>
      </div>
      
      <!-- (en)No results message -->
      <!-- (pt-br)Mensagem quando não há resultados -->
      <div v-else-if="termoPesquisa">
        <p class="no-results">Nenhum resultado encontrado para "{{ termoPesquisa }}"</p>
      </div>
      
      <!-- (en)Initial message before search -->
      <!-- (pt-br)Mensagem inicial antes da pesquisa -->
      <div v-else>
        <p class="initial-message">Digite um termo de pesquisa e clique em "Pesquisar"</p>
      </div>
    </div>
  </div>
</template>

<script>
// (en)Import Axios for HTTP requests
// (pt-br)Importa Axios para requisições HTTP
import axios from "axios";

export default {
  // (en)Component data properties
  // (pt-br)Propriedades de dados do componente
  data() {
    return {
      termoPesquisa: "",        // (en)Search term input / (pt-br)Termo de pesquisa
      campoSelecionado: "all",  // (en)Selected field for search / (pt-br)Campo selecionado para pesquisa
      operadoras: null,         // (en)Search results / (pt-br)Resultados da pesquisa
      carregando: false,        // (en)Loading state / (pt-br)Estado de carregamento
      camposDisponiveis: [      // (en)Available search fields / (pt-br)Campos disponíveis para pesquisa
        "Razao_Social", "UF", "CEP", "CNPJ", "Cargo_Representante", "Cidade", 
        "Complemento", "DDD", "Data_Registro_ANS", "Endereco_eletronico", 
        "Fax", "Logradouro", "Modalidade", "Nome_Fantasia", "Numero", 
        "Bairro", "Regiao_de_Comercializacao", "Registro_ANS", 
        "Representante", "Telefone"
      ]
    };
  },
  methods: {
    // (en)Formats field names for display (removes underscores)
    // (pt-br)Formata nomes de campos para exibição (remove underlines)
    formatarNomeCampo(campo) {
      return campo.replace(/_/g, ' ');
    },
    
    // (en)Main method to fetch data from API
    // (pt-br)Método principal para buscar dados da API
    async buscarDados() {
      // (en)Validate search term
      // (pt-br)Valida o termo de pesquisa
      if (!this.termoPesquisa.trim()) {
        alert("Por favor, digite um termo de pesquisa");
        return;
      }

      // (en)Set loading state and clear previous results
      // (pt-br)Define estado de carregamento e limpa resultados anteriores
      this.carregando = true;
      this.operadoras = null;

      try {
        let url;
        // (en)URL encode search term
        // (pt-br)Codifica termo de pesquisa para URL
        const termo = encodeURIComponent(this.termoPesquisa.trim());
        
        // (en)Build API URL based on selected field
        // (pt-br)Constrói URL da API baseado no campo selecionado
        if (this.campoSelecionado === "all") {
          url = `http://127.0.0.1:5000/search_all?query=${termo}`;
        } else {
          url = `http://127.0.0.1:5000/search_${this.campoSelecionado}?query=${termo}`;
        }

        // (en)Make API request
        // (pt-br)Faz requisição à API
        const response = await axios.get(url);
        console.log("Resposta da API:", response);

        // (en)Process API response
        // (pt-br)Processa resposta da API
        let data = this.processarRespostaAPI(response.data);
        
        // (en)Handle different response formats
        // (pt-br)Lida com diferentes formatos de resposta
        if (Array.isArray(data)) {
          this.operadoras = data.map(item => this.sanitizeData(item));
        } else if (typeof data === 'object' && data !== null) {
          this.operadoras = [this.sanitizeData(data)];
        } else {
          this.operadoras = [];
        }

      } catch (error) {
        console.error("Erro ao buscar dados:", error);
        alert("Ocorreu um erro ao buscar os dados. Verifique o console para mais detalhes.");
        this.operadoras = [];
      } finally {
        this.carregando = false;
      }
    },
    
    // (en)Processes raw API response string
    // (pt-br)Processa a string bruta de resposta da API
    processarRespostaAPI(jsonString) {
      try {
        // (en)Clean JSON string before parsing:
        // 1. Remove newlines
        // 2. Replace NaN with null
        // 3. Remove trailing commas
        
        // (pt-br)Limpa string JSON antes de parsear:
        // 1. Remove quebras de linha
        // 2. Substitui NaN por null
        // 3. Remove vírgulas finais
        jsonString = jsonString.replace(/\n/g, '');
        jsonString = jsonString.replace(/:\s*NaN\s*(,|\})/g, ':null$1');
        jsonString = jsonString.replace(/,\s*}/g, '}');
        jsonString = jsonString.replace(/,\s*]/g, ']');

        return JSON.parse(jsonString);
      } catch (e) {
        console.error("Erro ao processar resposta da API:", e);
        throw new Error("Dados da API estão em formato inválido");
      }
    },
    
    // (en)Sanitizes data by converting problematic values to null
    // (pt-br)Limpa dados convertendo valores problemáticos para null
    sanitizeData(obj) {
      // (en)Base case for recursion
      // (pt-br)Caso base para recursão
      if (obj === null || typeof obj !== 'object') {
        return obj;
      }

      // (en)Handle arrays
      // (pt-br)Lida com arrays
      if (Array.isArray(obj)) {
        return obj.map(item => this.sanitizeData(item));
      }

      // (en)Process object properties
      // (pt-br)Processa propriedades do objeto
      const cleanObj = {};
      for (const key in obj) {
        // (en) Convert problematic values to null
        // (pt-br) Converte valores problemáticos para null
        if (obj[key] === undefined || obj[key] === 'NaN') {
          cleanObj[key] = null;
        } else if (typeof obj[key] === 'number' && isNaN(obj[key])) {
          cleanObj[key] = null;
        } else {
          cleanObj[key] = this.sanitizeData(obj[key]);
        }
      }
      return cleanObj;
    }
  }
};
</script>

<style>
/* (en)Main app styling */
/* (pt-br)Estilos principais da aplicação */
#app {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

/* (en)Search container styles */
/* (pt-br)Estilos do container de pesquisa */
.search-container {
  margin-bottom: 30px;
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
}

.search-inputs {
  display: flex;
  gap: 10px;
}

.search-select {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.search-input {
  flex: 3;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.search-button {
  flex: 1;
  padding: 10px;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.3s;
}

.search-button:hover {
  background: #369f6e;
}

/* (en)Loading state styles */
/* (pt-br)Estilos do estado de carregamento */
.loading {
  padding: 20px;
  text-align: center;
  font-style: italic;
  color: #666;
}

/* (en)Result card styles */
/* (pt-br)Estilos dos cards de resultado */
.result-card {
  background: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.result-card h3 {
  margin-top: 0;
  color: #2c3e50;
}

.result-card ul {
  list-style: none;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 10px;
}

.result-card li {
  padding: 5px 0;
  border-bottom: 1px solid #eee;
}

/* (en) Message styles */
/* (pt-br) Estilos das mensagens */
.no-results, .initial-message {
  text-align: center;
  padding: 40px;
  color: #666;
  font-style: italic;
}
</style>