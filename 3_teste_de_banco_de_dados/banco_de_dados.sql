-- Code developed by Igor de Matos da Rosa
-- Date: 2025-03-25
-- Código desenvolvido por Igor de Matos da Rosa
-- Data: 25/03/2025

-- Question 3

-- (en)Create a database
-- (pt-br)Cria o banco de dados
CREATE DATABASE IF NOT EXISTS banco_de_dados;
USE banco_de_dados;

-- (en)Create the table for operators (operadoras)
-- (pt-br)Cria a tabela para as operadoras
CREATE TABLE if not exists operadoras(
    registro_ans BIGINT UNIQUE primary key,  -- (en) ANS Registration number / (pt-br) Número de Registro ANS
    cnpj VARCHAR(50),  -- (en) CNPJ / (pt-br) CNPJ
    razao_social VARCHAR(255),  -- (en) Social reason / (pt-br) Razão Social
    nome_fantasia VARCHAR(255),  -- (en) Trade name / (pt-br) Nome Fantasia
    modalidade VARCHAR(100),  -- (en) Modality / (pt-br) Modalidade
    logradouro VARCHAR(255),  -- (en) Street address / (pt-br) Logradouro
    numero VARCHAR(20),  -- (en) Number / (pt-br) Número
    complemento VARCHAR(255),  -- (en) Complement / (pt-br) Complemento
    bairro VARCHAR(255),  -- (en) Neighborhood / (pt-br) Bairro
    cidade VARCHAR(255),  -- (en) City / (pt-br) Cidade
    uf CHAR(50),  -- (en) State / (pt-br) UF
    cep VARCHAR(50),  -- (en) ZIP code / (pt-br) CEP
    ddd VARCHAR(50),  -- (en) Area code / (pt-br) DDD
    telefone VARCHAR(50),  -- (en) Phone / (pt-br) Telefone
    fax VARCHAR(50),  -- (en) Fax / (pt-br) Fax
    endereco_eletronico VARCHAR(255),  -- (en) Email address / (pt-br) Endereço eletrônico
    representante VARCHAR(255),  -- (en) Representative / (pt-br) Representante
    cargo_representante VARCHAR(255),  -- (en) Representative's role / (pt-br) Cargo do Representante
    regiao_comercializacao VARCHAR(255),  -- (en) Commercialization region / (pt-br) Região de Comercialização
    data_registro_ans DATE  -- (en) ANS registration date / (pt-br) Data de Registro ANS
);

-- (en)Create the table for financial demonstrations (demonstracoes_contabeis)
-- (pt-br)Cria a tabela para demonstrações contábeis
CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    data DATE,  -- (en)Date of the record -- (pt-br)Data do registro
    registro_ans BIGINT,  -- (en)ANS registration number -- (pt-br)Número de registro ANS
    cd_conta_contabil VARCHAR(50),  -- (en)Accounting account code -- (pt-br)Código da conta contábil
    descricao VARCHAR(255),  -- (en)Description of the transaction -- (pt-br)Descrição da transação
    vl_saldo_inicial DECIMAL(15, 2),  -- (en)Initial balance -- (pt-br)Saldo inicial
    vl_saldo_final DECIMAL(15, 2)  -- (en)Final balance -- (pt-br)Saldo final
);

-- (en) Import CSV data into 'operadoras' and 'demonstracoes_contabeis'
-- (pt-br) Importar dados do CSV para 'operadoras' e 'demonstracoes_contabeis'

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/arquivos/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/arquivos/1T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows
(@data, @registro_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @registro_ans,
    cd_conta_contabil = @cd_conta_contabil,
    descricao = @descricao,
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
    

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/arquivos/2t2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows
(@data, @registro_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @registro_ans,
    cd_conta_contabil = @cd_conta_contabil,
    descricao = @descricao,
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/arquivos/3T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows
(@data, @registro_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @registro_ans,
    cd_conta_contabil = @cd_conta_contabil,
    descricao = @descricao,
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/arquivos/4T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows
(@data, @registro_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data = STR_TO_DATE(@data, '%d/%m/%Y'),
    registro_ans = @registro_ans,
    cd_conta_contabil = @cd_conta_contabil,
    descricao = @descricao,
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/arquivos/1T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows
(@data, @registro_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @registro_ans,
    cd_conta_contabil = @cd_conta_contabil,
    descricao = @descricao,
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/arquivos/2T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows
(@data, @registro_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @registro_ans,
    cd_conta_contabil = @cd_conta_contabil,
    descricao = @descricao,
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/arquivos/3T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows
(@data, @registro_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @registro_ans,
    cd_conta_contabil = @cd_conta_contabil,
    descricao = @descricao,
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/arquivos/4T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows
(@data, @registro_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @registro_ans,
    cd_conta_contabil = @cd_conta_contabil,
    descricao = @descricao,
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- (en) Query to count the total records in 'demonstracoes_contabeis' table
-- (pt-br) Consulta para contar o total de registros na tabela 'demonstracoes_contabeis'
SELECT 
    COUNT(*) AS total_registros
FROM demonstracoes_contabeis;

-- (en) Query to count the total records in 'operadoras' table
-- (pt-br) Consulta para contar o total de registros na tabela 'operadoras'
SELECT 
    COUNT(*) AS total_registros
FROM operadoras;

-- (en) Query to find the top 10 operators with the highest expenses in the last quarter
-- (pt-br) Consulta para encontrar as 10 operadoras com as maiores despesas no último trimestre
-- (en) Access locally
-- (pt-br) Acessar localmente
SELECT o.razao_social, 
       SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o 
    ON d.registro_ans = o.registro_ans
WHERE d.descricao LIKE '%EVENTOS%SINISTROS%CONHECIDOS%OU%AVISADOS%DE%ASSISTÊNCIA%A%SAÚDE%MEDICO%HOSPITALAR%'
  AND data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

-- (en) Query to export the top 10 operators with the highest expenses in the last quarter into a file
-- (pt-br) Consulta para exportar as 10 operadoras com maiores despesas no último trimestre para um arquivo
SELECT o.razao_social, 
       SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o 
    ON d.registro_ans = o.registro_ans
WHERE d.descricao LIKE '%EVENTOS%SINISTROS%CONHECIDOS%OU%AVISADOS%DE%ASSISTÊNCIA%A%SAÚDE%MEDICO%HOSPITALAR%'
  AND data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/resultado_trimestral.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

-- (en) Query to find the top 10 operators with the highest expenses in the last year
-- (pt-br) Consulta para encontrar as 10 operadoras com as maiores despesas no último ano
-- (en) Access locally
-- (pt-br) Acessar localmente
SELECT o.razao_social, 
       SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o 
    ON d.registro_ans = o.registro_ans
WHERE d.descricao LIKE '%EVENTOS%SINISTROS%CONHECIDOS%OU%AVISADOS%DE%ASSISTÊNCIA%A%SAÚDE%MEDICO%HOSPITALAR%'
  AND data BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

-- (en) Query to export the top 10 operators with the highest expenses in the last year into a file
-- (pt-br) Consulta para exportar as 10 operadoras com maiores despesas no último ano para um arquivo
SELECT o.razao_social, 
       SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o 
    ON d.registro_ans = o.registro_ans
WHERE d.descricao LIKE '%EVENTOS%SINISTROS%CONHECIDOS%OU%AVISADOS%DE%ASSISTÊNCIA%A%SAÚDE%MEDICO%HOSPITALAR%'
  AND data BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY o.razao_social
ORDER BY total_despesas DESC
LIMIT 10
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/resultado_anual.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

