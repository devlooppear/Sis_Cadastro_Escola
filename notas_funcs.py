import os
from comum import sair
from db import CONN,CURSOR

NOTAS = """===================NOTAS===================

[1] - Listar
[2] - Deletar
[3] - Cadastrar
[4] - Voltar

[0] - Sair

===========================================
"""

def notas():
    opcao_notas = -1
    while True:
        os.system("cls")
        if opcao_notas != -1:
            print("Opção Inválida!")
        print(NOTAS)
        opcao_notas = int(input('Escolha uma opção: '))
        if opcao_notas == 1:
            listar_notas()
            opcao_notas = -1
        elif opcao_notas == 2:
            deletar_notas()
            opcao_notas = -1
        elif opcao_notas == 3:
            cadastrar_notas()
            opcao_notas = -1
        elif opcao_notas == 4:
            return
        elif opcao_notas == 0:
            sair()

def listar_notas():
    os.system("cls")
    print(f"{'='*25} LISTAGEM {'='*25}")
    COLUNAS = [("ID",5),("TRIMESTRE",10),("ID_ALUNO",10),("NOTA",5),("MATERIA",20)]
    print("|",end="")
    for col in COLUNAS:
        print(col[0] + " "*(col[1]-len(col[0])),end="|")
    
    print()

    CURSOR.execute("select * from notas")
    db_notas = CURSOR.fetchall()

    for nota in db_notas:
        print("|",end="")
        print(str(nota[0]) + " "*(5-len(str(nota[0]))),end="|")
        print(str(nota[1]) + " "*(10-len(str(nota[1]))),end="|")
        print(str(nota[2]) + " "*(10-len(str(nota[2]))),end="|")
        print(str(nota[3]) + " "*(5-len(str(nota[3]))),end="|")
        print(str(nota[4]) + " "*(20-len(str(nota[4]))),end="|")
        print()

    print(f"{'='*60}")
    if True:
        input('Pressione qualquer tecla para continuar........')
        os.system("cls")
        return notas()

def deletar_notas():
    os.system("cls")
    print(f"{'='*25} DELETAR UMA NOTA {'='*25}")

    id_nota = int(input('Insira o ID da nota a ser deletada:'))

    CURSOR.execute(f"select * from notas where id = {id_nota}")
    nota = CURSOR.fetchall()

    if not nota:
        os.system("cls")
        input('Sala inexistente!\nPressione qualquer tecla para continuar....\n')
        return
    else:
        CURSOR.execute(f"delete from notas where id = {id_nota}")

    if True:
        os.system("cls")
        input('Nota deletada com sucesso!\nPressione qualquer tecla para continuar....\n')
        return notas()

def cadastrar_notas():
    os.system("cls")

    print(f"{'='*25} CADASTRAR NOTAS {'='*25}")

    print("Insira os dados necessarios para efetuar o cadastro da nota")

    print(f"{'='*66}")

    trimestre = int(input("Insira qual o trimestre:"))
    nota1 = int(input("Insira a primeira nota:"))
    nota2 = int(input("Insira a segunda nota:"))
    nota3 = int(input("Insira a terceira nota:"))
    nota4 = int(input("Insira a quarta nota:"))
    materia = input("Qual a matéria?:")

    nota = int((nota1+nota2+nota3+nota4)/4)

    print(f"{'='*25} CONFIRMAR DADOS {'='*25}")

    print(f"QTD_ALUNO:{trimestre}")
    print(f"PROFESSOR:{nota}")
    print(f"ATIVA:{materia}")


    resposta = input("deseja cadastrar esta nota (S/N)?")

    if resposta.upper() == "S":
        CURSOR.execute(f"insert into notas (trimestre,nota,materia) values ('{trimestre}','{nota}','{materia}')")
        CONN.commit()
        print("Nota cadastrada com sucesso!")
    elif resposta.upper() == "N":
        print("Cadastro de nota anulado com sucesso")
    else:
        print("Resposta inválida!")

    if True:
        os.system("cls")
        input('Pressione qualquer tecla para continuar....')
        return notas()