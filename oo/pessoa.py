class Pessoa:

    def __init__(self,*filhos,nome=None,idade=31):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    lorenzo = Pessoa(nome="Lorenzo")
    jack = Pessoa(lorenzo,nome="Jackson")
    print(jack.cumprimentar())
    print(jack.nome)
    print(jack.idade)
    print(jack.filhos)

    for filho in jack.filhos:
        print(filho.nome)
