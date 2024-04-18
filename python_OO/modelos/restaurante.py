class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurentes(cls):
        print(f'{'Nome do Restaurante'.ljust(33)} | {'Categoria'.ljust(31)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'Restaurante: {restaurante._nome.ljust(20)} | Categoria: {restaurante._categoria.ljust(20)} | Status: {restaurante._status}')

    @property
    def status(self):
        return 'Verdadeiro' if self._status else 'Falso'
    
    def alternar_status(self):
        self._status = not self._status


restaurante_praca = Restaurante('praça','Gourmet')
restaurante_mexicano = Restaurante('Mexican Food','Mexicana')
restaurante_japones = Restaurante('Sushi Food','Japonesa')
restaurante_mexicano.alternar_status()

Restaurante.listar_restaurentes()
