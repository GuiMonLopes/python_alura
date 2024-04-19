from modelos.avaliacao  import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        self._avaliacao = []
        self._cardapio = []
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


    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do Restauante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start =1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)





    
