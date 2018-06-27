'''
import os
# List comprahensions
my_nums = [1,2,3,4,5,6,7,8,9,10]


my_list1 = []

for n in nums:
    if n%2 == 0:
        my_list1.append(n)
print(my_list1)

    my_list2 = [n for n in nums]
    print(my_list2)
    
    my_list3 = [n*n for n in nums]
    print(my_list3)

my_list4 = map(lambda n: n*n, nums)
print(my_list4)

my_list5 = [n for n in nums if n%2 == 0]
print(my_list5)

my_list6 = filter(lambda n: n%2 == 0, nums)
print(my_list6)'''


my_list7 = [(letter, num) for letter in 'ABCD' for num in range(4)]
print(my_list7)



names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_super_dict = {}
for name, hero in zip(names,heroes):
    my_super_dict[name] = hero
print(my_super_dict)

my_super_dict1 = {name: hero for name, hero in zip(names, heroes)}
print(my_super_dict1)


'''
def gen_function (nums):
    for n in nums:
        yield n*n

my_gen = (n*n for n in my_nums)

# Generators
# Control flow
user = 'Admin'
logged_in = False

if user == 'Admin' or not logged_in:
    print('Logged In')
else:
    print('Offline')

a = [1,2,3]
b = [1,2,3]
c = a

print(a is b)
print(id(a))
print(id(b))
print(id(c))
print(a is c)


def square_numbers(nums):
    for i in nums:
        yield i*i

square_list = (num*num for num in my_nums)

lst = list(square_list)

for item in lst:
    print(int(item))


class Employee():

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{} {}email.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


# Fibonacci sequence
def fib(n):
   if n == 1:
      return 1
   elif n == 0:
      return 0
   else:
      return fib(n-1) + fib(n-2)


def fib_sequence(length):
    fib_list = (fib(n) for n in range(length))
    try:
        while fib_list:
            print(next(fib_list))
    except StopIteration:
        print("List ended")


fib_sequence(10)



class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class Child(Parent):
    def get_value(self):
        return self.value + 1


print(Parent.__dict__)
print(Child.__dict__)

chl = Child()
prn = Parent()

print(chl.get_value)
print(prn.get_value)

'''

numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting itertor to list
resultList = list(result)
print(resultList)

# Two iterables are passed
result = zip(numberList, strList)

# Converting itertor to set
resultSet = set(result)
print(resultSet)

