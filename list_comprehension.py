# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

neg_zero_nums = [i for i in numbers if i <= 0]
print(neg_zero_nums)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# flattened_list = [ number for row in list_of_lists for number in row for number in row for number in row]
# print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

output = [num for row in list_of_lists for row in row for num in row]
print(output)

result = [tuple(i ** j for j in range(7)) for i in range(11)]
print(result)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [[country.upper(), country[:3].upper(), capital.upper()] 
          for [(country, capital)] in countries]

dic = [{'country': country.upper() , 'capital': capital.upper()}
       for [(country, capital)] in countries]

print(output)
print(dic)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat = [first_name +' ' + last_name for [(first_name, last_name)] in names ]
print(concat)

slope = lambda m , x, b : (m * x) + b

print(slope(8 , 9 , 4))