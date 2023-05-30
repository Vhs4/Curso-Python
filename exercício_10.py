from carro import Carro
from pessoa import Pessoa

carro_a = Carro("Ford", "Fiesta", "Branco", "Gasolina")

print(carro_a.marca, carro_a.modelo, carro_a.cor, carro_a.combustivel)

carro_a.ligar()
carro_a.acelerar()
carro_a.frear()


carro_b = Carro("Ford", "Fiesta", "Branco", "Gasolina")

print(carro_b.marca, carro_b.modelo, carro_b.cor, carro_b.combustivel)

carro_b.ligar()
carro_b.acelerar()
carro_b.frear()

pessoa_a = Pessoa("Victor Hugo", "17", "1,80")

print(pessoa_a.nome, pessoa_a.idade, pessoa_a.altura)
