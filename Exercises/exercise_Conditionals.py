"""<h1>Exercícios:<h1>

1. Construa uma condição para verificar se o número é múltiplo de 3.
"""
# x=7
# if x%3==0:
#   print("x é múltiplo de 3")
# else:
#   print("x nao é múltiplo de 3")

"""2. Crie 3 condicionais utilizando a estrutura elif."""
x = 7
y = 8
z = 9
if x == y or x == z:
    print('equals')
elif z > y and z > x:
    print('Z is bigger than x and y')
else:
    print('y is bigger')


"""
3. Crie uma lista e verifique se ela contém os números 7 e 3.
"""
lista = [0, 1, 2, 4, 5, 6, 7, 8 , 9]
if 3 in lista and 7 in lista:
    print('3 e 7 estao na lista')
elif 7 in lista:
    print('7 está na lista mas 3 nao está.')
else:
    print('Nem 3 e nem 7 estao na lista')

"""<h1>Desafio:<h1>

Crie uma lista com 5 valores e uma tupla com 10 valores, verifique se algum valor da lista está contido na tupla.
"""

lista1 = [5, 6, 7, 8 , 9]
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8 , 9)

for i in tupla:
    if i in lista1:
        print(i, 'está na lista e na tupla.')
