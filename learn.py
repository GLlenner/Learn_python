# from math import sqrt
#print("1024 * 768 =" ,1024 *768)

# print('%2d-%012d' % (3, 1))
# print('%.2f' % 3.1415926)

# s1 = 72
# s2 = 85
# r = (s2 - s1) / s1 * 100
# print(f'小明的学习成绩上升了{r:.2f}%')

# set = {[1,2,3,4],[1,2,3,4,5]}
# print(set)

# n1 = 255
# n2 = 1000
# print(hex(25))


# def quadratic(a, b, c):
#     x1 = (-b + sqrt(b*b - 4*a*c)) / 2
#     x2 = (-b - sqrt(b*b - 4*a*c)) / 2
#     return x1,x2

# print(quadratic(1,-3,2))


# def person(name, age, *, city, job):
#     print(name, age, city, job)
# p1 = person('GL',20)
# print(p1)

# def f1(a, b, c=0, *args, **kw):
#     # print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# def mul(*nums):
#     result = 1
#     for num in nums:
#         result = result * num
#     return result

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# print(fact(500))

# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#         return None
#     move(n-1,a,c,b)
#     move(1,a,b,c)
#     move(n-1,b,a,c)
#     return None
# move(15,'A','B','C')

# def trim(s):
#     start = 0
#     end = len(s) - 1
#     while s[start] == ' ':
#         start += 1
#     while s[end] == ' ':
#         end -= 1
#     s = s[start:end]
#     print(s)
#     return s

# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')


# s = 'hello world'
# start = 0
# end = len(s)
# s = s[start:end]
# print(s)

# dict = {'a': 1, 'b': 2, 'c': 3}
# for key,value in dict.items():
# 	print(f'key = {key},value = {value}')

# def findMinAndMax(L):
#     if not L:
#         return (None,None)
#     max = L[0]
#     min = L[0]
#     for num in L:
#         if num > max:
#             max = num
#         if num < min:
#             min = num
#     return (min, max)
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

# import os
# print([d for d in os.listdir('.')])

# L = ['Hello', 'World', 18, 'Apple', None]
# L2 = [x.lower() for x in L if isinstance(x,str)]

# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')

# def triangles():
#     row = [1]
#     while True:
#         yield row
#         newrow = [1]
#         for i in range(len(row) - 1):
#             newrow.append(row[i] + row[i+1])
#         newrow.append(1)
#         row = newrow

# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break

# for t in results:
#     print(t)

# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')  

# it = [1, 2, 3, 4, 5]
# # 循环:
# while True:
#     try:
#         # 获得下一个值:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break

# name  = 'asdjslkdlkakjdsjkasdjkkl'
# name.replace(name[0],name[0].upper())
# print(name)

# def normalize(name):
#     name = name.lower()
#     name = name[0].upper() + name[1:]
#     return name

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize,L1))
# print(L2)


# from functools import reduce
# def mul(x,y):
#     return x*y
# def prod(L):
#     return reduce(mul,L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')


# from functools import reduce

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}

# def char2num(s):
#     return DIGITS[s]

# def list2float(List):
#     result = 0
#     count = 0
#     big1 = True
#     for num in List:
#         if num == '.':
#             big1 = False
#         elif big1:
#             result = result * 10 + num
#         else:
#             result = result * 10 + num
#             count += 1
#     return result / pow(10,count)

# def str2float(s):
#     L = list(map(char2num,s))
#     result = list2float(L)
#     return result


# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# L = '123.123'
# print(L[-1:L.find('.'):-1])


# s = 'asd'
# s2 = 'sdf'
# print(s and s2)

# def is_palindrome(n):
#     L = []
#     while n!=0:
#         L.append(n%10)
#         n = n // 10
#         # print(n)
#     start = 0
#     end = len(L) - 1
#     while start < end:
#         if L[start] != L[end]:
#             return False
#         start += 1
#         end -= 1
#     return True
# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def by_name(t):
#     return t[0]

# L2 = sorted(L, key=by_name)
# print(L2)




# def createCounter():
#     i = 1
#     def counter():
#         i = i+1
#         return i
#     return counter

# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# L = list(filter(lambda x : x % 2 == 0,range(1,100)))
# print(L)

# import time, functools

# def decorator(fnc):
#     def wrapper(*args,**kw):
#         start_time = time.time()
#         result = fnc(*args,**kw)
#         end_time  = time.time()
#         print(f'process running use {start_time - end_time} second')
#         return fnc(*args,**kw)
#     return wrapper


# # 测试
# @decorator
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y

# @decorator
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

# import sys 
# print(sys.path)

# class Student(object):
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender

#     def get_name(self):
#         return self.__name
#     def get_gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         self.__gender = gender
    

# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# class Screen(object):
#     def __init__(self):
#         self._width = 0
#         self._height = 0
    
#     @property
#     def width(self):
#         return self._width
    
#     @width.setter
#     def width(self,value):
#         if value < 0 :
#             raise ValueError("width must be greater than 0")
#         self._width = value

#     @property
#     def height(self):
#         return self._height
    
#     @height.setter
#     def height(self,value):
#         if value < 0 :
#             raise ValueError("width must be greater than 0")
#         self._height = value

#     @property
#     def resolution(self):
#         return self._width * self._height

# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')

# from enum import Enum

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

# from functools import reduce

# def str2num(s):
#     return int(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# main()

def fact(n):
    '''
    Calculate 1*2*...*n
    
    >>> fact(1)
    1
    >>> fact(10)
    ?
    >>> fact(-1)
    ?
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()










































