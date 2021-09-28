"""
    Tendo o seguinte dicionário:
dicionario={'pessoa_1':{'nome':'Peterson','sobrenome':'Almeida'},'pessoa_2':{'nome':'Maria','sobrenome':'Silva'},'pessoa_3':{'nome':'Jose','sobrenome':'Santos'}}
Escreva o código que retorna e imprima o nome completo de cada pessoa em uma lista, primeiro o nome do Peterson, depois do Peterson e da Maria e depois de todo mundo, isso tudo de uma vez só.
Observação: Imprima apenas o resultado limpo no output sem incrementar outras coisas, palavras etc.
"""
dicionario={'pessoa_1':{'nome':'Peterson','sobrenome':'Almeida'},'pessoa_2':{'nome':'Maria','sobrenome':'Silva'},'pessoa_3':{'nome':'Jose','sobrenome':'Santos'}}
names = [ ]
for pessoa in dicionario.values():
    names = pessoa.get('nome') + ' ' + pessoa.get('sobrenome')
    print(names)