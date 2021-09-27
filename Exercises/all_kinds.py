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

