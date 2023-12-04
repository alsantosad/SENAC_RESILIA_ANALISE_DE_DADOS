-- Inserir dados nas tabelas empresa_parceira
-- nome_empresa, setor
INSERT INTO empresa_parceira(nome_empresa, setor) 
VALUES 
('TechCorp', 'Avenida Inovação 123'),
('GlobalTech', 'Rua da Tecnologia 456'),
('DataSolutions', 'Praça da Inovação 789');

-- Inserir dados nas tabelas tecnologia
-- nome_tecnologia, area
INSERT INTO tecnologia (nome_tecnologia, area) 
VALUES 
('Java', 'Desenvolvimento de Software'),
('React', 'Desenvolvimento Web'),
('Python', 'Ciência de Dados'),
('Swift', 'Desenvolvimento de Aplicativos Móveis'),
('SQL', 'Banco de Dados');


-- Inserir dados nas tabelas registro_tecnologia
-- id_empresa_parceira, id_tecnologia
INSERT INTO registro_tecnologia (id_empresa_parceira, id_tecnologia) 
VALUES 
(1, 2),
(2, 3),
(1, 1);


-- Inserir dados nas tabelas colaborador
-- nome, cargo, id_empresa_parceiro

-- Colaborador 1
INSERT INTO colaborador (nome, cargo, id_empresa_parceira) 
VALUES 
('João Silva', 'Desenvolvedor', 1); -- João Silva é um desenvolvedor na empresa PinkMello
-- Colaborador 2
INSERT INTO colaborador (nome, cargo, id_empresa_parceira) 
VALUES 
('Ana Souza', 'Analista de Dados', 2); -- Ana Souza é uma analista de dados na empresa WebZoom
-- Colaborador 3
INSERT INTO colaborador (nome, cargo, id_empresa_parceira) 
VALUES 
('Carlos Santos', 'Arquiteto de Software', 1); -- Carlos Santos é um arquiteto de software na empresa PinkMello
