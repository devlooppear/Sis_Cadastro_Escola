import os
from comum import sair
from db import CONN,CURSOR

ALUNOS ="""=================ALUNOS===================

[1] - Listar
[2] - Deletar
[3] - Cadastrar
[4] - Voltar

[0] - Sair

===========================================
"""

def alunos():
    opcao_alunos = -1

    while True:
        os.system("cls")
        if opcao_alunos != -1:
            print("Opção Inválida!")
        print(ALUNOS)
        opcao_alunos = int(input('Escolha uma opção: '))
        if opcao_alunos == 1:
            listar_alunos()
            opcao_alunos = -1
        elif opcao_alunos == 2:
            deletar_alunos()
            opcao_alunos = -1
        elif opcao_alunos == 3:
            cadastrar_alunos()
            opcao_alunos = -1
        elif opcao_alunos == 4:
            return
        elif opcao_alunos == 0:
            sair()

def listar_alunos():

    os.system("cls")

    print(f"{'='*25} LISTAGEM {'='*25}")
    COLUNAS = [("ID",5),("NOME",20),("DNS",15),("SEXO",5),("ID_SALA",8)]
    print("|",end="")
    for col in COLUNAS:
        print(col[0] + " "*(col[1]-len(col[0])),end="|")
    
    print()

    CURSOR.execute("select * from alunos")
    db_alunos = CURSOR.fetchall()

    for alunos in db_alunos:
        print("|",end="")
        print(str(alunos[0]) + " "*(5-len(str(alunos[0]))),end="|")
        print(str(alunos[1]) + " "*(20-len(str(alunos[1]))),end="|")
        print(str(alunos[2]) + " "*(15-len(str(alunos[2]))),end="|")
        print(str(alunos[3]) + " "*(5-len(str(alunos[3]))),end="|")
        print(str(alunos[4]) + " "*(8-len(str(alunos[4]))),end="|")
        print()
    
    print(f"{'='*60}")
    if True:
        input('Pressione qualquer tecla para continuar........')
        os.system("cls")
        return alunos()

def deletar_alunos():

    os.system("cls")
    print(f"{'='*25} DELETAR UM ALUNO {'='*25}")
    
    id_aluno = int(input('Insira o ID do aluno a ser deletado: '))


    CURSOR.execute(f"select * from alunos where id = {id_aluno}")
    aluno = CURSOR.fetchall()

    if not aluno:
        os.system("cls")
        input('Aluno inexistente! \n Pressione qualquer tecla para continuar....')
        return
    else:
        CURSOR.execute(f"delete from alunos where id = {id_aluno}")
    if True:
        os.system("cls")
        input('Aluno deletado com sucesso! \n Pressione qualquer tecla para continuar....')
        return alunos()

def cadastrar_alunos():
    os.system("cls")
    print(f"{'-'*68}")

    print(f"{'='*25} CADASTRAR ALUNO {'='*25}")

    print("Insira os dados necessarios para efetuar o cadastro do aluno")
 
    nome = str(input("Insira o nome do aluno:"))
    dns = (input("Insira a data de nascimento do aluno:"))
    sexo = str(input("Qual o sexo do aluno? (M/F):"))

    print(f"{'='*25} CONFIRMAR DADOS {'='*25}")

    print(f"NOME_ALUNO:{nome}")
    print(f"DATA_DE_NASCIMENTO:{dns}")
    print(f"SEXO:{sexo}")

    print(f"{'='*68}")
    
    resposta = input("deseja cadastrar este aluno? (S/N)?")

    if resposta.upper() == "S":
        CURSOR.execute(f"insert into alunos (nome,dns,sexo) values ('{nome}','{dns}','{sexo}')")
        CONN.commit()
        print("Aluno cadastrada com sucesso!")
    elif resposta.upper() == "N":
        print("Cadastro de aluno anulado com sucesso")
    else:
        print("Resposta inválida!")
    
    if True:
        os.system("cls")
        input('Pressione qualquer tecla para continuar....')
        return alunos()