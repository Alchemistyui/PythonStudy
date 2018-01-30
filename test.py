#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#1.输入输出流
# name = input('enter your name')
# print('hello', name)

# print('\\\t\\')
# print(r'\\\t\\')

# print(' line1 \n line2 \n line3')
# print('''line1
#     line2
#     line3''')

# #2.数据类型和变量
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''

# for i in n,f,s1,s2,s3,s4:
#     print(i)

#3.字符串和编码
# print('包含中文的str')
# print(ord('中'))
# print('chr(66)',chr(66))
# print(r"'\u4e2d\u6587'",'\u4e2d\u6587')

# print(r"'ABC'.encode('ascii') : ",'ABC'.encode('ascii'))
# print(r"'中文'.encode('utf-8') : ",'中文'.encode('utf-8'))

# print(b'ABC'.decode('utf-8'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# print ('%06.2f'%8123.1)

# print('hello, %s, 233' % ('Alchemist'))
# print('hello %s, your grade: %d%%' % ('Alchemist', 90))



#4.list & tuple元组，不可更改
# classmate = ['yujie','dabiao','yuge']
# for i in [0,1,2]:
#     print(classmate[i])

# print(classmate[-1])

# classmate.append('ergou')

# print(classmate)

# classmate.pop(2)
# print(classmate)

# s = ['python', 'java', ['asp', 'php'], 'scheme']
# print(len(s))
# print(s[2][1])


# t1 = (1, 2)
# print(t1[1])

# t2 = (1,)
# print(t2)

#5.条件判断
# a = input('age : ')
# age = int(a)
# if age >= 40:
#     print('old')
# elif age >= 20:
#     print('young')
# elif age >= 18:
#     print('adult')
# else :
#     print('kid')

#6.循环
# sum = 0
# for i in list(range(101)):
#     sum = sum + i
# print(sum)


# n = 5

# while n > 0:
#     sum = sum + n
#     n = n - 1
#     if n == 3:
#         continue

# print(sum)

# #7.dict & set
# score = {'math': 90, 'chinese': 95}
# score['english'] = 85

# print(score)
# print('math' in score)
# print(score.get('emm'))

# score.pop('english')
# #dict的key必须是不可变对象,
# #在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key


# #set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# s = set([1,2,2,3,1,4])
# print(s)
# s.add(5)
# s.remove(4)
# #set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
# s2 = set([2, 3, 4])
# print(s & s2)
# print(s | s2)


#8.函数
# def my_abs(x):
#     if not isinstance(x, (int,float)): 
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(my_abs(-233))

# def null_fun():
#     pass

# def nextTwo(x=1):
#     if not isinstance(x, int):
#         raise TabError('bad operand type')
#     return x+1, x+2
# #默认参数必须指向不变对象！
# x,y = nextTwo()
# print(x,y)

# def summit(*number):
#     sum = 0
#     for i in number:
#         sum = sum + i 
#     return sum

# nums = [1,2,3,4,5,6,7,8,9,10]
# print(summit(*nums))

# def person(name,**other):
#     print(name, 'other:', other)

# person('yun')
# person('dabiao',city='Beijing')
# d = {'age': 18, 'city': "chendu"}
# person('alchemist',**d)

# #命名关键字参数可以有缺省值
# def person2(name, age, *, city, job):
#     print(name, age, city, job)
# person2('Jack', 24, city='Beijing', job='Engineer')
# #参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数


#9. 切片:list,tuple,字符串
# l = list(range(100))
# print(l[0:10])



#10.迭代:list,tuple,字符串,dict
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)

# for value in d.values():
#     print(value)
# for k,v in d.items():
#     print(k,':',v)

# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)

#11.列表生成式
# print([x * x for x in range(1,11) if x % 2 == 0])
# print([x + y for x in 'abc' for y in 'xyz'])
# import os
# print([d for d in os.listdir('.')])

#12.生成器
# g = (x * x for x in range(10))
# print(g)
# for i in g:
#     print(i)

# def fib(max):
#     n,a,b = 0,0,1
#     while(n<max):
#         yield(b)
#         a,b = b,a+b
#         n = n + 1
#     return 'done'

# f = fib(6)
# for i in f:
#     print(i)


# def triangles():
#     Y=[1]    
#     while True:
#         yield Y
#         Y=[1]+[Y[i]+Y[i+1] for i in range(len(Y)-1)]+[1]
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break

#13.迭代器
# it = iter([1, 2, 3, 4, 5])

#14.高阶函数

def is_palindrome(n):
    s=str(n)
    t=s[::-1]
    return s==t
      
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)


#15.类
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def printMsg(self):
        print(self.__name,' : ', self.__score)
    def get_name(self):
        return self.__name
    def set_score(self, score):
        self.__score = score


stu = Student('bigBiao', 95)
stu.printMsg()




