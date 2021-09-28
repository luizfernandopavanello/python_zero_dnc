"""Exercícios Lista:

1. Construa uma lista de inteiros e ordene elas do maior para o menor.
2. Adicione os valores 10,7,33,22 com uma única linha de código e deixe-os ordenados também em uma segunda linha de código.

lista = [0, 1, 2, 4, 3, 5, 8, 7, 9]
lista.reverse()
print(lista)

lista.extend((10, 7, 33, 22))
print(lista)

lista.sort()
print(lista)

3. Gere uma lista de nomes e ordene ela pelo tamanho de cada nome.

lista_Names=['Peter', 'Fulano', 'Ciclano', 'Pet']
lista_Names.sort(key=len, reverse=True)
print(lista_Names)

4. Crie uma lista que vá de 1 até 100.

list_numbers_0_100 = [num for num in range(101)]
print('List: ', list_numbers_0_100)

5. Em uma nova lista adicione somente os valores ímpares de 1 a 100.

list_odds = [odd for odd in range(101) if odd % 2 != 0]
print('Odds:', list_odds)

"""

"""Exercícios String:

1. Crie uma paragráfo contando uma experiência de vida e armazene isso em uma string. Depois retorne a quantidade de palavras desse parágrafo.

texto = 'Vou Treinar todo dia Python'
text = texto.split()
print(len(text))

2. Conte a quantidade de nomes próprios e de números que aparecem na história.

print(texto.find('Python'))

3. Conte a quantidade de vogais que aparecem na história.

texto = 'Vou Treinar todo dia Python'

texto = texto.casefold()

count = {x:sum([1 for char in texto if char == x]) for x in 'aeiou'}
 
print("Total Number of Vowels in this String = ", count)

4. Conte a quantidade de linhas que aparece na string.

5. Utilize pelo menos mais 3 métodos próprios pra string que não apareceu em aula mas estão na referência.

"""