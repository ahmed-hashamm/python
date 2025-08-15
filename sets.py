it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')

it_companies.remove('Apple')

try:
    it_companies.remove('apple')
except:
    print("not found") #shows error if item is not found

it_companies.discard('apple') #does not show error if ite is not found
join = A.union(B)
print(join)

inter = A.intersection(B)
print(inter)

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.symmetric_difference(B))
del A
del B
# print(A)
# print(B)

ages = set(age)
print(len(ages))
print(len(age))
print(len(ages) is len(age))

text = 'I am a teacher and I love to inspire and teach people'

words = text.split()
unique_words = set(words)
print(words)
print(unique_words)