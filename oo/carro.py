
"""
    classe de teste
    python -m doctest nome_arquvo
    Exemplo:
    
    >>> # teste
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> direcao = Direcao()
    >>> direcao.direcao_atual
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.direcao_atual
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.direcao_atual
    'Norte'
    >>> carro = Carro(direcao,motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.ver_direcao_atual()
    'Norte'
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.girar_a_direita()
    >>> carro.ver_direcao_atual()
    'Leste'


"""

from oo.direcao import Direcao
from oo.motor import Motor


class Carro:

    def __init__(self,direcao,motor):
        self.direcao = direcao #Direcao()
        self.motor = motor #Motor()
        #self.direcao_atual = 'Norte'

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def ver_direcao_atual(self):
        return self.direcao.direcao_atual


if __name__ == "__main__":

    # instancia de direcao e motor direta na classe carro
    motor = Motor()
    direcao = Direcao()
    carro = Carro(direcao, motor)

    print(carro.calcular_velocidade())
    print(carro.ver_direcao_atual())

    carro.acelerar()
    print(carro.calcular_velocidade())

    carro.girar_a_direita()
    print(carro.ver_direcao_atual())
