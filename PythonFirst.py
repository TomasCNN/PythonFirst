﻿import math
import msvcrt
import this
from copy import copy


a = 3
print(a)
b = 3.1412926
print(math.floor(b))

name = "ada lovelace"

print(name.title())        # title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。

print(name.upper())        # upper()将字符串改为全部大写

print(name.lower())        # lower()将字符串改为全部小写


favorite_language = ' python '

print(favorite_language.rstrip())         # rstrip()删除字符串末尾的空白

print(favorite_language.lstrip())         # lstrip()删除字符串开头的空白

print(favorite_language.strip())          # strip()删除字符串两端的空白

print(favorite_language.strip())          # strip()删除字符串两端的空白

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)


import this

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())

knames = ['ron', 'tyler', 'dani'] 
msg = f"Hello, {knames[0].title()}!"
print(msg) 
msg = f"Hello, {knames[1].title()}!" 
print(msg) 
msg = f"Hello, {knames[2].title()}!" 
print(msg)

#'''
#    f-string，亦称为格式化字符串常量（formatted string literals），
#    是python3.6新引入的一种字符串格式化方法，该方法源于pep 498 – 
#    literal string interpolation，主要目的是使格式化字符串的操作更
#    加简便。f-string在形式上是以 f 或 f 修饰符引领的字符串（f'xxx' 
#    或 f'xxx'），以大括号 {} 标明被替换的字段；f-string在本质上并
#    不是字符串常量，而是一个在运行时运算求值的表达式：
#    while other string literals always have a constant value, formatted 
#    strings are really expressions evaluated at run time.
#    （与具有恒定值的其它字符串常量不同，格式化字符串实际上是运行时运算求值的表达式。）
#        —— python documentation
#    f-string在功能方面不逊于传统的%-formatting语句和str.format()函数，
#    同时性能又优于二者，且使用起来也更加简洁明了，因此对于python3.6及
#    以后的版本，推荐使用f-string进行字符串格式化。


list = [10,20,30,40,50,60]
print(list)

list.append('Google')
print(list)


temp = ['Doc','Exe','Excel','Pro','Outlook']
list.extend(temp)
list.extend(['Doc','Exe','Excel','Pro','Outlook'])
print(list)

list[12:17] = []
print(list)

list[6:12] = []
print(list)

list.insert(0,5)
list.insert(2,15)
list.insert(4,25)
list.insert(6,35)
list.insert(8,45)
list.insert(10,55)
list.insert(12,65)
list1 = list
list2 = copy(list)

if list1 is list:
    print(list1 is list)
    print('list\'s Type is:',type(list))
    print('list\'s ID is:',id(list))
    print('list\'s Value is:',list)
    print('list1\'s Type is:',type(list1))
    print('list1\'s ID is:',id(list1))
    print('list1\'s Value is:',list1)

if list2 is not list:
    print(list2 is list)
    print('list\'s Type is:',type(list))
    print('list\'s ID is:',id(list))
    print('list\'s Value is:',list)
    print('list2\'s Type is:',type(list2))
    print('list2\'s ID is:',id(list2))
    print('list2\'s Value is:',list2)

print(list)

for i in range(0,7):
    if list[i] % 2 != 0:
        del list[i] 
print(list)

for j in range(0,7):
    if list2[j] % 2 == 0:
        del list2[j] 
print(list2)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#   如果你不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：如果你要从列表
#   中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续
#   使用它，就使用方法pop()。

#   有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法remove()。
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#   使用remove()从列表中删除元素时，也可接着使用它的值。下面删除值'ducati'，并打印一条消息，指出要将其从列表中删除的原因：
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#   注意：方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要
#   使用循环来判断是否删除了所有这样的值。


#   Python方法sort()让你能够较为轻松地对列表进行排序。假设你有一个汽车列表，并要让其
#   中的汽车按字母顺序排列。为简化这项任务，我们假设该列表中的所有值都是小写的。
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
#   方法sort()永久性地修改了列表元素的排列顺序。现在，汽车是按字母顺序排列的，再也无法恢复到原来的排列顺序。

#   还可以按与字母顺序相反的顺序排列列表元素，为此，只需向sort()方法传递参数reverse=True。
cars.sort(reverse=True)
print(cars)

