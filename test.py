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



#4.list & tuple
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

sum = 0
for i in list(range(101)):
    sum = sum + i
print(sum)

 
n = 5

while n > 0:
    sum = sum + n
    n = n - 1
    if n == 3:
        continue
    
print(sum)

