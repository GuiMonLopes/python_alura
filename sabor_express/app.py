import os

restaurantes_lista = [{'nome':'Praça','categoria':'Japonesa', 'ativo': False}, 
                      {'nome':'Pizza Suprema','categoria':'Pizzaria', 'ativo': True},
                      {'nome':'Cantina','categoria':'Italiano', 'ativo': False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Essa função exibi as opções para usuario utilizar o nosso programa'''
    print('1.Cadastrar Restaurante')
    print('2.Listar Restaurante')
    print('3.Alternar status do Restaurante')
    print('4.Sair\n')

def finalizar_app():
    ''' Essa função finaliza o app'''
    exibir_subtitulo('Encerrando o App.')

def opcao_invalida():
    '''Essa função informa que ocorreu um erro ao selecionar uma opção não existente'''
    print('Opção Invalida.\n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    '''Exibi o titulo das opções do programa'''
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu():
    '''Essa função volta ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal.')
    main()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes')    
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes_lista.append(dados_do_restaurante)
    print(f'O restaurante: {nome_restaurante} com categoria: {categoria} foi cadastrado com sucesso!\n')
    voltar_ao_menu()

def listar_restaurantes():
    '''Essa função lista os restaurantes cadastrados'''
    exibir_subtitulo('Listando os Restaurantes')
    print(f'{'Nome do Restaurante'.ljust(33)} | {'Categoria'.ljust(31)} | {'Status'}')
    for restaurante in restaurantes_lista:
        nome_restautante = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'Restaurante: {nome_restautante.ljust(20)} | Categoria: {categoria.ljust(20)} | Status: {status}')    
    voltar_ao_menu()


def alternar_status_restaurante():
    '''Essa função altera as informações de status do restaurante já cadastrado.'''
    exibir_subtitulo('Alternando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja mudar o status: ')
    restaurante_encontrado = False
    for restaurante in restaurantes_lista:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_ao_menu()


def escolher_opcao():
    '''Essa função coleta a opção escolhida pelo usuario'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_status_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função é a main do programa'''
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()