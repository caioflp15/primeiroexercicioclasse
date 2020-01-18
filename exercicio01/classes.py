class Quadrado:
    def __init__(self, altura=None, largura=None):
        self._altura = altura
        self._largura = largura

    @property
    def altura(self):
        return self._altura

    @property
    def largura(self):
        return self._largura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @largura.setter
    def largura(self, largura):
        self._largura = largura

    def mudarValor(self, novo_altura, novo_largura):
        self.largura = novo_largura
        self.altura = novo_altura

        print(f'Agora os valores de altura e largura são {self.altura} e {self.largura}, respectivamente.')

    def retornaValor(self):
        if self.altura == None:
            print(f'Você não informou a altura e largura inicial.')
            return

        if self.largura == None:
            print(f'Você não informou a largura.')
            return

        print(f'A altura é: {self.altura}.\nA Largura é: {self.largura}.')

    def calcularArea(self):
        area = self.largura * self.altura
        print(f'A área do quadrado {self.altura}x{self.largura} é: {area}m².')
