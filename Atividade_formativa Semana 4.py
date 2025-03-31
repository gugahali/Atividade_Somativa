'''

Nome: Gustavo Halicki
Curso: Analise e Desenvolvimento de Sistemas (ADS)

'''
#Criação de uma Matriz contendo 5 listas vazias e adicionando na variavel "faculdade"
faculdade = [[],[],[],[],[]]

#Começa uma Estrutura de repetição com While True
while True :
    #Pergunta ao usuario qual das 5 opções do Menu Principal ele pretende acessar, Guardando a Resposta na variavel "menu_princ"
    menu_princ = input(("------ Menu Principal -----\n (1) Verificar Estudantes \n (2) Verificar Professores \n (3) Verificar Disciplinas \n (4) Verificar Turmas \n (5) Verificar Matriculas \n (8) Sair \n Opção Selecionada: "))
    
    #Verifica se o valor da variavel "menu_princ" é igual a '1', utilizando o if junto de uma estrutura de condição 
    if (menu_princ == '1'):
        while True:
            #Pergunta ao Usuario qual das 5 opções do menu de operações ele deseja acessar,e guarda o resultado na variavel "opção"
            opção = input(' \n ----[Estudantes]---- Menu de Modificações \n (1) Incluir \n (2) Listar \n (3) Atualizar \n (4) Excluir \n (0) Voltar ao Menu Principal \n Opção Selecionada: ') 
            #Verifica se o valor da variavel "opção" é igual a '1', utilizando o if junto de uma estrutura de condição
            if opção == '1':
                print('---Incluir Estudante---')
                #Pergunta ao usuario qual o nome do estudante que vai ser adicionada a lista, e guarda na variavel estudante_sendo_adicionado
                estudante_sendo_adicionado = str(input('Qual Seria o Nome Do Estudante?'))
                #Adiciona o Valor da variavel estudante_sendo_adicionado, adicionando na lista[0] , utilizando o metodo append
                faculdade[0].append(estudante_sendo_adicionado)
                #Mostra que o Estudante foi adicionado a lista, junto do nome do mesmo
                print('Estudante {} Adicionado'.format(estudante_sendo_adicionado))
                print('\nVoltando a tela ao Menu de Operações') #Mostra o texto antes de voltar ao menu de operações

            #Caso o primeiro if não for verdadeiro(True), Verifica se o valor da variavel opção é '2', Utiliznado elif
            elif opção == '2':
                print('---Preparando Lista de Estudantes---\n')
                #Verifica se a lista está vazia utilizando uma condição junto da função len na lista[0] da matriz, se estiver vazia mostra a mensegem ("Não há estudantes cadastrados")
                if len(faculdade[0]) == 0 :
                    print('Não há estudantes cadastrados')
                #Caso a Lista não esteja vazia, Vai passar por cada nome da lista[0] adicionando um "-" antes do nome, e mostrando cada nome em sequência que foi adicionado
                else:
                    for nome in faculdade[0]:
                        print('-',nome)
                print('\n Voltando ao Menu de Opçoes') #Mostra o texto antes de voltar ao menu de operações

            #Caso o primeiro elif não for verdadeiro(True), Verifica se o valor da variavel opção é '3'   
            elif opção == '3':
                print('\n EM DESENVOLVIMENTO') #Mostra a mensagem "Em desenvolvimento"

            #Caso o segundo elif não for verdadeiro(True), Verifica se o valor da variavel opção é '4'
            elif opção == '4':
                print('\n EM DESENVOLVIMENTO') #Mostra a mensagem "Em desenvolvimento"

            #Caso o terceiro elif não for verdadeiro(True), Verifica se o valor da variavel opção é '0'
            elif (opção == '0') :
                break   #Quebra a Estrutura de repetição(While), Fazendo voltar ao Menu Principal

    #Verifica se o valor da variavel "menu_princ" é igual a '2', utilizando o if junto de uma estrutura de condição             
    if (menu_princ == '2'):
        while True:
            input('\n EM DESENVOLVIMENTO \n Pressione ENTER Para Voltar ') #Mostra o Texto "EM DESENVOLVIMENTO"
            break #Quebra a Estrutura de repetição(While), Fazendo voltar ao Menu Principal
  
    if (menu_princ == '3'):
        while True: 
            input('\n EM DESENVOLVIMENTO \n Pressione ENTER Para Voltar ') #Mostra o Texto "EM DESENVOLVIMENTO"
            break #Quebra a Estrutura de repetição(While), Fazendo voltar ao Menu Principal
            
    if (menu_princ == '4'):
        while True:
            input('\n EM DESENVOLVIMENTO \n Pressione ENTER Para Voltar ') #Mostra o Texto "EM DESENVOLVIMENTO"
            break #Quebra a Estrutura de repetição(While), Fazendo voltar ao Menu Principal

    if (menu_princ == '5'):
        while True:
            input('\n EM DESENVOLVIMENTO \n Pressione ENTER Para Voltar ') #Mostra o Texto "EM DESENVOLVIMENTO"
            break #Quebra a Estrutura de repetição(While), Fazendo voltar ao Menu Principal

    if (menu_princ == '8') :
        break #Quebra a Estrutura de repetição(While), Finalizando o Programa 

print('Finalizando Aplicação...')
