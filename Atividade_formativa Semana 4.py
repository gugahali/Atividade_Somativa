import sqlite3
from tkinter import messagebox

class Registro_De_Alunos:
        def __init__(self):
            self.connect = sqlite3.connect('Estudantes.db')
            self.c = self.connect.cursor()
            self.create_table()

        def create_table(self):
            self.c.execute(''' CREATE TABLE IF NOT EXISTS Alunos(
                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                nome TEXT NOT NULL,
                                turma TEXT NOT NULL,
                                matricula TEXT NOT NULL,
                                telefone TEXT NOT NULL,
                                email TEXT NOT NULL)''')

        def register_student(self,Alunos):
            self.c.execute(''' INSERT INTO Alunos(nome, turma, matricula, telefone,email) VALUES (?,?,?,?,?)''', (Alunos))
            self.connect.commit

            messagebox.showinfo('Adicionado com Sucesso','Registrado com sucesso')
        
        def Students_data(self):
            self.c.execute(''' SELECT * FROM Alunos ''')
            dados_alunos= self.c.fetchall()
            for linha in dados_alunos:
                print(f'ID: {linha[0]} | Nome: {linha[1]} | Turma: {linha[2]} | Matricula: {linha[3]} | Tel: {linha[4]} | Email: {linha[5]}')

        def search_student(self,id):
            self.c.execute(''' SELECT * FROM Alunos WHERE id = ? ''',(id,))
            dados = self.c.fetchone()
            
            print(f'ID: {dados[0]} | Nome: {dados[1]} | Turma: {dados[2]} | Matricula: {dados[3]} | Tel: {dados[4]} | Email: {dados[5]}')

        def update_student(self,new_values):
            query = ''' UPDATE Alunos SET nome=? turma=? matricula=? tel=? email=? WHERE id=? '''
            self.c.execute(query,new_values)
            self.connect.commit()

            messagebox.showinfo('Sucesso',f'O Estudante com ID:{new_values[8]} Foi Atualizado')
        
        def delete_student(self,id):
            self.c.execute(''' DELETE FROM Estudantes WHERE id=? ''', (id,))
            self.connect.commit()
            messagebox.showinfo('Sucesso',f'O Estudante com ID:{id} Foi Deletado')



'''
while True :
    sistema_de_registro = Registro_De_Alunos()
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
                nome_estudante = str(input('Qual o Nome do Estudante?'))
                turma_estudante = str(input('Qual a Turma do Estudante?'))
                matricula_estudante = str(input('Qual o CPF do Estudante?'))
                tel_estudante = str(input('Qual o Telefone do Estudante?'))
                email_estudante = str(input('Qual o Email do Estudante?'))
                estudante_dados = (nome_estudante, turma_estudante, matricula_estudante, tel_estudante, email_estudante)
                sistema_de_registro = Registro_De_Alunos()
                sistema_de_registro.register_student(estudante_dados)
                       

            elif opção == 2:
                sistema_de_registro.Students_data()


            elif opção ==3:
                 with sqlite3.connect('Estudantes.db') as conexao:
                    cursor = conexao.cursor()
                    cursor.execute('' SELECT * FROM Estudantes '')
                    tabela = cursor.fetchall()
                    for linha in tabela:
                        print('-',linha)

                 with sqlite3.connect('Estudantes.db') as conexao :
                    update_aluno = str(input('Qual Nome Será Colocado no lugar do outro?'))
                    update_id = int(input('Qual ID Do outro aluno??'))
                    cursor = conexao.cursor()
                    cursor.execute('' UPDATE Estudantes SET nome='{}' WHERE id={} ''.format(update_aluno,update_id))
                    conexao.commit()
                    print('Estudante {} Adicionado com Sucesso'.format(update_aluno))
                    input("Pressione ENTER para voltar ao menu de operações")
                
            elif opção == 4:
                with sqlite3.connect('Estudantes.db') as conexao:
                    cursor = conexao.cursor()
                    cursor.execute('' SELECT * FROM Estudantes '')
                    tabela = cursor.fetchall()
                    for linha in tabela:
                        print('-',linha)

                with sqlite3.connect('Estudantes.db') as conexao :
                    delete_id = int(input('Qual ID Do outro aluno??'))
                    cursor = conexao.cursor()
                    cursor.execute('' SELECT nome FROM Estudantes WHERE id={} ''.format(delete_id))
                    deletado = cursor.fetchone()
                    cursor.execute('' DELETE FROM Estudantes WHERE id={} ''.format(delete_id))
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
'''