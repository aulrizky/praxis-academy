# squares = []
# for x in range(10):
#     squares.append(x**2)

# print(squares)

# squares = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(10)]
# print(squares)

# x =[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(x)
# combs = []
# for x in [1,2,3]:
#     for y in  [3,1,4]:
#         if x != y:
#             combs.append((x,y))

# print(combs)

# vec = [-4, -2, 0, 2, 4]
# a =[x*2 for x in vec]
# print(a)
# b = [x for x in vec if x >= 0]
# print(b)
# c = [abs(x) for x in vec]
# print(c)

# freshfruit = ['banana', 'loganberry', 'passion fruit']
# print([weapon.strip() for weapon in freshfruit])

# print([(x, x**2) for x in range(6)])

# vec = [[1,2,3], [4,5,6], [7,8,9]]

# print([num for elem in vec for num in elem])

# from math import pi
# c=[str(round(pi, i)) for i in range(1, 6)]

# print(c)

## Nested list comprehension 

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# n= [[row[i] for row in matrix] for i in range(4)]

# print(n)

# transposed = []
# for i in range (4):
#     transposed.append([row[i] for row in matrix])

# print(transposed)

# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# print(transposed)

# x = list(zip(*matrix))
# # print(x)

# for a in x:
#     print(a)
# a = [-1, 1, 66.25, 333, 333, 1234.5]

# del a[0]
# print (a)
# del a[2:4]
# print(a)

# del a[:]
# print(a)

# t = 12345, 54321, 'hello!'
# # print(t[0])
# print(t)

# u = t,(1,2,3,4,5,6,7,8)
# v = ([1, 2, 3, 4, 5],[1, 3, 8])
# print(v)

# empty = ()
# singleton = 'hello',
# print(len(empty))
# print(len(singleton))

# x = 12345123
# y = 12999
# u = 'hello',

# t = x, y, u

# print(t)

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)

# print('orange' in basket)
# print('gumbo' in basket)
# a = set('abracadabra')
# b = set('alacazam')

# print(a)
# print(a-b)
# print(a|b)
# print(a&b)
# print(a^b)

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127

# print(tel)
# print(tel['jack'])
# del tel['sape']
# tel['irv'] = 4127
# print(tel)
# print(list(tel))
# print(sorted(tel))
# print('guido' in tel)
# print('jack' in tel)

# print (dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# )
# print({x: x**2 for x in (2, 4, 6)})
# print(dict(sape=4139, guido=4127, jack=4098))

# knight = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knight.items():
#     print(k, v)


# for i,v in enumerate(['tic','tac','toe']):
#     print(i, v)

# questions = ['name', 'quest', 'favorite color'] 
# answers = ['lancelot', 'the holy grail', 'blue']

# for q, a in zip(questions, answers):
#     print('what is your {0} it is {1}. '.format(q, a))

# for i in reversed(range(1, 10, 2)):
#     print(i)

# basket = ['apple','orange','apple','pear','orange','banana']

# for f in sorted(set(basket)):
#     print(f)


# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'),47.8]
# filter_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filter_data.append(value)

# print(filter_data)

# string1, string2, string3 = '', 'Trondhim', 'hammer dance'

# non_null = string1 or string2  or string3
# print(non_null)

# (1, 2, 3)              < (1, 2, 4)
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, -1)
# (1, 2, 3)             == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)