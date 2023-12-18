DROP DATABASE IF EXISTS RESILIADATA;
CREATE DATABASE RESILIADATA;
USE RESILIADATA;

CREATE TABLE instituicao (
  `unidade` INT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `endereco` VARCHAR(250) NOT NULL,
  `nome_unidade` VARCHAR(200) NOT NULL);

CREATE TABLE aluno (
  `nome` VARCHAR(200) NOT NULL,
  `cpf` BIGINT(11) PRIMARY KEY NOT NULL,
  `idade` INT(3) NOT NULL,
  `genero` VARCHAR(100) NOT NULL,
  `email` VARCHAR(250) NOT NULL);

CREATE TABLE matricula (
  `matricula` INT(11) PRIMARY KEY NOT NULL,
  `unidade_fk` INT(11) NOT NULL,
  `id_curso_fk` INT(11) NOT NULL,
  `id_turma_fk` INT(11) NOT NULL,
  `status` VARCHAR(100) NOT NULL,
  `cpf_aluno_fk`  BIGINT(11) NOT NULL);

CREATE TABLE curso (
  `id_curso` INT(11) PRIMARY KEY NOT NULL,
  `nome_curso` VARCHAR(200) NOT NULL,
  `duracao` VARCHAR(100) NOT NULL,
  `total_dias` INT(11) NOT NULL);

CREATE TABLE turma (
  `curso_fk` INT(11) NOT NULL,
  `turma_pk` INT(3) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `sala` INT(3) NOT NULL);

CREATE TABLE monitor (
  `cpf_monitor`  BIGINT(11) PRIMARY KEY NOT NULL,
  `nome` VARCHAR(200) NOT NULL,
  `idade` INT(3) NOT NULL,
  `genero` VARCHAR(100) NOT NULL,
  `email` VARCHAR(250) NOT NULL);

CREATE TABLE facilitador (
  `cpf_facilitador`  BIGINT(11) PRIMARY KEY NOT NULL,
  `nome` VARCHAR(200),
  `idade` INT(3) NOT NULL,
  `genero` VARCHAR(100) NOT NULL,
  `especializacao` VARCHAR(200) NOT NULL,
  `email` VARCHAR(250) NOT NULL);

CREATE TABLE modulo (
  `curso_fk` INT(11) NOT NULL,
  `id_modulo` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `numero_modulo` INT(11) NOT NULL,
  `qt_aula` INT(11) NOT NULL,
  `carga_horaria` INT(11) NOT NULL,
  `id_disciplina_fk` INT(11) NOT NULL);

CREATE TABLE disciplina (
  `id_disciplina` INT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `nome` VARCHAR(200) NOT NULL);

CREATE TABLE presenca_aluno_monitor  (
  `id_aula_monitor` INTEGER(200) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `data` DATE NOT NULL,
  `cpf_monitor`  BIGINT(11) NOT NULL,
  `matricula_aluno_fk` INT(11) NOT NULL,
  `presenca_monitor` BOOLEAN NOT NULL DEFAULT 0,
  `modulo_fk` INT(11) NOT NULL);

CREATE TABLE presenca_aluno_facilitador (
  `id_aula_facilitador` INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `data` DATE NOT NULL,
  `cpf_facilitador`  BIGINT(11) NOT NULL,
  `matricula_aluno_fk` INT(11) NOT NULL,
  `presenca_facilitador` BOOLEAN NOT NULL DEFAULT 0,
  `modulo_fk` INT(10) NOT NULL);

CREATE TABLE presenca (
  `id_presenca` INT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `matricula_aluno_fk` INT(11) NOT NULL,
  `data` DATE NOT NULL,
  `modulo_fk` INT(11) NOT NULL,
  `id_aula_facilitador_fk` INT(11) NOT NULL,
  `id_aula_monitor_fk` INT(11) NOT NULL,
  `presenca_facilitador_fk` BOOLEAN NOT NULL DEFAULT 0,
  `presenca_monitor_fk` BOOLEAN NOT NULL DEFAULT 0,
  `presenca_modulo` INT(11));

CREATE TABLE avaliacao (
  `id_avaliacao` INT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `matricula_aluno_fk` INT(11) NOT NULL,
  `nota` INT(11) NOT NULL,
  `status` VARCHAR(100) NOT NULL,
  `total_presencas` INT(11) NOT NULL DEFAULT 0,
  `id_modulo_fk` INT NOT NULL);

-- Adicionando chaves estrangeiras
-- Matrícula
ALTER TABLE matricula 
  ADD CONSTRAINT fk_matricula_unidade 
  FOREIGN KEY (unidade_fk) REFERENCES instituicao(unidade);

ALTER TABLE matricula 
  ADD CONSTRAINT fk_matricula_curso 
  FOREIGN KEY (id_curso_fk) REFERENCES curso(id_curso);

ALTER TABLE matricula 
  ADD CONSTRAINT fk_matricula_aluno 
  FOREIGN KEY (cpf_aluno_fk) REFERENCES aluno(cpf);

ALTER TABLE matricula
ADD CONSTRAINT fk_matricula_turma
FOREIGN KEY (id_turma_fk) REFERENCES turma(turma_pk);

-- Turma
ALTER TABLE turma 
  ADD CONSTRAINT fk_turma_curso 
  FOREIGN KEY (curso_fk) REFERENCES curso(id_curso);

-- Módulo
ALTER TABLE modulo 
  ADD CONSTRAINT fk_modulo_curso 
  FOREIGN KEY (curso_fk) REFERENCES curso(id_curso);

ALTER TABLE modulo 
  ADD CONSTRAINT fk_modulo_disciplina 
  FOREIGN KEY (id_disciplina_fk) REFERENCES disciplina(id_disciplina);

-- Presença
ALTER TABLE presenca 
  ADD CONSTRAINT fk_presenca_matricula
  FOREIGN KEY (matricula_aluno_fk) REFERENCES matricula(matricula);

ALTER TABLE presenca 
  ADD CONSTRAINT fk_presenca_facilitador 
  FOREIGN KEY (id_aula_facilitador_fk) REFERENCES presenca_aluno_facilitador(id_aula_facilitador);

ALTER TABLE presenca 
  ADD CONSTRAINT fk_presenca_monitor 
  FOREIGN KEY (id_aula_monitor_fk) REFERENCES presenca_aluno_monitor(id_aula_monitor);

ALTER TABLE presenca  
  ADD CONSTRAINT fk_presenca_modulo 
  FOREIGN KEY (modulo_fk) REFERENCES modulo(id_modulo);

-- Presença Aluno Monitor
ALTER TABLE presenca_aluno_monitor  
  ADD CONSTRAINT fk_presenca_aluno_monitor_modulo 
  FOREIGN KEY (modulo_fk) REFERENCES modulo(id_modulo);


ALTER TABLE presenca_aluno_monitor  
  ADD CONSTRAINT fk_presenca_aluno_monitor_monitor 
  FOREIGN KEY (cpf_monitor) REFERENCES monitor(cpf_monitor);

ALTER TABLE presenca_aluno_monitor 
  ADD CONSTRAINT fk_presenca_aluno_monitor_matricula
  FOREIGN KEY (matricula_aluno_fk) REFERENCES matricula(matricula);

-- Presença Aluno Facilitador
ALTER TABLE presenca_aluno_facilitador 
  ADD CONSTRAINT fk_presenca_aluno_facilitador_facilitador 
  FOREIGN KEY (cpf_facilitador) REFERENCES facilitador(cpf_facilitador);

ALTER TABLE presenca_aluno_facilitador 
  ADD CONSTRAINT fk_presenca_aluno_facilitador_modulo 
  FOREIGN KEY (modulo_fk) REFERENCES modulo(id_modulo);

ALTER TABLE presenca_aluno_facilitador 
  ADD CONSTRAINT fk_presenca_aluno_facilitador_matricula
  FOREIGN KEY (matricula_aluno_fk) REFERENCES matricula(matricula);

-- Avaliação
ALTER TABLE avaliacao 
  ADD CONSTRAINT fk_avaliacao_matricula
  FOREIGN KEY (matricula_aluno_fk) REFERENCES matricula(matricula);

ALTER TABLE avaliacao 
  ADD CONSTRAINT fk_avaliacao_modulo
  FOREIGN KEY (id_modulo_fk) REFERENCES modulo(id_modulo);