import os


print('Sabor Express\n')

print('1.Cadastrar Restaurante')
print('2.Listar Restaurante')
print('3.Ativar Restaurante')
print('4.Sair\n')


opcao_escolhida = int(input('Escolha uma opção: '))


def finalizar_app():
    os.system('clear')
    print('Encerrando o App.\n')



match opcao_escolhida:
    case 1:
        print('Cadastrar Restaurante')
    case 2:
        print('Lista Restaurante')
    case 3:
        print('Ativar Restaurante')
    case 4:
        finalizar_app()
