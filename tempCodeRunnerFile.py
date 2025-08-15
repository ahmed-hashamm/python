countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for country in countries:
#     print(country)
# for name in names:
#     print(name)
# for n in numbers:
#     print(n)

# def Upper(x):
#     return x.upper()

# upper_case = map(Upper, countries)
# print(list(upper_case))

# def square(x):
#     return x * x

# square_num = map(square, numbers)
# print(list(square_num))

# def land(country):
#     return country if 'land' in country else None
# filtered = filter(land, countries)
# print(list(filtered))

# def length(country):
#     return country if len(country) == 6 else None
# leng = filter(length, countries)
# print(list(leng))

# def start_w_E(country):
#     return country if country.startswith('E') else None
# start_E = filter(start_w_E, countries)
# print(list(start_E))


# from functools import reduce
# chaining = reduce(
#     lambda acc, x: acc + x,
#     filter(lambda x: x > 10,
#     map(lambda x : x * x, numbers)),
#     0)
# print(chaining)

# mixed_list = [
#     42,                     # integer
#     3.14,                   # float
#     "Hello",                # string
#     True,                   # boolean
#     None,                   # NoneType
#     [1, 2, 3],               # list
#     {"name": "Zohaib"},      # dict
#     (4, 5),                  # tuple
#     {9, 8, 7},               # set
#     bytes("data", "utf-8")   # bytes
# ]

# print(mixed_list)

# def get_string_lists(x):
#     return x  if isinstance(x, str) else None
# get_srings = filter(get_string_lists, mixed_list)
# print(list(get_srings))


# # Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# def get_sentence(a, b):
#     return a + ", " + b

# sentence = reduce(get_sentence, countries[:-1]) + ", and " + countries[-1] + " are north European countries"

# print(sentence)