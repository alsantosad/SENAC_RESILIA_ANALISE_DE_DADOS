# RESILIADATA - Sistema de Banco de Dados

## Descrição do Projeto

O projeto RESILIADATA tem como objetivo desenvolver um banco de dados para armazenar informações cruciais a serem utilizadas pelo sistema RESILIADATA. O sistema proporcionará suporte na avaliação das tecnologias adotadas por empresas parceiras e na identificação de seus colaboradores.

### Funcionalidades Principais

1. Cadastro de Empresas Parceiras.
2. Cadastro de Tecnologias com a opção de selecionar a área (webdev, dados, marketing, etc.).
3. Registro das tecnologias utilizadas por empresas.
4. Cadastro de Colaboradores vinculados às empresas parceiras.

## Modelagem e Respostas

### 1. Entidades Necessárias:

- Empresa Parceira
- Tecnologia
- Registro de Tecnologia (Associação entre Empresas e Tecnologias)
- Colaborador

### 2. Principais Campos e Tipos:

**Empresa Parceira:**
- id_empresa_parceira (INT, PK)
- nome_parceira (VARCHAR(255))
- endereco (VARCHAR(255))
- setor (VARCHAR(50))

**Tecnologia:**
- id_tecnologia (INT, PK)
- nome_tecnologia (VARCHAR(255))
- area (VARCHAR(50))

**Registro de Tecnologia:**
- id_registro_tecnologia (INT, PK)
- id_empresa_parceira (INT, FK referenciando Empresa Parceira)
- id_tecnologia (INT, FK referenciando Tecnologia)
- nivel_utilizacao (INT)

**Colaborador:**
- id_colaborador (INT, PK)
- nome (VARCHAR(255))
- cargo (VARCHAR(50))
- id_empresa_parceira (INT, FK referenciando Empresa Parceira)

### 3. Relacionamentos:

- Relacionamento N:N entre Empresa Parceira e Tecnologia (por meio da tabela Registro de Tecnologia).
- Relacionamento 1:N entre Empresa Parceira e Colaborador.

### 4. Simulação de Registros:

**Empresa Parceira:**
```sql
INSERT INTO empresa_parceira (nome_parceira, endereco, setor)
VALUES 
('TechSolutions', 'Av. Inovação 123', 'Tecnologia'),
('DataInsights', 'Rua da Ciência 456', 'Dados');
```

**Tecnologia:**
```sql
INSERT INTO tecnologia (nome_tecnologia, area)
VALUES 
('JavaScript', 'Web Development'),
('Python', 'Data Science');
```

**Registro de Tecnologia:**
```sql
INSERT INTO registro_tecnologia (id_empresa_parceira, id_tecnologia, nivel_utilizacao)
VALUES 
(1, 1, 4),
(1, 2, 3),
(2, 2, 5);
```

**Colaborador:**
```sql
INSERT INTO colaborador (nome, cargo, id_empresa_parceira)
VALUES 
('Maria Oliveira', 'Desenvolvedora', 1),
('José Santos', 'Cientista de Dados', 2);
```


## CONTACTS

[![Linkedin Badge](https://img.shields.io/badge/-Alessandro%20Brito-986DFF?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/alessandro-brito-220ba6266/)](https://www.linkedin.com/in/alessandro-brito-220ba6266/) 
[![Gmail Badge](https://img.shields.io/badge/-Alsantosbrito@gmail.com-986DFF?style=flat-square&logo=Gmail&logoColor=white&link=mailto:alsantosbrito@gmail.com)](mailto:alsantosbrito@gmail.com)

