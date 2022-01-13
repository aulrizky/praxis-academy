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

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")