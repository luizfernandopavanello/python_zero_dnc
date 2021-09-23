# def contador_lista(lista):
#     return len(lista),sum(lista)
# print(contador_lista([0,1,2,3,4,5,6,7,8,9]))

# #função verifica se é par, atribui numa variável e retorna resposta "o numero é"+variavel
# def verifica_par(x):
#     if x % 2==0:
#         result = 'par'
#     else:
#         result='impar'
#     return 'O numero é ' + result
# print(verifica_par(7))

# #lista com numeros de 1 a 9
# lista=[1,2,3,4,5,6,7,8,9]
# #utilizando o map para aplicar a função verifica_par na lista e atribuindo o resultado em x
# x = map(verifica_par, lista)
# #printando a list de x porque o map retorna um construtor
# print(list(x))

#criando função cadastro com input de nome e sobrenome e retornando nome e sobrenome do input
# def cadastro():
#   print("Digite seu nome:")
#   nome=input()
#   print("Digite seu sobrenome:")
#   snome=input()
#   return (nome, snome)
# #criando variavel usuario e chamando funcao cadastro
# user = cadastro()
# #printando variavel usuario
# print(user)

"""1. Crie uma função que receba o input do cpf e nome do usuário."""
"""2. Agora nessa mesma função coloque o retorno como um dicionário onde a chave é o cpf e o valor o nome do usuário."""

# def cadastro_CPF():
#     print('Digite seu nome:')
#     nome = input()
#     print('Digite seu CPF:')
#     cpf = input()
#     return({cpf:nome})
# print(cadastro_CPF())
# print(type(cadastro_CPF()))

# """3. Crie uma função para retornar a quantidade de CPF cadastrados"""

# print(len(cadastro_CPF()))

"""4. Crie uma função Lambda para retornar a soma de 4 valores."""

# sum = lambda num1, num2, num3, num4 : num1 + num2 + num3 + num4
# print(sum(10,20,30,40))

"""5. Utilize uma função filter para retornar somente os números pares da lista abaixo."""

lista = [5,2,5,7,4,2,6,10,342,54,23,6,7,9,12]

# pair = list(filter(lambda x: True if x % 2 == 0 else False,lista))

# print(sorted(pair))

"""3. Utilize a função reduce e retorne a soma da lista anterior."""

# from functools import reduce

# reducer1 = reduce(lambda a, b: a + b, pair)

# print(reducer1)

lista = list(map(int, lista))
lista.sort()
print(lista)