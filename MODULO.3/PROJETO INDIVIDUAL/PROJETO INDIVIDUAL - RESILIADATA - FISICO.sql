-- APAGAR O BANCO INTEIRO
DROP DATABASE resiliadata;

-- CRIANDO O BANCO resiliadata
CREATE DATABASE resiliadata;

-- SELECIONANDO O BANCO resiliadata
USE resiliadata;

-- CRIANDO A TABELA empresa_parceira
CREATE TABLE empresa_parceira
( 
 id_empresa_parceira INT PRIMARY KEY AUTO_INCREMENT,  
 nome_empresa VARCHAR(255) NOT NULL,  
 setor VARCHAR(255) NOT NULL
);

-- CRIANDO A TABELA tecnologia
CREATE TABLE tecnologia 
( 
 id_tecnologia INT PRIMARY KEY AUTO_INCREMENT,  
 nome_tecnologia VARCHAR(50) NOT NULL,  
 area VARCHAR(50) NOT NULL
);

-- CRIANDO A TABELA registro_tecnologia
CREATE TABLE registro_tecnologia
( 
 id_reg_tec INT PRIMARY KEY AUTO_INCREMENT,  
 id_empresa_parceira INT,  
 id_tecnologia INT NOT NULL
); 

-- CRIANDO A TABELA colaborador
CREATE TABLE colaborador 
( 
 id_colaborador INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(100) NOT NULL,  
 cargo VARCHAR(50) NOT NULL,
 id_empresa_parceiro INT
);

-- Adicionando chaves estrangeiras com ALTER TABLE

-- ADICIONANDO FK
ALTER TABLE registro_tecnologia
ADD FOREIGN KEY (id_empresa_parceira) REFERENCES empresa_parceira (id_empresa_parceira);

-- ADICIONANDO FK
ALTER TABLE registro_tecnologia
ADD FOREIGN KEY (id_tecnologia) REFERENCES tecnologia (id_tecnologia);

-- ADICIONANDO FK
ALTER TABLE colaborador
ADD FOREIGN KEY (id_empresa_parceiro)
REFERENCES empresa_parceira (id_empresa_parceira);

-- MUDANDO O NOME DE UMA COLUNA
ALTER TABLE colaborador
CHANGE COLUMN id_empresa_parceiro TO id_empresa_parceira;

-- SELECIONANDO TODOS OS ITENS DA TABELA colaborador
SELECT *
FROM colaborador;