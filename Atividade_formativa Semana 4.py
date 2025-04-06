import sqlite3

conexao = sqlite3.connect('Estudantes.db')
cursor = conexao.cursor()

#Criação da Tabela Dos Dados
#cursor.execute (''' CREATE TABLE Estudantes (
#                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                    nome TEXT NOT NULL);''')    


faculdade = [[],[],[],[],[]]

while True :
    menu_princ = int(input("------ Menu Principal -----\n (1) Verificar Estudantes \n (2) Verificar Professores \n (3) Verificar Disciplinas \n (4) Verificar Turmas \n (5) Verificar Matriculas \n (8) Sair \n Opção Selecionada: "))
    
    if (menu_princ) not in [1,2,3,4,5,0] :
        print('\n Por favor, Insira um Número do Menu Principal\n')
      

    if (menu_princ == 1):
        while True:
            opção = int(input(' \n ----[Estudantes]---- Menu de Modificações \n (1) Incluir \n (2) Listar \n (3) Atualizar \n (4) Excluir \n (0) Voltar ao Menu Principal \n Opção Selecionada: '))
            
            if opção not in [1,2,3,4,0] :
                print('Por Favor Digite um Valor pdo menu de Operações')

            if opção == 1:
                print('---Incluir Estudante---')
                estudante_sendo_adicionado = input('Qual Seria o Nome Do Estudante?')
                if len(estudante_sendo_adicionado) == 0 :
                        print('Nome Invalido, Voltando ao menu de Operações')
                else:        
                    with sqlite3.connect('Estudantes.db') as conexao:
                        cursor = conexao.cursor()
                        cursor.execute(''' INSERT INTO Estudantes (nome) VALUES ('{}') ''' .format(estudante_sendo_adicionado))
                        conexao.commit
      
                        print('\nEstudante {} Adicionado'.format(estudante_sendo_adicionado))
                    input("Pressione ENTER para voltar ao menu de operações") 
                       

            elif opção == 2:
                print('---Preparando Lista de Estudantes---')
                with sqlite3.connect('Estudantes.db') as conexao:
                    cursor = conexao.cursor()
                    cursor.execute(''' SELECT * FROM Estudantes ''')
                    tabela = cursor.fetchall()
                    for linha in tabela:
                        print('-',linha)
                input("Pressione ENTER para voltar ao menu de operações")

            elif opção ==3:
                 with sqlite3.connect('Estudantes.db') as conexao:
                    cursor = conexao.cursor()
                    cursor.execute(''' SELECT * FROM Estudantes ''')
                    tabela = cursor.fetchall()
                    for linha in tabela:
                        print('-',linha)

                 with sqlite3.connect('Estudantes.db') as conexao :
                    update_aluno = str(input('Qual Nome Será Colocado no lugar do outro?'))
                    update_id = int(input('Qual ID Do outro aluno??'))
                    cursor = conexao.cursor()
                    cursor.execute(''' UPDATE Estudantes SET nome='{}' WHERE id={} '''.format(update_aluno,update_id))
                    conexao.commit()
                    print('Estudante {} Adicionado com Sucesso'.format(update_aluno))
                    input("Pressione ENTER para voltar ao menu de operações")
                
            elif opção == 4:
                with sqlite3.connect('Estudantes.db') as conexao:
                    cursor = conexao.cursor()
                    cursor.execute(''' SELECT * FROM Estudantes ''')
                    tabela = cursor.fetchall()
                    for linha in tabela:
                        print('-',linha)

                with sqlite3.connect('Estudantes.db') as conexao :
                    delete_id = int(input('Qual ID Do outro aluno??'))
                    cursor = conexao.cursor()
                    cursor.execute(''' SELECT nome FROM Estudantes WHERE id={} '''.format(delete_id))
                    deletado = cursor.fetchone()
                    cursor.execute(''' DELETE FROM Estudantes WHERE id={} '''.format(delete_id))
                    conexao.commit()
                    print('Estudante {} Removido com Sucesso'.format(deletado))
                    input("Pressione ENTER para voltar ao menu de operações")
                

            elif (opção == 0) :
                break

    if (menu_princ == 2):
        print(' EM DESENVOLVIMENTO')
        input(" Aperte a tecla ENTER para voltar")
               
    if (menu_princ == 3):
        print(' EM DESENVOLVIMENTO')
        input(" Aperte a tecla ENTER para voltar")
            
    if (menu_princ == 4):
        print(' EM DESENVOLVIMENTO')
        input(" Aperte a tecla ENTER para voltar")

    if (menu_princ == 5):
        print(' EM DESENVOLVIMENTO')
        input(" Aperte a tecla ENTER para voltar")

    if (menu_princ == 8) :
        break
    
    


print('Finalizando Aplicação...')
