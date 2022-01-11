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
class Point:
    x:int
    y:int

def where_is(point):
    match point:
        case Point(x=0,y=0):
            print("Origin")
        case Point(x=0,y=y):
            print(f"Y={y}")
        case Point(x=x,y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere Else")
        case _:
            raise ValueError("Not a point")


Point(0,0)
# Point(1, y=vars)
# Point(x=1, y=vars)
# Point(y=vars, x=1)