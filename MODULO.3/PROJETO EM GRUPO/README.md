# Projeto Resilia - Banco de Dados

![Banner Resilia](Doc/bannerresilia.png)


## Descrição
Este projeto faz parte do Módulo 3 da Resilia, com o objetivo de modernizar o processo de armazenamento de dados e gerenciamento da estrutura de ensino da empresa.

## Conteúdo do Projeto
- [Contexto](#contexto)
- [Requisitos](#requisitos)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Modelo Conceitual](#modelo-conceitual)
- [Modelo Lógico](#modelo-lógico)
- [Guia do Projeto](#guia-do-projeto)
- [Como Executar](#como-executar)
- [Contribuidores](#contribuidores)
- [Licença](#licença)
- [Status](#status)
- [Download](#download)



## Contexto
O projeto envolve a modernizar o processo
de armazenamento de dados e construção para gerenciamento da estrutura
de ensino da empresa; 
Criação da modelagem do banco de dados, scripts SQL para criação e inserção de dados, além da execução de consultas estratégicas para a área de ensino da Resilia.

## Requisitos
- Representação das entidades e os respectivos atributos de cada uma delas;
- Modelagem completa do banco de dados com entidades, atributos e relacionamentos;
- Scripts SQL de criação do banco de dados e das respectivas tabelas com seus atributos e chaves;
- Scripts SQL de inserção dos dados nas respectivas tabelas;
- Scripts SQL com a resolução das 6 perguntas estratégicas da empresa.

## Funcionalidades
- Cadastro de Alunos, Facilitadores, Cursos e Turmas
- Consultas Estratégicas sobre os Dados
- Utilização de Banco de Dados para Armazenamento

## Estrutura do Projeto
O projeto está estruturado da seguinte forma:
- `index.py`: Contém o menu principal e a lógica de execução.
- `utils/`: Diretório com módulos utilitários.
  - `cores.py`: Cores para melhorar a apresentação no console.
  - `lines.py`: Funções para desenhar linhas decorativas.
  - `quiz.py`: Lógica relacionada ao quiz e armazenamento de dados.

## Modelo Conceitual

<img src="Doc/MODULO%203%20-%20PROJETO%20EM%20GRUPO%20-%20CONCEITUAL.png" alt="Modelo Conceitual" width="800">



## Modelo Lógico

<img src="Doc/MODULO%203%20-%20PROJETO%20EM%20GRUPO%20-%20LOGICO.png" alt="Modelo Lógico" width="800">



## Guia do Projeto
- [PDF com Instruções e Detalhes do Projeto](Doc/1694009852_SEDadosM3Projetoemgrupopdf.pdf)

## Download

[![Download ZIP](https://img.shields.io/badge/Download_-ZIP-green?style=for-the-badge&logo=github)](https://github.com/NewKanvas/Projeto3/archive/main.zip)


## Como Executar
### Pré-requisitos

1. Clone o repositório para a sua máquina.

2. No diretório `C:/xampp`, crie uma pasta chamada "csv" e adicione todos os arquivos CSV necessários.

### Execução dos Scripts SQL

3. Execute os scripts SQL na seguinte ordem:

   - `RESILIADATA.sql`: Criação do banco de dados e tabelas.
   - `TRIGGER.sql`: Criação de triggers para atualizações no banco.
   - `INSERT.sql`: Inserção de dados nas tabelas.

### Consultas SQL

4. Execute as consultas SQL propostas para análise exploratória.

   - `SELECT.sql` (Opcional): Consultas adicionais para análise.
   - `VIEW.sql`: Criação de views para informações estratégicas.

## Contribuidores
- [Alessandro Brito](https://github.com/alsantosad)
- [Cássio Ramos](https://github.com/NewKanvas)
- [Felipe Damico](https://github.com/FelipeDamicoCapitao)
- [Xavier Flor](naoacheiolink)

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).

## Status

![GitHub Repo Size](https://img.shields.io/github/repo-size/NewKanvas/Projeto3?style=for-the-badge&logo=github)
![GitHub last commit](https://img.shields.io/github/last-commit/NewKanvas/Projeto3?style=for-the-badge&logo=git)
[![Licence](https://img.shields.io/github/license/NewKanvas/Projeto3?style=for-the-badge)](./LICENSE)
![Downloads](https://img.shields.io/github/downloads/NewKanvas/Projeto3/total?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/NewKanvas/Projeto3?style=for-the-badge)
![Watchers](https://img.shields.io/github/watchers/NewKanvas/Projeto3?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/NewKanvas/Projeto3?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/NewKanvas/Projeto3?style=for-the-badge)
