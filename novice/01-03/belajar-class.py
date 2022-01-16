# class myclass:
#     x = 5 #feature of my class

# p1 = myclass()
# print(p1.x)

# class Person:
#     '''fungsi yang selalu dipanggil setiap waktu ketika kelas tersebut dipakai'''
#     def __init__(self, name, age): 
#         self.name = name
#         self.age = age

# p1 = Person('waskito', 56)

# print(p1.name)
# print(p1.age)

# class Person:
#     ''' self adalah parameter yang mereferensikan kelas yang sekarang dan digunakan untuk mengakses variable yang berasal dari class '''
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
    
#     def myfunc(self):
#         print("hello my name is "+ self.name )
#         print("i'm {0} years old".format(self.age))
#         print(f"i live in {self.address}")

# p1 = Person("john",36,"bali" )
# p1.age = 40 
# p1.myfunc()
#import turtle

# class car:
#     def move_forward():
#         drive = 60
#         stop = 0
#         return print(f'speed {drive}')
    
#     def stoping():
#         drive = 0
#         stop = 50
#         return print(f'speed {drive}')

#     def turning():
#         drive = 20
#         stop = 0
#         turn = 60
#         return print(f'speed {drive}')

# p1 = car
# p1.move_forward()

# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine

# '''Order and report work-flow
# input>>find_drink>>get_item>>check_resource>> make_coffee>>make payment
# check resource : report
# check profit : report'''


# order_machine = Menu()
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# is_on = True
# while is_on:
#     print('Welcome to coffee mechine')
#     options = order_machine.get_items()
#     a = input(f'what do you want to order {options} \n')
#     if a == "report":
#         coffee_maker.report()
#         money_machine.report()
#     elif a == "off":
#         is_on = False
#     else:
#         drink = order_machine.find_drink(a)
#         print(drink)
#         check_ingredients =(coffee_maker.is_resource_sufficient(drink))
#         if check_ingredients == True:
#             payment = money_machine.make_payment((drink.cost))
#             make_coffee = coffee_maker.make_coffee(drink)

# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("after local assignment",spam)
#     do_nonlocal()
#     print("after nonlocal assignment",spam)
#     do_global()
#     print("after global assignment",spam)

# scope_test()
# print('in global scope:',spam)



# """class object"""

# class MyClass():
#     i = 12345123

#     def g(self):
#         return print('hello')


# x = MyClass()


# class complex:
#     def __init__(self,realpart,imagpart):
#         self.r = realpart
#         self.i = imagpart

# x = complex(3, 4)


# print(x.r)
# print(x.i)

# class dog:

#     kind = 'canine'

#     def __init__(self,name):
#         self.name = name
#         self.tricks = []

#     def add_trick(self,trick):
#         self.tricks.append(trick)

# d = dog('fido')
# e = dog('buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')


# print(d.kind)
# print(e.kind)
# print(e.name)
# print(d.tricks)


# class warehouse:
#     purpose = 'storage'
#     region = 'west'

# w1 = warehouse()
# print(w1.purpose,w1.region)
# w1.region = "north"
# print(w1.purpose,w1.region)


# def f1(self, x, y):
#     return min(x, x+y)

# class C:
#     f = f1

#     def g(self):
#         return 'hello world'

#     h = g

# class Bag:
#     def __init__(self):
#         self.data = []

#     def add(self, x):
#         self.data.append(x)

#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)

# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)

#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)

#     __update = update   # private copy of original update() method

# class MappingSubclass(Mapping):

#     def update(self, keys, values):
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)

# for element in [1, 2, 3]:
#     print(element)
# for element in (1, 2, 3):
#     print(element)
# for key in {'one':1, 'two':2}:
#     print(key)
# for char in "123":
#     print(char)
# for line in open("myfile.txt"):
#     print(line, end='')

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')
iter(rev)

for char in rev:
    print(char)