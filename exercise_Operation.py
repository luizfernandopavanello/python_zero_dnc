#Exercícios:
#1. Faça pelo menos 1 exemplo com cada operador visto utilizando variáveis do mesmo tipo.

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

#2. Repita o exercício 1 mas dessa vez utilizando variáveis de tipos diferentes, dessa vez verifique se o tipo dela alterou ou não.

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

#3. Faça 3 operações com operadores diferentes utilizando o formato passado na em Dicas.

x = 2
y = 3
x += 11
y += 11
x = x**2
x -= 150
print('x:',x,'y:',y)
print(x != y)
print("x += 11 é equivalente a: x = x + 11")