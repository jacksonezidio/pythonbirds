class Pessoa:

    olhos = 2

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

    #atributo dinamico
    jack.sobrenome = "Deus"
    print(jack.sobrenome)

    #exclui um atributo dinamicamente
    del jack.filhos

    print(jack.__dict__)
    print(lorenzo.__dict__)

    print(Pessoa.olhos)
    print(jack.olhos)
    print(lorenzo.olhos)
    print(id(Pessoa.olhos), id(jack.olhos), id(lorenzo.olhos) )

    # alteracao de valor do atributo olhos so de lorenzo
    lorenzo.olhos = 1
    print(id(Pessoa.olhos), id(jack.olhos), id(lorenzo.olhos))