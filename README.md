# Gerenciamento de Empregados e Históricos

## Descrição

Este projeto é um sistema de gerenciamento de empregados, que permite adicionar, ler, atualizar e excluir informações de empregados, trabalhos e históricos de trabalho. O sistema armazena dados em um banco de dados SQLite e fornece uma interface de linha de comando para interação.

## Funcionalidades

- **Adicionar Empregados**: Permite adicionar novos empregados com informações como nome, data de nascimento, salário e departamento.
- **Ler Empregados**: Exibe informações de um empregado específico.
- **Atualizar Empregados**: Permite atualizar informações de um empregado existente.
- **Excluir Empregados**: Remove um empregado do sistema.
- **Adicionar Trabalhos**: Permite adicionar novos trabalhos disponíveis.
- **Ler Trabalhos**: Exibe informações de um trabalho específico.
- **Atualizar Trabalhos**: Permite atualizar informações de um trabalho existente.
- **Excluir Trabalhos**: Remove um trabalho do sistema.
- **Adicionar Históricos de Trabalho**: Permite registrar o histórico de trabalho de um empregado.
- **Ler Históricos de Trabalho**: Exibe informações de um histórico específico de um empregado.
- **Atualizar Históricos de Trabalho**: Permite atualizar um registro de histórico de trabalho existente.
- **Excluir Históricos de Trabalho**: Remove um histórico de trabalho do sistema.

## Estrutura do Banco de Dados

O projeto utiliza um banco de dados SQLite com as seguintes tabelas:

### Tabela `Employee`

```sql
CREATE TABLE Employee (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(50),
    Birthday DATE,
    Salary NUMERIC(10,2),
    Department VARCHAR(50),
    JobID INTEGER,
    FOREIGN KEY(JobID) REFERENCES Job(JobID)
);
```

### Tabela `Job`

```sql
CREATE TABLE Job (
    JobID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(50),
    Description VARCHAR(255)
);
```

### Tabela `JobHistory`

```sql
CREATE TABLE JobHistory (
    JobHistoryID INTEGER PRIMARY KEY AUTOINCREMENT, 
    EmployeeID INTEGER,
    StartDate DATE,
    EndDate DATE,
    Salary NUMERIC(10,2),
    Job VARCHAR(50),
    FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID)
);
```

## Instruções de Uso

1. **Instalação**:
   - Certifique-se de ter o Python e a biblioteca `sqlite3` instalados.
   - Clone este repositório para o seu ambiente local.

2. **Criar o Banco de Dados**:
   - Execute a função `create_tables()` para criar as tabelas necessárias no banco de dados.

3. **Executar o Programa**:
   - Importe o módulo principal e utilize as funções disponíveis para interagir com o banco de dados.
   - As operações de CRUD (Criar, Ler, Atualizar e Deletar) estão disponíveis para empregados, trabalhos e históricos.

4. **Interação via Linha de Comando**:
   - Utilize as funções disponíveis para adicionar, atualizar ou consultar informações diretamente do terminal.


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
```
