import os
from comum import sair
from db import CONN,CURSOR


SALAS ="""==================SALAS===================

[1] - Listar
[2] - Deletar
[3] - Cadastrar
[4] - Voltar

[0] - Sair

===========================================
"""

def salas():
    opcao_sala = -1
    while True:
        os.system("cls")
        if opcao_sala != -1:
            print("Opção Inválida!")
        print(SALAS)
        opcao_sala = int(input('Escolha uma opção: '))
        if opcao_sala == 1:
            listar_salas()
            opcao_sala = -1
        elif opcao_sala == 2:
            deletar_sala()
            opcao_sala = -1
        elif opcao_sala == 3:
            cadastrar_sala()
            opcao_sala = -1
        elif opcao_sala == 4:
            return
        elif opcao_sala == 0:
            sair()
 
def listar_salas():
    os.system("cls")
    print(f"{'='*25} LISTAGEM {'='*25}")
    COLUNAS = [("ID",5),("QTD_ALUNO",10),("PROFESSOR",20),("ATIVO",5),("ANO",5)]
    print("|",end="")
    for col in COLUNAS:
        print(col[0] + " "*(col[1]-len(col[0])),end="|")
    
    print()

    CURSOR.execute("select * from salas")
    db_salas = CURSOR.fetchall()

    for sala in db_salas:
        print("|",end="")
        print(str(sala[0]) + " "*(5-len(str(sala[0]))),end="|")
        print(str(sala[1]) + " "*(10-len(str(sala[1]))),end="|")
        print(str(sala[2]) + " "*(20-len(str(sala[2]))),end="|")
        print(str(sala[3]) + " "*(5-len(str(sala[3]))),end="|")
        print(str(sala[4]) + " "*(5-len(str(sala[4]))),end="|")
        print()
    
    print(f"{'='*60}")
    if True:
        input('Pressione qualquer tecla para continuar........')
        os.system("cls")
        return salas()

def deletar_sala():
    os.system("cls")

    print(f"{'='*25} DELETAR UMA SALA {'='*25}")
    
    id_sala = int(input('Insira o ID da sala a ser deletada:'))


    CURSOR.execute(f"select * from salas where id = {id_sala}")
    sala = CURSOR.fetchall()

    if not sala:
        os.system("cls")
        input('Sala inexistente! \n Pressione qualquer tecla para continuar....')
        return
    else:
        CURSOR.execute(f"delete from salas where id = {id_sala}")

    if True:
        os.system("cls")
        input('Sala deletada com sucesso! \n Pressione qualquer tecla para continuar....')
        return salas()

def cadastrar_sala():
    os.system("cls")
    print(f"{'='*66}")

    print(f"{'='*25} CADASTRAR SALA {'='*25}")

    print("Insira os dados necessarios para efetuar o cadastro da sala")

    print(f"{'='*66}")

    qtd_alunos = int(input("Insira a quantidade de alunos maximo permitido nessa sala:"))
    professor = input("Insira o nome do professor responsavel por esta sala:")
    ativa = input("Esta sala está ativa? (S/N):")
    ano = input("Informe o ano dessa sala:")


    print(f"{'='*25} CONFIRMAR DADOS {'='*25}")

    print(f"QTD_ALUNOS:{qtd_alunos}")
    print(f"PROFESSOR:{professor}")
    print(f"ATIVA:{ativa}")
    print(f"ANO:{ano}")

    
    
    resposta = input("deseja cadastrar esta sala (S/N)?")

    if resposta.upper() == "S":
        CURSOR.execute(f"insert into salas (qtd_alunos,professor,ativa,ano) values ({qtd_alunos},'{professor}','{ativa}','{ano}')")
        CONN.commit()
        print("Sala cadastrada com sucesso!")
    elif resposta.upper() == "N":
        print("Cadastro anulado com sucesso")
    else:
        print("Resposta inválida!")

    if True:
        os.system("cls")
        input('Pressione qualquer tecla para continuar....')
        return salas()