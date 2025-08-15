result = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(f"Concatinated String: {result}")

company = 'Coding For All'
print(company)

print(len(company))

print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[7:])

print('Coding' in company)
print(company.index('Coding'))

company = company.replace('Coding', 'Python')
print(company)

company = company.replace("All", "Everyone")
print(company)

print(company.split(" "))

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

print(company[0])
print(company[-1])
print(company[10])

abb_str = company.split(" ")
print(len(abb_str))

print(f"{company[0][0]}{company[1][0]}{company[2][0]}".upper())

print(company.index('P'))

print(company.index('F'))

print(company.rfind('I'))

text = 'You cannot end a sentence with because because because is a conjunction'

print(text.index('because'))
print(text.rfind('because'))

result = text.replace('because because because', '')
print(result)

print('Coding For All'.startswith('Coding'))
print('Coding For All'.endswith('Coding'))
print('    Coding For All   '.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print((' # '.join(libs)))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\t\tCity\nHasham\t21\tPakistan\tWah')

radius = 10
area = 3.14 * radius ** 2
print(f"Teh are of circle with radius {radius} is {area}")
