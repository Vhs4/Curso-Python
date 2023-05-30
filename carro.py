class Carro:
    def __init__(self, marca: str, modelo: str, cor: str, combustivel: str):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

    def ligar(self):
        print(
            f"Marca: {self.marca}. Modelo: {self.modelo}. "
            f"Cor: {self.cor}. Combustível: {self.combustivel}."
        )

    def acelerar(self):
        print("Estou acelerando!")

    def frear(self):
        print("Estou freando!")
