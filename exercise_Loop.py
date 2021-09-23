'''Exercícios Loop:'''

'''1. Crie uma lista contendo os números pares de 0 até 100'''

# lista_pares = []
# for par in range(101):
#     if par % 2 == 0:
#         lista_pares.append(par)
# lista_pares
# print(lista_pares)

"""2. Transforme cada valor da lista anterior em um string."""
# print('Os valores da lista sao:', type(lista_pares))
# list_to_Str = ', '.join(map(str, lista_pares))
# print('String:',list_to_Str)        
# print('Os valores da lista sao:', type(lista_pares))
# print('Os valores da Lista String sao:', type(list_to_Str))
    

"""3. Compare os valores entre as listas e some os valores das 2 listas."""
# for number in lista_pares:
#     for num in list_to_Str:
#         if num != number:
#             print('Error: Unsupported operand type(s) for +: ', type(lista_pares), 'and', type(list_to_Str))
#             break
#         else:
#             print(number + num)


"""4. Crie um for para reproduzir a [sequência de Fibonacci](https://www.coc.com.br/blog/soualuno/matematica/o-que-e-a-sequencia-de-fibonacci#:~:text=A%20sequ%C3%AAncia%20de%20Fibonacci%20%C3%A9,no%20final%20do%20s%C3%A9culo%2012.&text=Desde%20que%20nenhum%20coelho%20morra,os%20n%C3%BAmeros%200%20e%201.)."""

# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1
       
       
"""5. Crie um for que execute até aparecer a palavra "parar"."""

# palavras=['continue','ok','segue','opa,','quase','parar',':)']
# busca = []

# for word in palavras:
#     if word != 'parar':
#         busca.append(word)
#     else:
#         print(busca)

"""6. Crie um Loop que percorra uma string e coloque a posição de cada caracter contida nela."""

# texto = 'vou fazer todos os exercícios'
# for a,b in enumerate(texto):
#   print(a,b)

"""7. Refaça o exercício 1 mas dessa vez pulando os espaços."""



"""8. crie duas listas e percorra as duas no mesmo for, se elas tiverem tamanhos diferentes descreva o que acontece."""

# texto_2 = texto.split()
# for a in texto_2:
#     for b in texto_2:
#         print(a, b) 

"""9. Faça a taboada feita em aula começando do número 9."""

# for num in range(9,10):
#     for num_2 in range(9,10):
#         print(num,'*',num_2,'=',num*num_2)
