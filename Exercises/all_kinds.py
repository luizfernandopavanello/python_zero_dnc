'''Sort Numerical Data Given as Strings in a list'''
nums = ['5', '1', '3', '2', '4']
nums = [int(i) for i in nums]
nums.sort()
print(nums)


'''Add two Lists using map and lambda'''
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

result = map(lambda x, y : x + y, nums1, nums2)
print(list(result))

'''filter vowels from list'''

def vowel(char):
    if char.lower() in 'aeiou':
        return True
    else:
        return False

chars = ['A', 's', 'S', 'e', 'a']
print(list(filter(vowel, chars)))

'''filter vowels from list using filter and Lambda Function'''

print(list(filter(lambda x : x.lower() in 'aeiou', chars)))
