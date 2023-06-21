print('Olá, mundo!')

pessoa1 = 'Victor'
pessoa2 = 'Vitor'

print('Sejam bem vindos', pessoa1, 'e', pessoa2)

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
resultadosoma = numero1+numero2

print('A soma entre {} e {} é igual a {}'.format(numero1, numero2, resultadosoma))

checar = (input('Digite o caractere: '))

tipo = type(checar)

so_tem_espacos = checar.isspace()

e_um_numero = checar.isnumeric()

e_alfabetico = checar.isalpha()

e_alfanumerico = checar.isalnum()

esta_em_maiusculas = checar.isupper()

esta_em_minusculas = checar.islower()

esta_capitalizado = checar.istitle()

print('O tipo primitivo desse valor é', tipo)
print('Só tem espaços?', so_tem_espacos)
print('É um número?', e_um_numero)
print('É alfabético?', e_alfabetico)
print('É alfanumérico?', e_alfanumerico)
print('Está em maiúsculas?', esta_em_maiusculas)
print('Está em minúsculas?', esta_em_minusculas)
print('Está capitalizado?', esta_capitalizado)

inteiro = int(input('Digite o seu primeiro número inteiro:'))

antecessor = inteiro-1

sucessor = inteiro+1

print('Analisando o número {}, seu antecessor é {}, e o seu sucessor é {}'.format(inteiro, antecessor, sucessor))