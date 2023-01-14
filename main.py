import os
from comum import sair
from salas_funcs import salas
from alunos_funcs import alunos
from notas_funcs import notas

MENU ="""===================MENU===================

[1] - Salas
[2] - Alunos
[3] - Notas

[0] - Sair

===========================================
"""


def menu():
    opcao = -1
    while opcao not in [0,1,2,3]:
        os.system("cls")
        if opcao != -1:
            print("Opção Inválida!")
        print(MENU)
        opcao = int(input('Escolha uma opção: '))
    return opcao

def main():

    while True:
        opcao = menu()

        if opcao == 0:
            sair()
        elif opcao == 1:
            salas()
        elif opcao == 2:
            alunos()
        elif opcao == 3:
            notas()

main()