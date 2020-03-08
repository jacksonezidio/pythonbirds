class Direcao:

    def __init__(self):
        self.direcao_atual = "Norte"

    def girar_a_direita(self):
        if self.direcao_atual == "Norte":
            self.direcao_atual = "Leste"
        elif self.direcao_atual == "Leste":
            self.direcao_atual = "Sul"
        elif self.direcao_atual == "Sul":
            self.direcao_atual = "Oeste"
        elif self.direcao_atual == "Oeste":
            self.direcao_atual = "Norte"

    def girar_a_esquerda(self):
        if self.direcao_atual == "Norte":
            self.direcao_atual = "Oeste"
        elif self.direcao_atual == "Oeste":
            self.direcao_atual = "Sul"
        elif self.direcao_atual == "Sul":
            self.direcao_atual = "Leste"
        elif self.direcao_atual == "Leste":
            self.direcao_atual = "Norte"


if __name__ == "__main__":
    direcao = Direcao()
    print(direcao.direcao_atual)

    direcao.girar_a_direita()
    print(direcao.direcao_atual)

    direcao.girar_a_direita()
    print(direcao.direcao_atual)