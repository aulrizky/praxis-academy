# year = 2016
# event = 'Referendum'

# print(f'result of the {year} {event}')

# yes_votes = 42_572_654
# no_votes = 43_132_495
# percentage = yes_votes/(yes_votes + no_votes)
# print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

# s = 'hello, world'
# print(str(s))
# print(repr(s))
# print(str(1/7))

# x = 10 * 3.25
# y = 200 * 200
# # s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'

# # print(s)

# hello = 'hello, world\n'
# hellos = repr(hello)
# print(hellos)

# print(repr((x, y, ('spam', 'eggs'))))

# import math

# print(f'the value of pi is approximately {math.pi:.3f}.')

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

# for name, phone, in table.items():
#     print(f'{name:10} ==> {phone:10d}')

# animals = 'eels'
# print(f'my hovercraft is full of {animals}')
# print(f'my hovercraft is full of {animals!r}')

# print('we are the {} who say "{}!"'. format('knights','Ni'))

# print('{0} and {1} .'.format('spam','eggs','spam'))
# print('{1} and {0} .'.format('spam','eggs','spam'))
# print('this {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; sjoerd: {0[Sjoerd]:d};' 'Dcab: {0[Dcab]:d}'.format(table))

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# for x in range(1,11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


"""7.1.3. Manual String Formatting"""

# for x in range(1,11):
    # print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # print(repr(x*x*x).rjust(4))

# print('12'.zfill(5))
# print('-3.14'.zfill(7))

# print('3.14159265359'.zfill(5))

"""7.1.4. Old string formatting"""

# import math 
# print('the value of pi is approximately %5.3f.'% math.pi)

"""7.2. Reading and Writing Files"""

#f = open('workfile','w')

# with open('workfile') as f:
#      read_data = f.read()

# f.closed
# f = open('workfile','r')
# print(f.read())
# print(f.readline())

# f = open('workfile','w')
# print(f.write('test \n'))
# f = open('workfile','r')
# print(f.readline())

#f.write('This is a test\n')
# value = ('the answer', 42)
# s = str(value) 
# f.write(s)

# import json
# x = [1,'simple','list']
# print(json.dumps(x))
# print(json.dumps(x, f))
# x = json.load(f)