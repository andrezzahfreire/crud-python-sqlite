
from create_table import create_tables
from crud_empregado import *
from crud_historico import *
from crud_trabalho import *
from db import criar_conexao, fechar_conexao


def adicionar_empregado(conn):
    empregado = (
        input("Nome: "), 
        input("Aniversário (YYYY-MM-DD): "), 
        float(input("Salário: ")), 
        input("Departamento: ")
    )
    emp_id = add_empregado(conn, empregado)
    print(f"Empregado adicionado com sucesso com ID {emp_id}!")

def ler_empregado(conn):
    empregado_id = input("Digite o ID do empregado: ")
    empregado = read_empregado(conn, empregado_id)
    if empregado:
        print("ID:", empregado[0])
        print("Nome:", empregado[1])
        print("Aniversário:", empregado[2])
        print("Salário:", empregado[3])
        print("Departamento:", empregado[4])
        print("ID do Trabalho:", empregado[5])
    else:
        print("Empregado não encontrado!")

def atualizar_empregado(conn):
    empregado_id = input("Digite o ID do empregado para atualizar: ")
    
    empregado_atual = read_empregado(conn, empregado_id)
    
    if empregado_atual:
        print(f"\nDados atuais do empregado (ID {empregado_id}):")
        print(f"Nome: {empregado_atual[1]}")
        print(f"Aniversário: {empregado_atual[2]}")
        print(f"Salário: {empregado_atual[3]}")
        print(f"Departamento: {empregado_atual[4]}")
        print(f"ID do Trabalho: {empregado_atual[5]}")

       
        nome = input(f"Nome [{empregado_atual[1]}]: ") or empregado_atual[1]
        aniversario = input(f"Aniversário (YYYY-MM-DD) [{empregado_atual[2]}]: ") or empregado_atual[2]
        salario = input(f"Salário [{empregado_atual[3]}]: ") or empregado_atual[3]
        departamento = input(f"Departamento [{empregado_atual[4]}]: ") or empregado_atual[4]
        job_id = input(f"ID do Trabalho [{empregado_atual[5]}]: ") or empregado_atual[5]

    
        empregado = {
            'EmployeeID': empregado_id,
            'Name': nome,
            'Birthday': aniversario,
            'Salary': float(salario),
            'Department': departamento,
            'JobID': job_id
        }

        update_empregado(conn, empregado)
        print("Empregado atualizado com sucesso!")
    else:
        print(f"Empregado com ID {empregado_id} não encontrado.")


def deletar_empregado(conn):
    empregado_id = input("Digite o ID do empregado para deletar: ")
    delete_empregado(conn, empregado_id)
    print("Empregado deletado com sucesso!")


def adicionar_trabalho(conn):
    trabalho = (input("Nome do Trabalho: "), input("Descrição: "))
    job_id = add_trabalho(conn, trabalho)  
    print(f"Trabalho adicionado com sucesso com ID {job_id}!")


def ler_trabalho(conn):
    trabalho_id = input("Digite o ID do trabalho: ")
    trabalho = read_trabalho(conn, trabalho_id)
    if trabalho:
        print("ID do Trabalho:", trabalho[0])
        print("Nome:", trabalho[1])
        print("Descrição:", trabalho[2])
    else:
        print("Trabalho não encontrado!")

def atualizar_trabalho(conn):
    trabalho_id = input("Digite o ID do trabalho para atualizar: ")
    
    # Busca os dados existentes
    trabalho_existente = read_trabalho(conn, trabalho_id)
    
    if trabalho_existente:
        print(f"Dados atuais do trabalho:")
        print(f"ID: {trabalho_existente[0]}, Nome: {trabalho_existente[1]}, Descrição: {trabalho_existente[2]}")
        
        # Solicita as novas informações
        trabalho = {
            'JobID': trabalho_id,
            'Name': input("Novo Nome (deixe em branco para manter o atual): ") or trabalho_existente[1],
            'Description': input("Nova Descrição (deixe em branco para manter a atual): ") or trabalho_existente[2]
        }
        
        update_trabalho(conn, trabalho)
        print("Trabalho atualizado com sucesso!")
    else:
        print("Trabalho não encontrado!")


def deletar_trabalho(conn):
    trabalho_id = input("Digite o ID do trabalho para deletar: ")
    delete_trabalho(conn, trabalho_id)
    print("Trabalho deletado com sucesso!")


def adicionar_historico(conn):
    historico = (
        input("ID do Empregado: "),  
        input("Data de Início (YYYY-MM-DD): "),
        input("Data de Término (YYYY-MM-DD): "),
        float(input("Salário: ")),
        input("Nome do Trabalho: ")
    )
    job_history_id = add_historico(conn, historico)  
    print(f"Histórico adicionado com sucesso com ID {job_history_id}!")


def ler_historico(conn):
    historico_id = input("Digite o ID do histórico: ")
    historico = read_historico(conn, historico_id)
    if historico:
        print("ID do Histórico:", historico[0])
        print("ID do Empregado:", historico[1])
        print("Data de Início:", historico[2])
        print("Data de Término:", historico[3])
        print("Salário:", historico[4])
        print("Nome do Trabalho:", historico[5])
    else:
        print("Histórico não encontrado!")


def atualizar_historico(conn):
    historico_id = input("Digite o ID do histórico para atualizar: ")
    

    historico = read_historico(conn, historico_id)
    if historico:
        print(f"Informações do Histórico:")
        print(f"ID: {historico[0]}")
        print(f"ID do Empregado: {historico[1]}")
        print(f"Data de Início: {historico[2]}")
        print(f"Data de Término: {historico[3]}")
        print(f"Salário: {historico[4]}")
        print(f"Nome do Trabalho: {historico[5]}")
    else:
        print("Histórico não encontrado.")
        return


    novo_historico = {
        'JobHistoryID': historico_id,  
        'EmployeeID': input("ID do Empregado (deixe em branco para manter o atual): ") or historico[1],
        'StartDate': input("Data de Início (YYYY-MM-DD, deixe em branco para manter a atual): ") or historico[2],
        'EndDate': input("Data de Término (YYYY-MM-DD, deixe em branco para manter a atual): ") or historico[3],
        'Salary': float(input("Salário (deixe em branco para manter o atual): ") or historico[4]),
        'Job': input("Nome do Trabalho (deixe em branco para manter o atual): ") or historico[5]
    }
    
    update_historico(conn, novo_historico)
    print("Histórico de trabalho atualizado com sucesso!")


def deletar_historico(conn):
    historico_id = input("Digite o ID do histórico para deletar: ")
    delete_historico(conn, historico_id)
    print("Histórico de trabalho deletado com sucesso!")


def exibir_menu():
    print("\nMENU CRUD")
    print("1. Criar empregado")
    print("2. Ler empregado")
    print("3. Atualizar empregado")
    print("4. Deletar empregado")
    print("5. Criar trabalho")
    print("6. Ler trabalho")
    print("7. Atualizar trabalho")
    print("8. Deletar trabalho")
    print("9. Criar histórico de trabalho")
    print("10. Ler histórico de trabalho")
    print("11. Atualizar histórico de trabalho")
    print("12. Deletar histórico de trabalho")
    print("13. Sair")


def executar_menu(conn):
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_empregado(conn)
        elif opcao == "2":
            ler_empregado(conn)
        elif opcao == "3":
            atualizar_empregado(conn)
        elif opcao == "4":
            deletar_empregado(conn)
        elif opcao == "5":
            adicionar_trabalho(conn)
        elif opcao == "6":
            ler_trabalho(conn)
        elif opcao == "7":
            atualizar_trabalho(conn)
        elif opcao == "8":
            deletar_trabalho(conn)
        elif opcao == "9":
            adicionar_historico(conn)
        elif opcao == "10":
            ler_historico(conn)
        elif opcao == "11":
            atualizar_historico(conn)
        elif opcao == "12":
            deletar_historico(conn)
        elif opcao == "13":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    
    fechar_conexao(conn)


if __name__ == '__main__':
    conn = criar_conexao("my.db")
    create_tables()
    if conn:
        executar_menu(conn)
    else:
        print("Erro ao conectar com o banco de dados!")
