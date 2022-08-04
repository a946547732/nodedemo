# import keyword
# import a2

# print(keyword.kwlist)

# if True:
#     print('true')
# else:
#     print('false')
# print(123)

# print('''qqq
# 222
# ''')

# str = '1234567890'

# data = input('请输入：')

# print(data)

# import sys
# sys.stdout.write(' h1 ')

# print(1,2)

# import sys
# for i in sys.argv:
#     print('i', i)
# print('path', sys.path)

# from sys import argv, path
# print(argv, path)

# a = b = 2
# print(a, b) #2 2

# a, b = 1, 2
# print(a, b) #1 2

# a = 111
# print(isinstance(a, int)) #True 检查类型

class A: {}
class B(A): {}

print(isinstance(A(), A), isinstance(B(), A)) # True True B类继承于A类

# bool是int的子类 True == 1 False == 0
print(issubclass(bool, int)) #True
print(True == 1, False == 0) #True True
# print(1 is True, 0 is False) #False False

#删除变量 del
