# Sis_Cadastro_Escola

- Esse código é um Sistema de Cadastro de escolas gerado a partir do Terminal. Com ele, é possível fazer um Data Base, onde é possível realizar os comandos CRUD: criando, lendo, atualizando e deletando dados.

- Como usar: através da execução do arquivo principal "main.py", será gerado um Menu que orienta cada comandos, como demonstrado abaixo:
```python
===================MENU===================

[1] - Salas
[2] - Alunos
[3] - Notas

[0] - Sair

===========================================
```

 De acordo com o comando selecionado, é apresentado o menu dos comandos `Salas`, `Alunos`, `Notas` ou apenas "Sair". Dentre essas três primeiras opções, é possível visualizar um dos seguintes menus:
- `Salas`

```python
 ==================SALAS===================

[1] - Listar
[2] - Deletar
[3] - Cadastrar
[4] - Voltar

[0] - Sair

===========================================
```

- `Alunos`

```python
=================ALUNOS===================

[1] - Listar
[2] - Deletar
[3] - Cadastrar
[4] - Voltar

[0] - Sair

===========================================
```
- `Notas`

```python
===================NOTAS===================

[1] - Listar
[2] - Deletar
[3] - Cadastrar
[4] - Voltar

[0] - Sair

===========================================
```

- No código, foram testados valores que podem exemplificar parte da tabela, como no exemplo a seguir, em `Salas`.

```python
========================= LISTAGEM =========================
|ID   |QTD_ALUNO |PROFESSOR           |ATIVO|ANO  |
|1    |79        |Mauricio            |S    |1B   |
|9    |50        |Emanuel             |S    |1B   |
|10   |50        |Aurélio             |S    |6B   |
|11   |60        |Renato              |S    |2B   |
|12   |50        |Valdemar            |S    |2D   |
|13   |67        |Ari                 |S    |5D   |
|14   |20        |Aldemiro            |S    |5C   |
============================================================
Pressione qualquer tecla para continuar........
```
- Também em `Alunos`:

```python
========================= LISTAGEM =========================
|ID   |NOME                |DNS            |SEXO |ID_SALA |
|1    |Flavio Alladin      |1980-01-02     |M    |1       |
|9    |Agostinho           |2001-02-09     |M    |9       |
|10   |Karina              |2001-08-05     |F    |10      |
|11   |Kleber              |2004-03-11     |M    |11      |
|12   |Breno               |2001-08-19     |M    |12      |
============================================================
Pressione qualquer tecla para continuar........
```

- E `Notas`:
```python
========================= LISTAGEM =========================
|ID   |TRIMESTRE |ID_ALUNO  |NOTA |MATERIA             |
|9    |1         |9         |6    |Geometria           |
|10   |2         |10        |3    |História            |
|11   |1         |11        |6    |Matemática          |
|12   |3         |12        |7    |Português           |
============================================================
```

- Nos IDs, os valores de exemplo começam a partir do 9, porque foi testado também a função delete.

- O arquivo que executa o código é o ``main.py``.

- O arquivo de output é o Bando de Dados.

## Ferramentas

- Na criação do Banco de Dados, foi usado o Sistema Gerenciador de Banco de Dados (SGBD): Postgres.

- Para a criação e a excussão do output dos comandos, será necessário criar um Banco de Dados, chamado "Escola", pelo adminpg4 é possível em: `Databases > Create > Database...`.

- Para a criação das tabelas a serem usadas, foi usado o seguinte código:

```sql
CREATE TABLE IF NOT EXISTS salas(
    id SERIAL NOT NULL,
    qtd_alunos INT NOT NULL,
    professor VARCHAR (50) NOT NULL,
    ativa CHAR (5) NOT NULL,
    ano VARCHAR (5) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE alunos(
    id SERIAL NOT NULL,
    nome VARCHAR (50) NOT NULL,
    dns DATE NOT NULL,
    sexo CHAR (5) NOT NULL,
    id_sala SERIAL NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_sala) REFERENCES salas (id)
);

CREATE TABLE notas(
    id SERIAL NOT NULL,
    trimestre INT NOT NULL,
    id_aluno SERIAL NOT NULL,
    nota INT NOT NULL,
    materia VARCHAR (50) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_aluno) REFERENCES alunos (id)
);
```

- Como configurar no Postgres: para a integração com o Postgres, o código Python deve estar com as informações de acesso coincidentes, podendo serem definidas na função ``IniciarPsycopg()``, como é ilustrado abaixo:

```python
def IniciarPsycopg():
    conn = psycopg2.connect(
        database="Escola",
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
        )
        
    conn.autocommit = True

    cursor = conn.cursor()
    
    return cursor, conn
```

- Aqui é possível tanto alterar essas informações para a integração, mudando nesta função o nome do Data Base, por exemplo, caso queira quanto segui-las e executar da mesma forma como a já feita.

## Bibliotecas

- Para utilizar o código, é necessário instalar as bibliotecas, com a escrita, no Terminal: pip install -r requirements.txt, que irá instalar todas as bibliotecas necessárias.

| Command | Description |
| --- | --- |
| pip install -r requirements.txt | Irá instalar todas as bibliotecas necessárias |

