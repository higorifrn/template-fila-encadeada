# -*- coding:UTF-8 -*-
from no import No

class Fila:
    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__fim = None
        self.__capacidade = capacidade
        self.__qtdItens = 0
        print(f"Criada EDD Fila com capacidade: {capacidade}")


    # verifica se a fila está vazia
    # retornar True se a fila estiver vazia e False caso contrário
    def is_empty(self) -> bool:
        # implementação do método
        pass


    # verifica se a fila está cheia
    # retornar True se a fila estiver cheia e False caso contrário
    def is_full(self) -> bool:
        # implementação do método
        pass


    # insere um elemento no final da fila e retorna True, se for possível
    # se a fila estiver cheia, lança uma exceção: raise Exception("mensagem de erro")
    def enqueue(self, valor) -> bool:
        # implementação do método
        pass

    
    # remove um elemento do início da fila e retorna esse elemento
    # se a fila estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def dequeue(self) -> No:
        # implementação do método
        pass


    # retornar o primeiro elemento da fila sem removê-lo
    # se a fila estiver vazia retorna None
    def peek_first(self) -> No:
        # implementação do método
        pass


    # retornar o último elemento da fila sem removê-lo
    # se a fila estiver vazia retorna None
    def peek_last(self) -> No:
        # implementação do método
        pass


    # retorna uma lista com a ordem dos elementos da fila
    # imprime os elementos da fila do primeiro para o último
    # caso a fila esteja vazia, imprime uma mensagem informando
    # que a fila está vazia e retorna uma lista vazia
    def display(self) -> list[str]:
        # implementação do método
        pass
    

    # retorna a quantidade de elementos na fila
    # se a fila estiver vazia, retorna ZERO
    def size(self) -> int:
        # implementação do método
        pass
