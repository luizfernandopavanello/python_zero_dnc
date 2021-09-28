"""
    Tendo o seguinte dicionário:
dicionario={'pessoa_1':{'nome':'Peterson','sobrenome':'Almeida'},'pessoa_2':{'nome':'Maria','sobrenome':'Silva'},'pessoa_3':{'nome':'Jose','sobrenome':'Santos'}}
Escreva o código que retorna e imprima o nome completo de cada pessoa em uma lista, primeiro o nome do Peterson, depois do Peterson e da Maria e depois de todo mundo, isso tudo de uma vez só.
Observação: Imprima apenas o resultado limpo no output sem incrementar outras coisas, palavras etc.

dicionario={'pessoa_1':{'nome':'Peterson','sobrenome':'Almeida'},'pessoa_2':{'nome':'Maria','sobrenome':'Silva'},'pessoa_3':{'nome':'Jose','sobrenome':'Santos'}}
names = [ ]
for pessoa in dicionario.values():
    names = pessoa.get('nome') + ' ' + pessoa.get('sobrenome')
    print(names)
    
"""

# a =['dnc','abc','bnc','mnc','dnc','bnc','Dnc','ncd','dnc','dncdnc','ddnc']
# b =['dnc','abc','bnc','mnc','dnc','bnc','Dnc','ncd','dnc','dncdnc','ddnc','xms','cds','dn','cdn','dnc','xml','a']

# def frequency(words):
#     print("A palavra 'dnc' aparece", a.count('dnc') + b.count('dnc') , "vezes nas listas A e B.")

# frequency(a)

"""
  Use uma função nativa para descobrir qual o menor número da lista abaixo:
lista = [77,80,90,23,44,15,11,25,68,14,22,99]
Observação: Declare uma variável que contenha o resultado e imprima para garantir que o resultado seja mostrado na janela "Output"
Imprima apenas o resultado limpo no output sem incrementar outras coisas, palavras etc.  
"""
# lista = [77,80,90,23,44,15,11,25,68,14,22,99]

# smallest = min(lista)

# print(smallest)

"""
Some os valores da lista dinheiro:
dinheiro = [10,2,30,23,12,42,543,24,33,34,123.5,1231,53,123,6456,234,45]
Observação: Declare uma variável que contenha o resultado e imprima para garantir que o resultado seja mostrado na janela "Output"
Imprima apenas o resultado limpo no output sem incrementar outras coisas, palavras etc.
"""
# dinheiro = [10,2,30,23,12,42,543,24,33,34,123.5,1231,53,123,6456,234,45]

# sum = sum(dinheiro)

# print(sum)

"""
Crie uma função lambda que adiciona + 1 para os elementos pares da lista abaixo transformando todos os pares em ímpares e mantendo os ímpares sem alterações.
lista=[1,10,3,4,1,2,3,4,5,3,1,2,3]
Observação: Imprima apenas o resultado limpo no output sem incrementar outras coisas, palavras etc.
"""
# lista=[1,10,3,4,1,2,3,4,5,3,1,2,3]

# filtered_result = map(lambda x : x + 1 if x % 2 == 0 else x, lista)
# print(list(filtered_result))

"""
Ordene a lista abaixo:
lista = [77,80,90,23,44,15,11,25,68,14,22,99]
Observação: Declare uma variável que contenha o resultado e imprima para garantir que o resultado seja mostrado na janela "Output"
Observação: Imprima apenas o resultado limpo no output sem incrementar outras coisas, palavras etc.
"""
# lista = [77,80,90,23,44,15,11,25,68,14,22,99]

# ordered_list =  sorted(lista)
# print(ordered_list)

"""Considerando a Lista:
Lista=[1,2,3,4,5,1,2,3,4,5]
Escreva o código para obter os itens sem repetições
Observação: Declare uma variável que contenha o resultado e imprima para garantir que o resultado seja mostrado na janela "Output"
Imprima apenas o resultado limpo no output sem incrementar outras coisas, palavras etc.
"""
# lista=[1,2,3,4,5,1,2,3,4,5]

# no_repetition = set(lista)
# print(no_repetition)

"""
Considerando as informações abaixo, crie uma função para que a saída seja a posição da palavra 'dnc':
a =['dnc','abc','bnc','mnc','dnc','bnc','Dnc','ncd','dnc','dncdnc','ddnc']
b =['dnc','abc','bnc','mnc','dnc','bnc','Dnc','ncd','dnc','dncdnc','ddnc','xms','cds','dn','cdn','dnc','xml','a']
Imprima apenas a saída, ou seja, qual a posição da palavra 'dnc'.
Observação: Imprima apenas o resultado limpo no output sem incrementar outras coisas, palavras etc.
"""

