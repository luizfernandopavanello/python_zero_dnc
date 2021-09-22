<h1> Condicionais </h1>

<h2> Relembrando um pouco de operações </h2>
<b> Geral:</b><br>
Toda condicional em um código depende do resultado de uma operação booleana.
<br> <br>

> <b> As principais condições utilizadas são:</b><br>
<b>==:</b> Verifica se os valores são exatamente iguais.<br>
<b>>:</b> Verifica se o valor a esquerda é maior do que o valor a esquerda.<br>
<b><:</b> Verifica se o valor a esquerda é menor do que o valor a esquerda. <br>
<b>>=:</b> Verifica se o alor a esquerda é maior ou igual comparado ao valor a esquerda. <br>
<b><=:</b> Verifica se o valor a esquerda é menor ou igual comparado ao valor a esquerda. <br>
<b>in:</b> Verifica se os a esquerda está contido no valor a direita. <br>
<br>

## As condicionais em python são declaradas utilizando a sintaxe abaixo:<br> 

<b>if x == y:</b> *Compara se x e y são iguais*<br>
<b>elif x > y:</b> *Caso x e y seja diferente compara se x é menor que y*<br>
<b>else:</b> *Caso nenhuma condição acima seja verdade ele executa esse bloco.*
"""

#é possível também fazer uma operação antes do x e fazer a verificação com o seu resultado.
x=4
if x%2==0:
  print("x é par")
else:
  print("x é ímpar")

#caso tenha mais de uma condição para validar é utilizado o elif como um else+if
#print verdadeiro no else
x = 5
y = 10
if x == y:
  print("são iguais")
elif x > y:
  print("x é maior que y")
else:
  print("são diferentes e x não é maior que y")

#print verdadeiro no elif
x = 5.5
y = 5
if x == y:
  print("são iguais")
elif x > y:
  print("x é maior que y")
else:
  print("são diferentes e x não é maior que y")

#print verdadeiro no if
x = 5
y = 5
if x == y:
  print("são iguais")
elif x > y:
  print("x é maior que y")
else:
  print("são diferentes e x não é maior que y")

"""<h1> Dois novos tipos de váriaveis</h1>

Nessa etapa vamos aprender mais dois tipos de váriaveis, até essa etapa já vimos string, inteiros, booleanas e números reais, mas e se quisermos armazenar diversos valores? Temos que declarar diversas variáveis? Para esses casos podemos a Lista e a Tupla, ambas são para armazenar diversos valores em uma única variável.

*   <b>Lista:</b> varíavel mutável que armazena diversos valores heterogêneos ou homogêneos
*   <b>Tupla:</b> varíavel imutável que armazena diversos valores heterogêneos ou homogêneos.

A grande diferença entre as duas é que a lista permite alterar valores dentro dela enquanto a tupla não permite alterações.

<h2> Exemplos:</h2>

É possível também fazer operações entre strings.
"""

#criação de lista e tupla com valores de diferentes tipos
lista = ['oi',5,'tchau']
tupla = ('oi',5,'tchau')
#por mais que contenham os mesmos valores, são tipos diferentes e isso torna elas diferentes
lista==tupla

#print do primeiro valor da lista e da tupla
print(lista[0])
print(tupla[0])
#quanto comparamos o valor podemos ver que é igual
lista[0]==tupla[0]

"""Podemos adicionar, remover ou alterar valores da lista, enquanto a tupla não permite essas ações por ser imutável."""

#adição de um elemento na lista
lista.append('ultimo')
#print da lista
print(lista)
#atribuindo um novo valor ao último elemento da lista
lista[-1]='alterado'
#print da lista
print(lista)
#remoção (pop) do último elemento da lista
lista.pop(-1)
print(lista)

"""É possível converter a tupla em lista para adicionar valores."""

#convertendo tupla em lista
tupla = list(tupla)
#adicionando um valor ao final da tupla
tupla.append('adicionado')
#printando a tupla e seu type
print(tupla,type(tupla))

"""Verificando valores dentro de uma lista


"""

#verificando se "oi" está na lista
if 'oi' in lista:
  print('oi está na lista')

#verificando se "ei" está na lista
if 'ei' in lista:
  print('ei está na lista')
else:
  print('ei não está na lista')

"""Podemos também utilizar as expressões and e or para colocar duas ou mais condições dentro da mesma linha do if"""

#verificando se x ESTÁ NA lista E x maior > que 3 E x < menor que 10
x=5
if x in lista and x>3 and x<10:
  print("x está na lista, é maior que 3 e menor do que 10")

#verificando se x NÃO ESTÁ na lista OU x maior > que 3 E x < menor que 10
x=5
if x not in lista or x>3 and x<10:
  print("ou x não está na lista ou é maior que 3 e menor do que 10")

"""Nas aulas e exercícios adiantes aprenderemos cada vez mais novos conceitos na medida que nos aprofundamos no que já vimos. É recomendado que seja feito todos os exercícios e pontuado cada dúvida que surgir.

<h2> Dicas </h2>

> O python nos dá uma série de opções para resolver o mesmo problema, cabe a nós decidir qual é o mais adequado para cada situação. Tuplas e listas são ótimos exemplos disso, ambos podem resolver o problema de armazenar diversos valores em uma única variável, entretanto um é mutável e a outra não, cabe analisarmos a situação e ver qual melhor atende a necessidade. <br> <br>Caso você queira saber mais sobre quando usar qual tipo e quais as suas particularidades, esse [link](https://pt.stackoverflow.com/questions/192727/quando-usar-listas-e-quando-usar-tuplas#:~:text=As%20tuplas%20s%C3%A3o%20sequ%C3%AAncias%20imut%C3%A1veis,armazenamento%20em%20set%20ou%20dict%20).) no StackOverflow (se você ainda não conhece essa plataforma, é uma ótima oportunidade de conhecer, no decorrer do curso e da sua nova carreira, ela será sua grande companheira) vai te ajudar bastante.
"""

x = 1
y = 1
x+=10
y+=10
print('x:',x,'y:',y)
print("x += 10 é equivalente a: x = x + 10")

"""<h1>Exercícios:<h1>

1. Construa uma condição para verificar se o número é múltiplo de 3.
"""



"""2. Crie 3 condicionais utilizando a estrutura elif."""



"""
3. Crie uma lista e verifique se ela contém os números 7 e 3.
"""



"""<h1>Desafio:<h1>

Crie uma lista com 5 valores e uma tupla com 10 valores, verifique se algum valor da lista está contido na tupla.
"""

