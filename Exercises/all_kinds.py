# '''Sort Numerical Data Given as Strings in a list'''
# nums = ['5', '1', '3', '2', '4']
# nums = [int(i) for i in nums]
# nums.sort()
# print(nums)


# '''Add two Lists using map and lambda'''
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# result = map(lambda x, y : x + y, nums1, nums2)
# print(list(result))

# '''filter vowels from list'''

# def vowel(char):
#     if char.lower() in 'aeiou':
#         return True
#     else:
#         return False

# chars = ['A', 's', 'S', 'e', 'a']
# print(list(filter(vowel, chars)))

# '''filter vowels from list using filter and Lambda Function'''

# print(list(filter(lambda x : x.lower() in 'aeiou', chars)))

"""
Case 1 → Uma empresa te enviou 3 listas, uma representa a largura, outra representa a altura e a terceira representa a área em m2 de determinado terreno, todas estão ordenadas entretanto tem alguns valores faltantes que precisam ser preenchidos. <br> Todos os terrenos dessa empresa são retângulares e você pode utilizar a fórmula abaixo:

---

*a = b. h (área = largura * altura)*

area = [200,'null',720,1500,1000,275,'null',1200,2400,'null']
altura = ['null',30,40,30,10,25,33,'null',12,20]
largura = [20,20,'null',50,100,'null',30,100,200,10]

def fill_in (a,b,h):
  total_area = [ ]
  total_largura = [ ]
  total_altura =[ ]
  for area,largura,altura in zip(a,b,h):
    if type(area)!=int:
      total_area.append(int(largura*altura))
    else:
      total_area.append(area)
    if type(largura)!=int:
      total_largura.append(int(area/altura))
    else:
      total_largura.append(largura)
    if type(altura)!=int:
      total_altura.append(int(area/largura))
    else:
      total_altura.append(altura)
  return (total_area,total_largura,total_altura)

(area,largura,altura) = fill_in(area,largura,altura)
print(area)
print(largura)
print(altura)

print("Os terrenos tem em média",sum(altura)/len(altura), "M de altura.")
print("Os terrenos tem em média",sum(largura)/len(largura), "M de lagura.")

print('No total a empresa tem',sum(area),'M, e a média total dos terrenos é de ',sum(area)/len(area),'M2')
"""

"""Case 2 → Você recebeu um arquivo chamado usuarios_feedback, nesse arquivo contém o comentário, nome, gênero e nota de usuários referente a um produto de sua empresas. Você precisa verificar quais as palavras que mais apareceram nos comentários:


usuarios_feedback = [{'nome':'Peter','nota':9,'genero':'M','comentario':'bom demais e agil'},
                {'nome':'Joao','nota':10,'genero':'M','comentario':'agil e eficiente'},
                {'nome':'user_not_found','nota':0,'genero':'M','comentario':'Horrível'},
                {'nome':'Marta','nota':10,'genero':'F','comentario':'muito agil bom demais'},
                {'nome':'Beatriz','nota':10,'genero':'F','comentario':'rápido e eficaz'},
                {'nome':'user_not_found','nota':2,'genero':'M','comentario':'ruim'},
                {'nome':'Jéssica','nota':10,'genero':'F','comentario':'agil'},
                {'nome':'José','nota':7,'genero':'M','comentario':'ok'},
                {'nome':'Elias','nota':5,'genero':'M','comentario':'precisa melhorar'},
                {'nome':'Miriã','nota':9,'genero':'F','comentario':'foi muito agil e rápido'},
                {'nome':'Maria','nota':10,'genero':'F','comentario':'muito bom e agil'}] 

# def frequency(faults):
#     words = [ ]
#     for user in faults:
#         words.extend(user['comentario'].split())
#         uniq_word = sorted(set(words))
#     for word in uniq_word:
#         print(words.count(word), word)

# frequency(usuarios_feedback)

def notas (x):
  masc = []
  fem = []
  for a in x:
    if a['genero']=='M':
      masc.append(a['nota'])
    elif a['genero']=='F':
      fem.append(a['nota'])
  print('média masc =',sum(masc)/len(masc),'média fem=',sum(fem)/len(fem))
  return masc,fem
masc, fem = notas(usuarios_feedback)
print(masc,fem)

"""
"""
Case 3: Sua empresa te passou uma lista com requisições de treinamentos (muitos repetidos), você tem que definir o cenário que melhor atenda os pedidos, o budget é de 150 moedas e você tem um dicionário que contem o nome do treinamento e o valor dele
"""

treinamentos = [{'treinamento':'Scrum','moedas':30},
                     {'treinamento':'Data Science','moedas':40},
                     {'treinamento':'Gestão de Projetos','moedas':50},
                     {'treinamento':'Marketing','moedas':30},
                     {'treinamento':'Cloud','moedas':20},
                     {'treinamento':'Blockchain','moedas':10},
                     {'treinamento':'Python','moedas':30}]

pedidos = ['Scrum','Data Science','Gestão de Projetos','Marketing','Cloud','Python','Python','Python',
           'Scrum','Data Science','Gestão de Projetos','Marketing','Data Science','Gestão de Projetos',
           'Python','Marketing','Data Science','Gestão de Projetos','Data Science','Gestão de Projetos','Data Science']

def get_value (x,b):
  for a in x:
    if a['treinamento']in b:
      print ('valor:',a['moedas'])
      return a['moedas']

ped = sorted(set(pedidos))
for a in ped:
  print('solicitações:',pedidos.count(a),'\ntreinamento:',a)
  valor = get_value(treinamentos,a)
  for b in treinamentos:
    if a == b['treinamento']:
     b['total_pedidos']=pedidos.count(a)
     


