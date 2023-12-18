'''
Essas informações são colocadas em
planilhas diferentes, dificultando muitas das vezes a extração de dados
estratégicos para a empresa.
1. Gerar uma representação das entidades e seus respectivos atributos e relacionamentos;
2. Criar a modelagem do banco de dados;
3. Criar os scripts SQL para criação do banco de dados e das tabelas com seus respectivos
atributos;
4. Criar scripts SQL para inserção dos dados nas tabelas
5. Executar consultas para gerar informações estratégicas para a área de ensino da Resilia
Detalhes do projeto:

● Após a criação do banco de dados, você e sua equipe deverão inserir dados para teste do banco
de dados. Vocês deverão executar as consultas abaixo e apresentar seus resultados:
1. Selecionar a quantidade total de estudantes cadastrados no banco;
2. Selecionar quais pessoas facilitadoras atuam em mais de uma turma;
3. Crie uma view que selecione a porcentagem de estudantes com status de evasão
agrupados por turma;
4. Crie um trigger para ser disparado quando o atributo status de um estudante for atualizado
e inserir um novo dado em uma tabela de log.
● Além disso, vocês deverão pensar em mais uma pergunta que deverá ser respondida por scripts
SQL que combine pelo menos 3 tabelas.
'''

-- 

-- 1. Selecionar a quantidade total de estudantes cadastrados no banco;
SELECT COUNT(cpf) AS total_alunos
FROM aluno;

-- Total de matrículas
SELECT COUNT(matricula) AS total_matriculas
FROM matricula;

-- Ver as turmas que cada facilitador ja deu aula

SELECT DISTINCT f.nome, f.cpf_facilitador, t.sala
FROM facilitador f
INNER JOIN presenca_aluno_facilitador paf ON paf.cpf_facilitador = f.cpf_facilitador
INNER JOIN matricula m ON m.matricula = paf.matricula_aluno_fk
INNER JOIN turma t ON t.turma_pk = m.id_turma_fk;

-- 2. Selecionar quais pessoas facilitadoras atuam em mais de uma turma

SELECT f.nome, f.cpf_facilitador, COUNT(DISTINCT t.sala) AS total_turmas
FROM facilitador f
INNER JOIN presenca_aluno_facilitador paf ON paf.cpf_facilitador = f.cpf_facilitador
INNER JOIN matricula m ON m.matricula = paf.matricula_aluno_fk
INNER JOIN turma t ON t.turma_pk = m.id_turma_fk
GROUP BY f.nome, f.cpf_facilitador
HAVING COUNT(DISTINCT t.sala) > 1;

-- Contar o total de aulas ministradas por cada facilitador
SELECT f.nome, paf.cpf_facilitador, COUNT(DISTINCT paf.id_aula_facilitador) AS total_aulas_ministradas
FROM presenca_aluno_facilitador paf
INNER JOIN facilitador f ON paf.cpf_facilitador = f.cpf_facilitador
WHERE presenca_facilitador = 1
GROUP BY cpf_facilitador;

-- 3. Crie uma view que selecione a porcentagem de estudantes com status de evasão agrupados por turma;

SELECT m.matricula, t.sala, a.status
FROM avaliacao a
INNER JOIN matricula m ON m.matricula = a.matricula_aluno_fk
INNER JOIN turma t ON t.turma_pk = m.id_turma_fk;

SELECT
    t.sala,
    COUNT(CASE WHEN a.status = 'APROVADO' THEN 1 END) AS aprovados,
    COUNT(CASE WHEN a.status = 'EVADIDO' THEN 1 END) AS evadidos,
    COUNT(CASE WHEN a.status NOT IN ('APROVADO', 'EVADIDO') THEN 1 END) AS outros
FROM
    avaliacao a
INNER JOIN matricula m ON m.matricula = a.matricula_aluno_fk
INNER JOIN turma t ON t.turma_pk = m.id_turma_fk
GROUP BY
    t.sala;

-- 3. Crie uma view que selecione a porcentagem de estudantes com status de evasão agrupados por turma;

CREATE VIEW porcentagem_status AS
SELECT
    t.sala,
    COUNT(CASE WHEN a.status = 'APROVADO' THEN 1 END) AS aprovados,
    COUNT(CASE WHEN a.status = 'EVADIDO' THEN 1 END) AS evadidos,
    COUNT(CASE WHEN a.status NOT IN ('APROVADO', 'EVADIDO') THEN 1 END) AS outros,
    COUNT(*) AS total,
    ROUND(COUNT(CASE WHEN a.status = 'APROVADO' THEN 1 END) / COUNT(*) * 100, 2) AS percentual_aprovados,
    ROUND(COUNT(CASE WHEN a.status = 'EVADIDO' THEN 1 END) / COUNT(*) * 100, 2) AS percentual_evadidos,
    ROUND(COUNT(CASE WHEN a.status NOT IN ('APROVADO', 'EVADIDO') THEN 1 END) / COUNT(*) * 100, 2) AS percentual_outros
FROM
    avaliacao a
INNER JOIN matricula m ON m.matricula = a.matricula_aluno_fk
INNER JOIN turma t ON t.turma_pk = m.id_turma_fk
GROUP BY
    t.sala;

SELECT * FROM porcentagem_status;

-- Aluno -> Avaliaçao -> Diciplina - Modulo -> Curso -> Turma

-- # Tabela de Status em Geral (Ideia para 5ª Pergunta)
CREATE VIEW status_alunos AS
SELECT 
    aluno.nome AS nome_aluno,
    aluno.cpf AS cpf_aluno, 
    turma.nome_da_turma, 
    curso.nome_curso, 
    disciplina.nome AS nome_disciplina, 
    avaliacao.nota, 
    avaliacao.status
FROM aluno
INNER JOIN avaliacao ON avaliacao.cpf_fk = aluno.cpf
INNER JOIN disciplina ON disciplina.id_disciplina = avaliacao.id_disciplina_fk
INNER JOIN modulo ON modulo.id_disciplina_fk = disciplina.id_disciplina
INNER JOIN curso ON curso.id_curso = modulo.curso_fk
INNER JOIN turma ON turma.curso_fk = curso.id_curso;


-- Crie a tabela de log
CREATE TABLE log_status (
  `id_log` INT(11) PRIMARY KEY AUTO_INCREMENT,
  `matricula_fk` BIGINT(11) NOT NULL,
  `status_log` VARCHAR(100) NOT NULL,
  `data_atualizacao` DATE
);

DELIMITER //
CREATE TRIGGER tr_inserir_status
AFTER INSERT ON avaliacao
FOR EACH ROW
BEGIN
  INSERT INTO log_status (matricula_fk, status_log, data_atualizacao)
  VALUES (NEW.matricula_aluno_fk, NEW.status, NOW());
END;
//
DELIMITER ;


-- Criar uma consulta que forneça a média de notas dos alunos agrupada por curso, turma e status.

SELECT
    curso.nome_curso,
    turma.nome_da_turma,
    avaliacao.status,
    AVG(avaliacao.nota) AS media_notas
FROM
    aluno
INNER JOIN avaliacao ON avaliacao.cpf_fk = aluno.cpf
INNER JOIN disciplina ON disciplina.id_disciplina = avaliacao.id_disciplina_fk
INNER JOIN modulo ON modulo.id_disciplina_fk = disciplina.id_disciplina
INNER JOIN curso ON curso.id_curso = modulo.curso_fk
INNER JOIN turma ON turma.curso_fk = curso.id_curso
GROUP BY
    curso.nome_curso, turma.nome_da_turma, avaliacao.status;
