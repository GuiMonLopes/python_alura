from modelos.avaliacao  import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurentes(cls):
        print(f'{'Nome do Restaurante'.ljust(33)} | {'Categoria'.ljust(31)} | {'Avaliações'.ljust(20)}| {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'Restaurante: {restaurante._nome.ljust(20)} | Categoria: {restaurante._categoria.ljust(20)} | Avaliações: {restaurante.media_avaliacoes.ljust(7)} | Status: {restaurante.status}')

    @property
    def status(self):
        return 'Verdadeiro' if self._status else 'Falso'
    
    def alternar_status(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        if 0< nota <5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return str(media)

    
