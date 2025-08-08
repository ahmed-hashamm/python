#empty list
arr = []

#list with items
arr = [1, 3, 5, 'apple', 'kela']
length = len(arr)
print(length)

print(arr[0])
print(arr[int(length /2)])
print(arr[length - 1])

mixed_data_types = ['Hasham', 21, 5.11, False, 'Wah']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))

len_comp = len(it_companies)

print(it_companies[0])
print(it_companies[int(len_comp /2)])
print(it_companies[len_comp - 1])

it_companies[2] = 'Softonic'
print(it_companies)

it_companies.append('Kode Studio')
it_companies.insert(int(len(it_companies) /2), 'HouseIt')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print((' # ').join(it_companies))

print('Google' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[3:])

print(it_companies[:-3])

print(it_companies.pop(0))
print(it_companies.pop(-1))
print(it_companies.pop(int(len(it_companies)/2)))
print(it_companies.clear())

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = min(ages)
max_age = max(ages)
avg = sum(ages)/len(ages)
print(min_age)
print(max_age)
print(ages[int(len(ages)/2)])
print(avg)
print(max_age - min_age)
print(abs(max_age - avg) is abs(min_age - avg))

from countries import countries

mid = len(countries) // 2

print(countries[mid] if mid % 2 !=0 else countries[mid:mid+2])

# print(mid)

total = len(countries)
print(total)
split = (total + 1) // 2
first_half = countries[: split]
second_half = countries[split: ]
print(len(first_half))
print(len(second_half))

coun = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

ch, rus, us, *scandic_countries = coun

print(ch, rus, us, scandic_countries)