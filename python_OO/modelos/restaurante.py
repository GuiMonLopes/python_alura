class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurentes():
        for restaurante in Restaurante.restaurantes:
            print(f'Restaurante: {restaurante.nome} | Categoria: {restaurante.categoria} | Status: {restaurante.status}')


    


restaurante_praca = Restaurante('Praça', 'Brasileira')
restaurante_pizza = Restaurante('Suprema', 'Pizzaria')


Restaurante.listar_restaurentes()