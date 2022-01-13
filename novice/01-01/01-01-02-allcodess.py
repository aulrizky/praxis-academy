# the_world_is_flat = True
# if the_world_is_flat:
#     print("be carefull not to fall off")

# print("""\
# Usage: thingy [OPTIONS]
#     -h                        Display this usage message
#     -H hostname               Hostname to connect to
# """)

# x = int(input("please enter an interger: "))
# if x < 0:
#     x = 0
#     print('negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('single')
# else:
#     print('more')

# words = ['cat','window','defenestrate']
# for w in words:
#     print(w,len(w))

# users = {
#     'Hans':'active',
#     'Elenore':'inactive',
#     '景太郎': 'active'
# }
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# active_users = {}
# for user,status in users.items():
#     if status == 'active':
#         active_users[user] = status

# print(active_users)

# for i in range(5):
#     print(i)

# a = ['Mary','had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i,a[i])

# for n in range(2,10):
#     for x in range(2,n):
#         if n % x == 0:
#             print(n,'equals',x,'*',n//x)
#             break
#     else:
#         print(n,'is a prime number')

# for num in range(2,10):
#     if num % 2 ==0:
#         print('found an even number',num)
#         continue
#     print('found an odd number',num)

# from typing import Match


# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not Found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "something's wrong with the internet"


# internet_status = 400
# print(http_error(internet_status))


# class Point:
#     x:int
#     y:int

#     __match_args__=["x","y"]

#     def __init__(self,x,y):
#         self.x = x
#         self.

# def where_is(point):
#     match point:
#         case Point(x=0,y=0):
#             print("Origin")
#         case Point(x=0,y=y):
#             print(f"Y={y}")
#         case Point(x=x,y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere Else")
#         case _:
#             raise ValueError("Not a point")


# Point(1,vars)
# # Point(1, y=vars)
# # Point(x=1, y=vars)
# # Point(y=vars, x=1)

#defining Function
# def fib(n):
#     '''Print a fibonacci series up to n'''
#     a,b = 0,1 
#     while a < n :
#         print (a,end=' ')
#         a, b = b, a + b 
#         print()

#fib(2000)
# fib 
# f = fib
# f(100)

# def fib(n):
#     ''' return list containing the fibonaci series up to n.'''
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result

# #default argument valuees
# def ask_ok(prompt, retries = 4, reminder= 'Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y','ye','yes'):
#             return True
#         if ok in ('no','nop','nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user respons')
#         print(reminder)

# ask_ok('Do you really want to quit? ')y
# i = 5 

# def f(arg=i):
#     print(arg)
# i= 6
# f()

# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")


# parrot(1000)                                          
# parrot(voltage=1000)                                  
# parrot(voltage=1000000, action='VOOOOOM')             
# parrot(action='VOOOOOM', voltage=1000000)             
# parrot('a million', 'bereft of life', 'jump')         
# parrot('a thousand', state='pushing up the daisies')

# def function(a):
#     pass

# function(0, a=0)

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

#special Parameters

# def standard_arg(arg):
#     print(arg)

# def pos_only_arg(arg,/):
#     print(arg)

# def kwd_only_arg(*, arg):
#     print(arg)
# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)
# # standard_arg(2)

# # pos_only_arg(1)
# # pos_only_arg(arg=1)

# # kwd_only_arg(arg =3)

# # combined_example(1, 2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3)

# def foo(name, **kwds):
#     return 'name' in kwds


# def foo(name, /, **kwds):
#     return 'name' in kwds

# foo(1, **{'name': 2})

#arbitary argument
# def write_multiple_items(file, separator, *args):
#     file.write(separator.join(args))

# def concat(*args, sep="/"):
#     return print(sep.join(args))

# concat("earth", "mars", "venus")
# concat("earth", "mars", "venus", sep=".")


#unpacking arguments list
# list(range(3, 6))

# args = [3, 6]
# list(range(*args))


# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")

# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)

# f(0)

# def my_function():
#     """Do nothing, but document it.
#     No, really, it doesn't do anything.
#     """
#     pass

# print(my_function.__doc__)


# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs

# f('spam')

# from enum import Enum
# class Color(Enum):
#     RED = 0
#     GREEN = 1
#     BLUE = 2

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")