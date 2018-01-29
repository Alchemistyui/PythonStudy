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







