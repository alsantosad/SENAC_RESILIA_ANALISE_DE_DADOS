/*
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
*/

-- 

-- 1. Selecionar a quantidade total de estudantes cadastrados no banco;
SELECT COUNT(cpf) AS total_alunos
FROM aluno;

-- Total de matrículas
SELECT COUNT(matricula) AS total_matriculas
FROM matricula;

-- 2. Selecionar quais pessoas facilitadoras atuam em mais de uma turma

SELECT f.nome, f.cpf_facilitador, COUNT(DISTINCT t.sala) AS total_turmas
FROM facilitador f
INNER JOIN presenca_aluno_facilitador paf ON paf.cpf_facilitador = f.cpf_facilitador
INNER JOIN matricula m ON m.matricula = paf.matricula_aluno_fk
INNER JOIN turma t ON t.turma_pk = m.id_turma_fk
GROUP BY f.nome, f.cpf_facilitador
HAVING COUNT(DISTINCT t.sala) > 1;

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


-- 5.# Tabela de Status de Alunos
CREATE VIEW status_alunos AS
SELECT 
    aluno.nome AS nome_aluno,
    aluno.cpf AS cpf_aluno, 
    turma.sala, 
    curso.nome_curso, 
    avaliacao.nota, 
    avaliacao.status
FROM aluno
INNER JOIN matricula on aluno.cpf = matricula.cpf_aluno_fk
INNER JOIN curso ON curso.id_curso = matricula.id_curso_fk
INNER JOIN turma ON turma.curso_fk = curso.id_curso
INNER JOIN modulo ON turma.curso_fk = modulo.curso_fk
INNER JOIN avaliacao ON modulo.id_modulo = avaliacao.id_modulo_fk
GROUP BY aluno.cpf;

SELECT * FROM status_alunos;