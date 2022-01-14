# while True print('Hello world')

# 10 * (1/0)

#4 + spam*3

#'2' + 2

# while True:
#     try:
#         x = int(input('please enter a number: '))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
# except (RuntimeError, TypeError, NameError):
#     pass

# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("B")
#     except C:
#         print("C")
#     except B:
#         print("D")


# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("could no convert data to an interger. ")
# except BaseException as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise


# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print("Couldn't open",arg)
#     else:
#         print(arg, 'has', len(f.readlines()),'lines')
#         f.close()

#  raise Exception('spam','eggs')
# ... except Exception as inst:
# ...     print(type(inst))
# ...     print(inst.args)
# ...     print(inst)
# ...     
# ...     x,y = inst.args
# ...     print('x =',x)
# ...     print('y =',y)
# ... 
# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = egg

# >>> def this_fails():
# ...     x = 1/0
# ... 
# >>> try:
# ...     this_fails()
# ... except ZeroDivisionError as err:
# ...     print('handling run-time error:', err)
# ... 
# handling run-time error: division by zero


# raise NameError('HiThere')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: HiThere

# >>> try:
# ...     raise NameError('HiThere')
# ... except NameError:
# ...     print('an exception flew by!')
# ...     raise
# ... 
# an exception flew by!
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# NameError: HiThere

# >>> def func():
# ...     raise ConnectionError
# ... 
# >>> 
# >>> try:
# ...     func()
# ... except ConnectionError as exc:
# ...     raise RuntimeError('Failed to open databasa') from exc
# ... 
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#   File "<stdin>", line 2, in func
# ConnectionError

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# RuntimeError: Failed to open databasa


# >>> try: 
# ...     raise KeyboardInterrupt 
# ... finally: 
# ...     print('goodbye, world!')
# ... 
# goodbye, world!
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# KeyboardInterrupt
# >>> 


# def bool_return():
#     try:
#         return True
#     finally:
#         return False

# bool_return()

# def divide(x, y):
#     try:
#         result = x/y
#     except ZeroDivisionError:
#         print('division by zero')
#     else:
#         print('result is',result)
#     finally:
#         print('excuting finnaly clause')

#divide(2, 1)
#divide(2,0)
#divide('2','1')

# for line in open('mylife.txt'):
#     print(line, end="")

# with open("myfile.txt") as f:
#     for line in f:
#         print(line, end='')


