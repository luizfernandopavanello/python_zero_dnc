<h1> Operações </h1>

<h2> Relembrando um pouco de variáveis </h2>
<b> Geral:</b><br>
Variáveis são utilizadas para armazenar valores dentro do código, existem diferentes tipos de variáveis, cada uma adequada para alguma situação.
<br> <br>

> <b> Alguns dos tipos primários de variáveis</b><br>
<b>int:</b> utilizadas para armazenar números inteiros.<br>
<b>float:</b> utilizada para pontos flutuantes, ou seja, números reais.<br>
<b>string:</b> utilizadas para armazenar textos. <br>
<b>boleeano:</b> utilizadas para armazenar condição binária de True (verdadeiro) ou False (falso). <br>
<br>




Em python não precisamos declarar o tipo de variável, ele reconhece de forma automática.<br>

<h1> Operações</h1>

Principais operações em python são:

*   <b>Soma:</b> para operações de soma é utilizado o sinal de +
*   <b>Subtração:</b> para operações de subtração é utilizado o sinal de -
*   <b>Multiplicação:</b> para operações de Multiplicação é utilizado o sinal de *
*   <b>Divisão:</b> para operações de divisão é utilizado o sinal de /

<h2> Exemplos:</h2>
"""

#soma de inteiros no print
inteiro_1 = 5
inteiro_2 = 7
#print dos inteiros + strings descrevendo operação
print('somando:',inteiro_1, '+', inteiro_2,'=',inteiro_1 + inteiro_2)

#soma de floats no print
real_1 = 3.45
real_2 = 5.50
print('multiplicando:',real_1, '+', real_2,'=',real_1 + real_2)

"""É possível também fazer operações entre strings."""

#soma de strings no print
texto = 'oi'
texto_2 = "tchau"
print('Somando:',texto, '+', texto_2,'=',texto + texto_2)

# E também multiplicar uma string por um inteiro no print
print('Multiplicando:',texto*3 )

"""Podemos também atribuir os valores das operações em uma nova variável ou atribuir como o novo valor da variável já existente."""

#somando dois inteiros e atribuindo a uma nova variável
inteiro_3 = inteiro_1 + inteiro_2
#printando a váriavel e seu type
print(inteiro_3, type(inteiro_3))

"""Ao realizar operações o tipo da nossa variável pode mudar."""

#somando um inteiros e um número real e atribuindo a uma nova variável
inteiro_3 = inteiro_1 + real_1
#printando a váriavel e seu type
print(inteiro_3, type(inteiro_3))

"""Existem também operadores que os resultados são booleanos, esses operadores são voltados para comparação

*   Maior > Menor 
*   Igual: ==
*   Diferente: !=



"""

#printando comparações entre 2 valores com cada um dos operadores
print(5>3)
print(5<3)
print(7==7)
print(7==7.5)
print(7!=7)
print('7'==7)

"""Por trás do operador booleano existe o 0 para False e o 1 para True, logo se realizarmos uma soma o resultado será o seguinte"""

#somando valores booleanos True
True + True

#somando true com false
True+False

#multiplicando true
True*3

#dividindo true e atribuindo a uma nova variavel
booleano = True/2
#printando o valor da variável e seu type
print(booleano,type(booleano))

"""O Python também fornece funções built in (nativas) que permitem você transformar o valor de uma variável."""

#o python possui a função "type()" já nativa e construída para mostar o tipo da variável
print('Booleano:',booleano, ' Tipo:',type(booleano))
#convertendo variável booleano para int
booleano = int(booleano)
#printando variável e seu type
print('Booleano:',booleano, ' Tipo:',type(booleano))
#convertendo o valor para string
booleano = str(booleano)
#printando variável e seu type
print('Booleano:',booleano, ' Tipo:',type(booleano))

"""<b><h2>Operações 2</h2>

Além das operações mais comuns, o Python nativamente oferece operações de:

*   <b>Módulo: </b> %
*   <b>Exponencial: </b> **
*   <b>Divisão com arredondamento: </b> //

<h2> Exemplos </h2>
"""

#basicamente a sobra da divisão
#Muito utilizado para verificar se um número é par, caso o resto da divisão por 2 for 0, ele é par
print(9%2)
print(4%2)

#Printando operação de 2 numeros com Exponencial
print(2 ** 2)
print('o mesmo que: ',2*2)
print(1.3 **3)
print('O mesmo que: ',1.3*1.3*1.3)

#Divisão com arredondamento
print(5//2)
print(5//3)
print(5//4)

"""<h2> Dicas </h2>

Um dos grandes motivos do Python ter conseguido tanto espaço é a constante atualização para deixar cada vez mais acessível, rápido e fácil codificar, então as operações visto acima podem ser feitas da seguinte forma:
"""

x = 1
y = 1
x+=10
y+=10
print('x:',x,'y:',y)
print("x += 10 é equivalente a: x = x + 10")

"""<h1>Exercícios:<h1>

1. Faça pelo menos 1 exemplo com cada operador visto utilizando variáveis do mesmo tipo.
"""

var1 = 1
var2 = 5
var3 = 9
var4 = var1 <= var3

print(var1 + var2)
print(var1 - var2)
print(var1 * var2)
print(var1 / var2)
print(var2**var2)
print(var3//var2)
print(var2 % 2)
print(var4)
print('5' == var2)

"""2. Repita o exercício 1 mas dessa vez utilizando variáveis de tipos diferentes, dessa vez verifique se o tipo dela alterou ou não."""

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

"""
3. Faça 3 operações com operadores diferentes utilizando o formato passado na em Dicas.
"""

x = 2
y = 3
x += 11
y += 11
x = x**2
x -= 150
print('x:',x,'y:',y)
print(x != y)
print("x += 11 é equivalente a: x = x + 11")