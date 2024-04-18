from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','Gourmet')
restaurante_mexicano = Restaurante('Mexican Food','Mexicana')
restaurante_japones = Restaurante('Sushi Food','Japonesa')

restaurante_mexicano.alternar_status()

def main():
    Restaurante.listar_restaurentes()


if __name__ == '__main__':
    main()