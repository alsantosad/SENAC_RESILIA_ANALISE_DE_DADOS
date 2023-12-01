CREATE DATABASE RESILIADATA;
USE RESILIADATA;

DROP DATABASE RESILIADATA;

CREATE TABLE empresa 
( 
 id_empresa INT PRIMARY KEY AUTO_INCREMENT,  
 nome_empresa VARCHAR(255) NOT NULL,  
 endereco VARCHAR(255) NOT NULL,  
 telefone VARCHAR(20) NOT NULL
);

CREATE TABLE tecnologia 
( 
 id_tecnologia INT PRIMARY KEY AUTO_INCREMENT,  
 area VARCHAR(50) NOT NULL,  
 nome_tecnologia VARCHAR(50) NOT NULL
);

CREATE TABLE tecnologia_empresa 
( 
 id_empresa INT,  
 id_tecnologia INT,  
 nivel_utilizacao INT NOT NULL  -- 1 a 5 (Sendo 1 pouco usado e 5 muito usado)
); 

CREATE TABLE colaborador 
( 
 id_colaborador INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(100) NOT NULL,  
 cargo VARCHAR(50) NOT NULL
);

CREATE TABLE colaborador_empresa 
( 
 id_colaborador INT,
 id_empresa INT,
 data_inicio DATE NOT NULL
);

-- Adicionando chaves estrangeiras com ALTER TABLE

ALTER TABLE tecnologia_empresa 
  ADD CONSTRAINT fk_tecnologia_empresa_empresa 
  FOREIGN KEY (id_empresa) REFERENCES empresa (id_empresa);

ALTER TABLE tecnologia_empresa 
  ADD CONSTRAINT fk_tecnologia_empresa_tecnologia 
  FOREIGN KEY (id_tecnologia) REFERENCES tecnologia (id_tecnologia);

ALTER TABLE colaborador_empresa 
  ADD CONSTRAINT fk_colaborador_empresa_colaborador 
  FOREIGN KEY (id_colaborador) REFERENCES colaborador (id_colaborador);

ALTER TABLE colaborador_empresa 
  ADD CONSTRAINT fk_colaborador_empresa_empresa 
  FOREIGN KEY (id_empresa) REFERENCES empresa (id_empresa);

-- Ver tabelas

SELECT * FROM empresa;
SELECT * FROM tecnologia;
SELECT * FROM tecnologia_empresa;
SELECT * FROM colaborador;
SELECT * FROM colaborador_empresa;


-- Joins
SELECT c.nome, e.nome_empresa, ce.data_inicio 
FROM colaborador c
INNER JOIN colaborador_empresa ce ON ce.id_colaborador = c.id_colaborador
INNER JOIN empresa e ON e.id_empresa = ce.id_empresa;

-- Inserir dados nas tabelas empresa e tecnologia

INSERT INTO empresa(nome_empresa, endereco, telefone) 
VALUES 
('PinkMello', 'Estrada porto Nacional 111', '2199035-2400'),
('WebZoom', 'Rua bacabal 223', '2197311-2188');

INSERT INTO tecnologia(area, nome_tecnologia) 
VALUES 
('Front End', 'HTML/CSS'),
('Analista de Dados', 'Python');

-- Inserir dados nas tabelas colaborador, tecnologia_empresa, colaborador_empresa

INSERT INTO colaborador(nome, cargo) 
VALUES 
('Ailton john', 'Developer'),
('Mendes jorgegin', 'Data Scientist');

INSERT INTO colaborador_empresa(id_colaborador, id_empresa, data_inicio) 
VALUES 
(1, 1, '2023-01-01'),
(2, 2, '2023-01-01');

INSERT INTO tecnologia_empresa(id_empresa, id_tecnologia, nivel_utilizacao) 
VALUES 
(1, 1, 4),
(1, 2, 3),
(2, 1, 5),
(2, 2, 2);