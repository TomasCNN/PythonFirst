import math
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

'''
    Python之禅
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

        Python程序员笃信代码可以编写得漂亮而优雅。编程是要解决问题的，设计良好、高效而漂
    亮的解决方案都会让程序员心生敬意。随着你对Python的认识越来越深入，并使用它来编写越来
    越多的代码，有一天也许会有人站在你后面惊呼：“哇，代码编写得真是漂亮！”
        如果有两个解决方案，一个简单，一个复杂，但都行之有效，就选择简单的解决方案吧。这
    样，你编写的代码将更容易维护，你或他人以后改进这些代码时也会更容易。
        现实是复杂的，有时候可能没有简单的解决方案。在这种情况下，就选择最简单可行的解决
    方案吧。
        即便是复杂的代码，也要让它易于理解。开发的项目涉及复杂代码时，一定要为这些代码编
    写有益的注释。
        如果让两名Python程序员去解决同一个问题，他们提供的解决方案应大致相同。这并不是说
    编程没有创意空间，而是恰恰相反！然而，大部分编程工作都是使用常见解决方案来解决简单的
    小问题，但这些小问题都包含在更庞大、更有创意空间的项目中。在你的程序中，各种具体细节
    对其他Python程序员来说都应易于理解。
        你可以将余生都用来学习Python和编程的纷繁难懂之处，但这样你什么项目都完不成。不要
    企图编写完美无缺的代码；先编写行之有效的代码，再决定是对其做进一步改进，还是转而去编
    写新代码。


'''


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

'''
    list操作
    append()
    insert()
    pop()
    del()
    remove()
'''


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

#   要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数sorted()。函数
#   sorted()让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。


cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#   注意，调用函数sorted()后，列表元素的排列顺序并没有变。如果你要按与字母顺序相反的顺序显示列表，也可向函数sorted()传递参数reverse = True。

#   在并非所有的值都是小写时，按字母顺序排列列表要复杂些。决定排列顺序时，有多种解读大写字母的方式，要指定准确的排列顺序，可能比我们这里所做的要复杂。

#   要反转列表元素的排列顺序，可使用方法reverse()。假设汽车列表是按购买时间排列的，可轻松地按相反的顺序排列其中的汽车：

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#   reverse()不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序：
#   方法reverse()永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用reverse()即可。

#   使用函数len()可快速获悉列表的长度。在下面的示例中，列表包含4个元素，因此其长度为4：

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
print('\t' + str(len(cars)))

#   在你需要完成如下任务时，len()很有用：确定还有多少个外星人未被射杀，需要管理多少项可视化数据，网站有多少注册用户等。
#   循环这种概念很重要，因为它是让计算机自动完成重复工作的常见方式之一。

#   在for循环中，可对每个元素执行任何操作。
#   使用for循环处理数据是一种对数据集执行整体操作的不错的方式。


#   能使用for循环来初始化游戏——遍历角色列表，将每个角色都显示到屏幕上；再在循环后面添加一个不缩进的代码块，在屏幕上绘制所有角色后显示一个Play Now按钮。
#   Python根据缩进来判断代码行与前一个代码行的关系。

#   需要存储一组数字的原因有很多，例如，在游戏中，需要跟踪每个角色的位置，还可能需要跟踪玩家的几个最高得分。
#   在数据可视化中，处理的几乎都是由数字（如温度、距离、人口数量、经度和纬度等）组成的集合。列表非常适合用于存储数字集合。

#   Python函数range()让你能够轻松地生成一系列的数字。
for value in range(1,5):
    print('\t' + str(value))

#   使用range()时，如果输出不符合预期，请尝试将指定的值加1或减1。

#   要创建数字列表，可使用函数list()将range()的结果直接转换为列表。

#   列表解析让你只需编写一行代码就能生成这样的列表。列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。

#   要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range()一样，Python在到达你指定的第二个索引前面的元素后停止。
#   要输出列表中的前三个元素，需要指定索引0~3，这将输出分别为0、1和2的元素。

#   在很多情况下，切片都很有用。例如，编写游戏时，你可以在玩家退出游戏时将其最终得分加入到一个列表中。然后，为获取该玩家的三个最高得分，
#   你可以将该列表按降序排列，再创建一个只包含前三个得分的切片。处理数据时，可使用切片来进行批量处理；编写Web应用程序时，可使用切片来分
#   页显示信息，并在每页显示数量合适的信息。

#   你经常需要根据既有列表创建全新的列表。下面来介绍复制列表的工作原理，以及复制列表可提供极大帮助的一种情形。
#   要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。
#   列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网站的用户列表或游戏中的角色列表至关重要。
#   然而，有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组。

#   元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
#   例如，如果有一个大小不应改变的矩形，可将其长度和宽度存储在一个元组中，从而确保它们是不能修改的：
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


#   虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组：
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#   相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组。

#   编程时经常需要检查一系列条件，并据此决定采取什么措施。在Python中，if语句让你能够检查程序的当前状态，并据此采取相应的措施。

#   每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试。Python根据条件测试的值为True还是False来决定是否
#   执行if语句中的代码。如果条件测试的值为True，Python就执行紧跟在if语句后面的代码；如果为False，Python就忽略这些代码。

#   大多数条件测试都将一个变量的当前值同特定值进行比较。最简单的条件测试检查变量的值是否与特定值相等：


#   检查是否相等时不考虑大小写

#   你可能想同时检查多个条件，例如，有时候你需要在两个条件都为True时才执行相应的操作，
#   而有时候你只要求一个条件为True时就执行相应的操作。在这些情况下，关键字and和or可助你一臂之力。
#   1. 使用and检查多个条件
#   要检查是否两个条件都为True，可使用关键字and将两个条件测试合而为一；如果每个测试都通过了，整个表达式就为True；如果至少有一个测试没有通过，整个表达式就为False。

#   为改善可读性，可将每个测试都分别放在一对括号内，但并非必须这样做。
#   2. 使用or检查多个条件
#   关键字or也能够让你检查多个条件，但只要至少有一个条件满足，就能通过整个测试。仅当两个测试都没有通过时，使用or的表达式才为False。


#   有时候，执行操作前必须检查列表是否包含特定的值。例如，结束用户的注册过程前，可能需要检查他提供的用户名是否已包含在用户名列表中。
#   在地图程序中，可能需要检查用户提交的位置是否包含在已知位置列表中。要判断特定的值是否已包含在列表中，可使用关键字in。
#   来看你可能为比萨店编写的一些代码；这些代码首先创建一个列表，其中包含用户点的比萨配料，然后检查特定的配料是否包含在该列表中。

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")


#   为让代码更简洁，可不在if-elif-else代码块中打印门票价格，而只在其中设置门票价格，并在它后面添加一条简单的print语句：

age = 120
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")



#   else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行，这可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，
#   应考虑使用一个elif代码块来代替else代码块。这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。


#   if-elif-else结构功能强大，但仅适合用于只有一个条件满足的情况：遇到通过了的测试后，Python就跳过余下的测试。这种行为很好，效率很高，
#   让你能够测试一个特定的条件。
#   然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含elif和else代码块的简单if语句。在可能有多个条件为True，
#   且你需要在每个条件为True时都采取相应措施时，适合使用这种方法。

#   总之，如果你只想执行一个代码块，就使用if-elif-else结构；如果要运行多个代码块，就使用一系列独立的if语句。

######################################################################################################################################################################################################
#   姓名：将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。

names = ['ZhanSan','LiSi','WangWu','HouLiu']

#   方法一：
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#   方法二：
for i in range(0,4):
    print(names[i])

######################################################################################################################################################################################################




######################################################################################################################################################################################################
#   问候语：继续使用练习3-1 中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。

names = ['ZhanSan','LiSi','WangWu','HouLiu']

#   方法一：
print('Goodmorning!Dear' + str(names[0]) + '!')
print('Goodmorning!Dear' + str(names[1]) + '!')
print('Goodmorning!Dear' + str(names[2]) + '!')
print('Goodmorning!Dear' + str(names[3]) + '!')

#   方法二：
for i in range(0,4):
    print('Goodmorning!Dear' + str(names[i]) + '!')

######################################################################################################################################################################################################




######################################################################################################################################################################################################
#   自己的列表：想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“I would liketo own a Honda motorcycle”。

Commuting_modes = ['Bus', 'Subway', 'Car', 'Bycicle']

#   方法一：
print('I would liketo own a ' + str(Commuting_modes[0]) + '!')
print('I would liketo own a ' + str(Commuting_modes[1]) + '!')
print('I would liketo own a ' + str(Commuting_modes[2]) + '!')
print('I would liketo own a ' + str(Commuting_modes[3]) + '!')

#   方法二：
for i in range(0,4):
    print('I would liketo own a ' + str(Commuting_modes[i]) + '!')

######################################################################################################################################################################################################




######################################################################################################################################################################################################
#   嘉宾名单：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少3 个你想邀请的人；然后，使用这个列表打印消息，邀请这些人来与你共进晚餐。

Guest = ['ZhanSan','LiSi','WangWu','HouLiu']

#   方法一：
print('Dear ' + str(Guest[0]) + ', would you like to eat dinner with me tonight!')
print('Dear ' + str(Guest[1]) + ', would you like to eat dinner with me tonight!')
print('Dear ' + str(Guest[2]) + ', would you like to eat dinner with me tonight!')
print('Dear ' + str(Guest[3]) + ', would you like to eat dinner with me tonight!')

#   方法二：
for i in range(0,4):
    print('Dear ' + str(Guest[i]) + ', would you like to eat dinner with me tonight!')

######################################################################################################################################################################################################




######################################################################################################################################################################################################
#   修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。以完成练习上题时编写的程序为基础，
#   在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
#   修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
#   再次打印一系列消息，向名单中的每位嘉宾发出邀请。

Guest = ['ZhanSan','LiSi','WangWu','HouLiu']
Lost_G = 'WangWu'

#   删除一位贵宾
#   方法一：
Guest.pop(2)
print(Guest)
Guest.insert(2,'WangWu')  # 插入一位贵宾
print(Guest)


#   方法二：
del(Guest[2])
print(Guest)


#   在列表末尾添加一位贵宾
Guest.append('WuQi')

print('I\'m sorry to hear that ' + Lost_G + '\'s grandpa is died , so he can\'t jion us to eat dinner tonight!')


#   方法一：
print('Dear ' + str(Guest[0]) + ', would you like to eat dinner with me tonight!')
print('Dear ' + str(Guest[1]) + ', would you like to eat dinner with me tonight!')
print('Dear ' + str(Guest[2]) + ', would you like to eat dinner with me tonight!')
print('Dear ' + str(Guest[3]) + ', would you like to eat dinner with me tonight!')

#   方法二：
for i in range(0,4):
    print('Dear ' + str(Guest[i]) + ', would you like to eat dinner with me tonight!')

######################################################################################################################################################################################################



#   在Python中，字典是一系列键—值对。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。
#   与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。
#   键—值对是两个相关联的值。指定键时，Python将返回与之相关联的值。键和值之间用冒号分隔，
#   而键—值对之间用逗号分隔。在字典中，你想存储多少个键—值对都可以。

#   要获取与键相关联的值，可依次指定字典名和放在方括号内的键，如下所示：
alien_0 = {'color': 'green'}
print(alien_0['color'])


#   字典是一种动态结构，可随时在其中添加键—值对。要添加键—值对，可依次指定字典名、用方括号括起的键和相关联的值。
#   使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时，通常都需要先定义一个空字典。

#   要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3
    # 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#   通过修改外星人字典中的值，可改变外星人的行为。















