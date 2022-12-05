from classes.elogio import Elogio
from classes.reclamacoes import Reclamacoes
from classes.sugestoes import Sugestoes

print('-'*100)
print('Bem-Vindo a Ouvidoria Unifacisa'.center(100))
print('-'*100)

user = str(input('\nDigite seu nome de usuário : '))
senha = int(input('Digite sua Senha : '))

print("\nBem-vindo %s!" % user)
print("Senha: %s" % senha)

Reclamacoes = Reclamacoes()
Elogio = Elogio()
Sugestoes = Sugestoes()

option = 6

while True:
    print('='*100)
    print('O que você deseja fazer ?\n')
    print('1) Inserir')
    print('2) Listar')
    print('3) Apagar')
    print('4) Editar')
    print('5) Sair')

    option = int(input('\nEscolha uma opção :'))
    print('Opção escolhida :', option)

    if option == 1:
        print('\n1) Reclamação')
        print('2) Elogio')
        print('3) Sugestões')
        resp = int(input('\nEscolha uma categoria :\n'))
        

        if resp == 1:
            descricao = input('\nDigite sua reclamação:\n')
            Reclamacoes.inserir(descricao)
        elif resp == 2:
            descricao = input('\nDigite seu elogio:\n')
            Elogio.inserir(descricao)
        elif resp == 3:
            descricao = input('\nDigite sua Sugestão:\n')
            Sugestoes.inserir(descricao)
        else:
            print('Erro! Categoria não encontrada')

    elif option == 2:
        
        Reclamacoes.listar()
        Elogio.listar()
        Sugestoes.listar()


    elif option == 3:
        print('\n1) Reclamação')
        print('2) Elogio')
        print('3) Sugestões')
        resp = int(input('\nEscolha uma Categoria :'))
        
        if resp == 1:
            Reclamacoes.listar()
            resp = int(input('Se você deseja apagar todas as reclamações digite 0, caso queira apagar outras ocorrencias digite o \nnumero da reclamação.\nOpção: '))
            Reclamacoes.apagar(resp)
        elif resp == 2:
            Elogio.listar()
            resp = int(input('Se você deseja apagar todos os elogios digite 0, caso queira apagar outras ocorrencias digite o \nnumero do Elogio.\nOpção: '))
            Elogio.apagar(resp)
        elif resp == 3:
            Sugestoes.listar()
            resp = int(input('Se você deseja apagar todas as sugestões digite 0, caso queira apagar outras ocorrencias digite o \nnumero da sugestão\nOpção: '))
            Sugestoes.apagar(resp)
        else:
            print('Erro! Categoria não encontrada!')
        
    elif option == 4:
        print('\n1) Reclamação')
        print('2) Elogio')
        print('3) Sugestões')
        resp = int(input('\nEscolha uma Categoria :'))
        
        if resp == 1:
            Reclamacoes.listar()
            id = int(input('Qual reclamação você deseja editar ?\nOpção: '))
            novaDescricao = input('Digite a descrição da ocorrencia: \n')
            Reclamacoes.editar(id, novaDescricao)
        elif resp == 2:
            Elogio.listar()
            id = int(input('Qual elogio você deseja editar ?\nOpção: '))
            novaDescricao = input('Digite a descrição da ocorrencia: \n')
            Elogio.editar(id, novaDescricao)
        if resp == 3:
            Sugestoes.listar()
            id = int(input('Qual reclamação você deseja editar ?\nOpção: '))
            novaDescricao = input('Digite a descrição da ocorrencia: \n')
            Sugestoes.editar(id, novaDescricao)
    
    elif option == 5:
        print('=' * 100)
        print('Obrigado por ultilizar nossa Ouvidoria!'.center(100))
        print()
        print('© 2022 Babigol | Unifacisa'.center(100))
        print('=' * 100)
        break

    else:
        print('\nERRO : Opção Invalida')
