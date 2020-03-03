class Pessoa:

    def __init__(self,nome=None,idade=31):
        self.nome = nome
        self.idade = idade


    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa("Jackson")
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)

    p.nome = "Jack"
    p.idade = 29

    print(p.nome)
    print(p.idade)