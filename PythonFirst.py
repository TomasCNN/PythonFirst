import math
import msvcrt
import this
from copy import copy

######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################

#a = 3
#print(a)
#b = 3.1412926
#print(math.floor(b))

#name = "ada lovelace"

#print(name.title())        # title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。

#print(name.upper())        # upper()将字符串改为全部大写

#print(name.lower())        # lower()将字符串改为全部小写


#favorite_language = ' python '

#print(favorite_language.rstrip())         # rstrip()删除字符串末尾的空白

#print(favorite_language.lstrip())         # lstrip()删除字符串开头的空白

#print(favorite_language.strip())          # strip()删除字符串两端的空白

#print(favorite_language.strip())          # strip()删除字符串两端的空白

#age = 23
#message = "happy " + str(age) + "rd birthday!"
#print(message)


#import this

#bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles[0])
#print(bicycles[0].title())

#knames = ['ron', 'tyler', 'dani'] 
#msg = f"hello, {knames[0].title()}!"
#print(msg) 
#msg = f"hello, {knames[1].title()}!" 
#print(msg) 
#msg = f"hello, {knames[2].title()}!" 
#print(msg)

#'''
#    python之禅
#    the zen of python, by tim peters

#    beautiful is better than ugly.
#    explicit is better than implicit.
#    simple is better than complex.
#    complex is better than complicated.
#    flat is better than nested.
#    sparse is better than dense.
#    readability counts.
#    special cases aren't special enough to break the rules.
#    although practicality beats purity.
#    errors should never pass silently.
#    unless explicitly silenced.
#    in the face of ambiguity, refuse the temptation to guess.
#    there should be one-- and preferably only one --obvious way to do it.
#    although that way may not be obvious at first unless you're dutch.
#    now is better than never.
#    although never is often better than *right* now.
#    if the implementation is hard to explain, it's a bad idea.
#    if the implementation is easy to explain, it may be a good idea.
#    namespaces are one honking great idea -- let's do more of those!

#        python程序员笃信代码可以编写得漂亮而优雅。编程是要解决问题的，设计良好、高效而漂
#    亮的解决方案都会让程序员心生敬意。随着你对python的认识越来越深入，并使用它来编写越来
#    越多的代码，有一天也许会有人站在你后面惊呼：“哇，代码编写得真是漂亮！”
#        如果有两个解决方案，一个简单，一个复杂，但都行之有效，就选择简单的解决方案吧。这
#    样，你编写的代码将更容易维护，你或他人以后改进这些代码时也会更容易。
#        现实是复杂的，有时候可能没有简单的解决方案。在这种情况下，就选择最简单可行的解决
#    方案吧。
#        即便是复杂的代码，也要让它易于理解。开发的项目涉及复杂代码时，一定要为这些代码编
#    写有益的注释。
#        如果让两名python程序员去解决同一个问题，他们提供的解决方案应大致相同。这并不是说
#    编程没有创意空间，而是恰恰相反！然而，大部分编程工作都是使用常见解决方案来解决简单的
#    小问题，但这些小问题都包含在更庞大、更有创意空间的项目中。在你的程序中，各种具体细节
#    对其他python程序员来说都应易于理解。
#        你可以将余生都用来学习python和编程的纷繁难懂之处，但这样你什么项目都完不成。不要
#    企图编写完美无缺的代码；先编写行之有效的代码，再决定是对其做进一步改进，还是转而去编
#    写新代码。


#'''


##'''
##    f-string，亦称为格式化字符串常量（formatted string literals），
##    是python3.6新引入的一种字符串格式化方法，该方法源于pep 498 – 
##    literal string interpolation，主要目的是使格式化字符串的操作更
##    加简便。f-string在形式上是以 f 或 f 修饰符引领的字符串（f'xxx' 
##    或 f'xxx'），以大括号 {} 标明被替换的字段；f-string在本质上并
##    不是字符串常量，而是一个在运行时运算求值的表达式：
##    while other string literals always have a constant value, formatted 
##    strings are really expressions evaluated at run time.
##    （与具有恒定值的其它字符串常量不同，格式化字符串实际上是运行时运算求值的表达式。）
##        —— python documentation
##    f-string在功能方面不逊于传统的%-formatting语句和str.format()函数，
##    同时性能又优于二者，且使用起来也更加简洁明了，因此对于python3.6及
##    以后的版本，推荐使用f-string进行字符串格式化。

#'''
#    list操作
#    append()
#    insert()
#    pop()
#    del()
#    remove()
#'''


#list = [10,20,30,40,50,60]
#print(list)

#list.append('google')
#print(list)


#temp = ['doc','exe','excel','pro','outlook']
#list.extend(temp)
#list.extend(['doc','exe','excel','pro','outlook'])
#print(list)

#list[12:17] = []
#print(list)

#list[6:12] = []
#print(list)

#list.insert(0,5)
#list.insert(2,15)
#list.insert(4,25)
#list.insert(6,35)
#list.insert(8,45)
#list.insert(10,55)
#list.insert(12,65)
#list1 = list
#list2 = copy(list)

#if list1 is list:
#    print(list1 is list)
#    print('list\'s type is:',type(list))
#    print('list\'s id is:',id(list))
#    print('list\'s value is:',list)
#    print('list1\'s type is:',type(list1))
#    print('list1\'s id is:',id(list1))
#    print('list1\'s value is:',list1)

#if list2 is not list:
#    print(list2 is list)
#    print('list\'s type is:',type(list))
#    print('list\'s id is:',id(list))
#    print('list\'s value is:',list)
#    print('list2\'s type is:',type(list2))
#    print('list2\'s id is:',id(list2))
#    print('list2\'s value is:',list2)

#print(list)

#for i in range(0,7):
#    if list[i] % 2 != 0:
#        del list[i] 
#print(list)

#for j in range(0,7):
#    if list2[j] % 2 == 0:
#        del list2[j] 
#print(list2)

#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)
#popped_motorcycle = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycle)

##   如果你不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：如果你要从列表
##   中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续
##   使用它，就使用方法pop()。

##   有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法remove()。
#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)
#motorcycles.remove('ducati')
#print(motorcycles)

##   使用remove()从列表中删除元素时，也可接着使用它的值。下面删除值'ducati'，并打印一条消息，指出要将其从列表中删除的原因：
#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)
#too_expensive = 'ducati'
#motorcycles.remove(too_expensive)
#print(motorcycles)
#print("\na " + too_expensive.title() + " is too expensive for me.")

##   注意：方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要
##   使用循环来判断是否删除了所有这样的值。


##   python方法sort()让你能够较为轻松地对列表进行排序。假设你有一个汽车列表，并要让其
##   中的汽车按字母顺序排列。为简化这项任务，我们假设该列表中的所有值都是小写的。
#cars = ['bmw', 'audi', 'toyota', 'subaru']
#print(cars)
#cars.sort()
#print(cars)
##   方法sort()永久性地修改了列表元素的排列顺序。现在，汽车是按字母顺序排列的，再也无法恢复到原来的排列顺序。

##   还可以按与字母顺序相反的顺序排列列表元素，为此，只需向sort()方法传递参数reverse=true。
#cars.sort(reverse=true)
#print(cars)

##   要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数sorted()。函数
##   sorted()让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。


#cars = ['bmw', 'audi', 'toyota', 'subaru']

#print("here is the original list:")
#print(cars)

#print("\nhere is the sorted list:")
#print(sorted(cars))

#print("\nhere is the original list again:")
#print(cars)

##   注意，调用函数sorted()后，列表元素的排列顺序并没有变。如果你要按与字母顺序相反的顺序显示列表，也可向函数sorted()传递参数reverse = true。

##   在并非所有的值都是小写时，按字母顺序排列列表要复杂些。决定排列顺序时，有多种解读大写字母的方式，要指定准确的排列顺序，可能比我们这里所做的要复杂。

##   要反转列表元素的排列顺序，可使用方法reverse()。假设汽车列表是按购买时间排列的，可轻松地按相反的顺序排列其中的汽车：

#cars = ['bmw', 'audi', 'toyota', 'subaru']
#print(cars)
#cars.reverse()
#print(cars)

##   reverse()不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序：
##   方法reverse()永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用reverse()即可。

##   使用函数len()可快速获悉列表的长度。在下面的示例中，列表包含4个元素，因此其长度为4：

#cars = ['bmw', 'audi', 'toyota', 'subaru']
#print(len(cars))
#print('\t' + str(len(cars)))

##   在你需要完成如下任务时，len()很有用：确定还有多少个外星人未被射杀，需要管理多少项可视化数据，网站有多少注册用户等。
##   循环这种概念很重要，因为它是让计算机自动完成重复工作的常见方式之一。

##   在for循环中，可对每个元素执行任何操作。
##   使用for循环处理数据是一种对数据集执行整体操作的不错的方式。


##   能使用for循环来初始化游戏——遍历角色列表，将每个角色都显示到屏幕上；再在循环后面添加一个不缩进的代码块，在屏幕上绘制所有角色后显示一个play now按钮。
##   python根据缩进来判断代码行与前一个代码行的关系。

##   需要存储一组数字的原因有很多，例如，在游戏中，需要跟踪每个角色的位置，还可能需要跟踪玩家的几个最高得分。
##   在数据可视化中，处理的几乎都是由数字（如温度、距离、人口数量、经度和纬度等）组成的集合。列表非常适合用于存储数字集合。

##   python函数range()让你能够轻松地生成一系列的数字。
#for value in range(1,5):
#    print('\t' + str(value))

##   使用range()时，如果输出不符合预期，请尝试将指定的值加1或减1。

##   要创建数字列表，可使用函数list()将range()的结果直接转换为列表。

##   列表解析让你只需编写一行代码就能生成这样的列表。列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。

##   要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range()一样，python在到达你指定的第二个索引前面的元素后停止。
##   要输出列表中的前三个元素，需要指定索引0~3，这将输出分别为0、1和2的元素。

##   在很多情况下，切片都很有用。例如，编写游戏时，你可以在玩家退出游戏时将其最终得分加入到一个列表中。然后，为获取该玩家的三个最高得分，
##   你可以将该列表按降序排列，再创建一个只包含前三个得分的切片。处理数据时，可使用切片来进行批量处理；编写web应用程序时，可使用切片来分
##   页显示信息，并在每页显示数量合适的信息。

##   你经常需要根据既有列表创建全新的列表。下面来介绍复制列表的工作原理，以及复制列表可提供极大帮助的一种情形。
##   要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。这让python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。
##   列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网站的用户列表或游戏中的角色列表至关重要。
##   然而，有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。python将不能修改的值称为不可变的，而不可变的列表被称为元组。

##   元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
##   例如，如果有一个大小不应改变的矩形，可将其长度和宽度存储在一个元组中，从而确保它们是不能修改的：
#dimensions = (200, 50)
#print(dimensions[0])
#print(dimensions[1])


##   虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组：
#dimensions = (200, 50)
#print("original dimensions:")
#for dimension in dimensions:
#    print(dimension)

#dimensions = (400, 100)
#print("\nmodified dimensions:")
#for dimension in dimensions:
#    print(dimension)

##   相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组。

##   编程时经常需要检查一系列条件，并据此决定采取什么措施。在python中，if语句让你能够检查程序的当前状态，并据此采取相应的措施。

##   每条if语句的核心都是一个值为true或false的表达式，这种表达式被称为条件测试。python根据条件测试的值为true还是false来决定是否
##   执行if语句中的代码。如果条件测试的值为true，python就执行紧跟在if语句后面的代码；如果为false，python就忽略这些代码。

##   大多数条件测试都将一个变量的当前值同特定值进行比较。最简单的条件测试检查变量的值是否与特定值相等：


##   检查是否相等时不考虑大小写

##   你可能想同时检查多个条件，例如，有时候你需要在两个条件都为true时才执行相应的操作，
##   而有时候你只要求一个条件为true时就执行相应的操作。在这些情况下，关键字and和or可助你一臂之力。
##   1. 使用and检查多个条件
##   要检查是否两个条件都为true，可使用关键字and将两个条件测试合而为一；如果每个测试都通过了，整个表达式就为true；如果至少有一个测试没有通过，整个表达式就为false。

##   为改善可读性，可将每个测试都分别放在一对括号内，但并非必须这样做。
##   2. 使用or检查多个条件
##   关键字or也能够让你检查多个条件，但只要至少有一个条件满足，就能通过整个测试。仅当两个测试都没有通过时，使用or的表达式才为false。


##   有时候，执行操作前必须检查列表是否包含特定的值。例如，结束用户的注册过程前，可能需要检查他提供的用户名是否已包含在用户名列表中。
##   在地图程序中，可能需要检查用户提交的位置是否包含在已知位置列表中。要判断特定的值是否已包含在列表中，可使用关键字in。
##   来看你可能为比萨店编写的一些代码；这些代码首先创建一个列表，其中包含用户点的比萨配料，然后检查特定的配料是否包含在该列表中。

#age = 17
#if age >= 18:
#    print("you are old enough to vote!")
#    print("have you registered to vote yet?")
#else:
#    print("sorry, you are too young to vote.")
#    print("please register to vote as soon as you turn 18!")


#age = 12
#if age < 4:
#    print("your admission cost is $0.")
#elif age < 18:
#    print("your admission cost is $5.")
#else:
#    print("your admission cost is $10.")


##   为让代码更简洁，可不在if-elif-else代码块中打印门票价格，而只在其中设置门票价格，并在它后面添加一条简单的print语句：

#age = 120
#if age < 4:
#    price = 0
#elif age < 18:
#    price = 5
#else:
#    price = 10

#print("your admission cost is $" + str(price) + ".")



##   else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行，这可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，
##   应考虑使用一个elif代码块来代替else代码块。这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。


##   if-elif-else结构功能强大，但仅适合用于只有一个条件满足的情况：遇到通过了的测试后，python就跳过余下的测试。这种行为很好，效率很高，
##   让你能够测试一个特定的条件。
##   然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含elif和else代码块的简单if语句。在可能有多个条件为true，
##   且你需要在每个条件为true时都采取相应措施时，适合使用这种方法。

##   总之，如果你只想执行一个代码块，就使用if-elif-else结构；如果要运行多个代码块，就使用一系列独立的if语句。

#######################################################################################################################################################################################################
##   姓名：将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。

#names = ['zhansan','lisi','wangwu','houliu']

##   方法一：
#print(names[0])
#print(names[1])
#print(names[2])
#print(names[3])

##   方法二：
#for i in range(0,4):
#    print(names[i])

#######################################################################################################################################################################################################




#######################################################################################################################################################################################################
##   问候语：继续使用练习3-1 中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。

#names = ['zhansan','lisi','wangwu','houliu']

##   方法一：
#print('goodmorning!dear' + str(names[0]) + '!')
#print('goodmorning!dear' + str(names[1]) + '!')
#print('goodmorning!dear' + str(names[2]) + '!')
#print('goodmorning!dear' + str(names[3]) + '!')

##   方法二：
#for i in range(0,4):
#    print('goodmorning!dear' + str(names[i]) + '!')

#######################################################################################################################################################################################################




#######################################################################################################################################################################################################
##   自己的列表：想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“i would liketo own a honda motorcycle”。

#commuting_modes = ['bus', 'subway', 'car', 'bycicle']

##   方法一：
#print('i would liketo own a ' + str(commuting_modes[0]) + '!')
#print('i would liketo own a ' + str(commuting_modes[1]) + '!')
#print('i would liketo own a ' + str(commuting_modes[2]) + '!')
#print('i would liketo own a ' + str(commuting_modes[3]) + '!')

##   方法二：
#for i in range(0,4):
#    print('i would liketo own a ' + str(commuting_modes[i]) + '!')

#######################################################################################################################################################################################################




#######################################################################################################################################################################################################
##   嘉宾名单：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少3 个你想邀请的人；然后，使用这个列表打印消息，邀请这些人来与你共进晚餐。

#guest = ['zhansan','lisi','wangwu','houliu']

##   方法一：
#print('dear ' + str(guest[0]) + ', would you like to eat dinner with me tonight!')
#print('dear ' + str(guest[1]) + ', would you like to eat dinner with me tonight!')
#print('dear ' + str(guest[2]) + ', would you like to eat dinner with me tonight!')
#print('dear ' + str(guest[3]) + ', would you like to eat dinner with me tonight!')

##   方法二：
#for i in range(0,4):
#    print('dear ' + str(guest[i]) + ', would you like to eat dinner with me tonight!')

#######################################################################################################################################################################################################




#######################################################################################################################################################################################################
##   修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。以完成练习上题时编写的程序为基础，
##   在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
##   修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
##   再次打印一系列消息，向名单中的每位嘉宾发出邀请。

#guest = ['zhansan','lisi','wangwu','houliu']
#lost_g = 'wangwu'

##   删除一位贵宾
##   方法一：
#guest.pop(2)
#print(guest)
#guest.insert(2,'wangwu')  # 插入一位贵宾
#print(guest)


##   方法二：
#del(guest[2])
#print(guest)


##   在列表末尾添加一位贵宾
#guest.append('wuqi')

#print('i\'m sorry to hear that ' + lost_g + '\'s grandpa is died , so he can\'t jion us to eat dinner tonight!')


##   方法一：
#print('dear ' + str(guest[0]) + ', would you like to eat dinner with me tonight!')
#print('dear ' + str(guest[1]) + ', would you like to eat dinner with me tonight!')
#print('dear ' + str(guest[2]) + ', would you like to eat dinner with me tonight!')
#print('dear ' + str(guest[3]) + ', would you like to eat dinner with me tonight!')

##   方法二：
#for i in range(0,4):
#    print('dear ' + str(guest[i]) + ', would you like to eat dinner with me tonight!')

#######################################################################################################################################################################################################



##   在python中，字典是一系列键—值对。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。
##   与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何python对象用作字典中的值。
##   键—值对是两个相关联的值。指定键时，python将返回与之相关联的值。键和值之间用冒号分隔，
##   而键—值对之间用逗号分隔。在字典中，你想存储多少个键—值对都可以。

##   要获取与键相关联的值，可依次指定字典名和放在方括号内的键，如下所示：
#alien_0 = {'color': 'green'}
#print(alien_0['color'])


##   字典是一种动态结构，可随时在其中添加键—值对。要添加键—值对，可依次指定字典名、用方括号括起的键和相关联的值。
##   使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时，通常都需要先定义一个空字典。

##   要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。


#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print("original x-position: " + str(alien_0['x_position']))

## 向右移动外星人
## 据外星人当前速度决定将其移动多远

#if alien_0['speed'] == 'slow':
#    x_increment = 1
#elif alien_0['speed'] == 'medium':
#    x_increment = 2
#else:
#    # 这个外星人的速度一定很快
#    x_increment = 3
#    # 新位置等于老位置加上增量
#alien_0['x_position'] = alien_0['x_position'] + x_increment
#print("new x-position: " + str(alien_0['x_position']))

##   通过修改外星人字典中的值，可改变外星人的行为。


##   对于字典中不再需要的信息，可使用del语句将相应的键—值对彻底删除。使用del语句时，必须指定字典名和要删除的键。

#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)
#del alien_0['points']
#print(alien_0)

##   在前面的示例中，字典存储的是一个对象（游戏中的一个外星人）的多种信息，但你也可以使用字典来存储众多对象的同一种信息。
##   例如，假设你要调查很多人，询问他们最喜欢的编程语言，可使用一个字典来存储这种简单调查的结果，如下所示：
#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#    }

#print("sarah's favorite language is " + 
#      favorite_languages['sarah'].title() +
#      ".")

#print(favorite_languages)

#'''
#        正如你看到的，我们将一个较大的字典放在了多行中。其中每个键都是一个被调查者的名字，
#    而每个值都是被调查者喜欢的语言。确定需要使用多行来定义字典时，在输入左花括号后按回车
#    键，再在下一行缩进四个空格，指定第一个键—值对，并在它后面加上一个逗号。此后你再次按
#    回车键时，文本编辑器将自动缩进后续键—值对，且缩进量与第一个键—值对相同。
#    定义好字典后，在最后一个键—值对的下一行添加一个右花括号，并缩进四个空格，使其与
#    字典中的键对齐。另外一种不错的做法是在最后一个键—值对后面也加上逗号，为以后在下一行
#    添加键—值对做好准备。
#'''

##   注意 对于较长的列表和字典，大多数编辑器都有以类似方式设置其格式的功能。对于较长的字典，
##   还有其他一些可行的格式设置方式，因此在你的编辑器或其他源代码中，你可能会看到稍微不同的格式设置方式。


#'''
#        一个python字典可能只包含几个键—值对，也可能包含数百万个键—值对。鉴于字典可能包含
#    大量的数据，python支持对字典遍历。字典可用于以各种方式存储信息，因此有多种遍历字典的           
#    方式：可遍历字典的所有键—值对、键或值。
#'''

#user_0 = {
#    'username': 'efermi',
#    'first': 'enrico',
#    'last': 'fermi',
#    }

#for key, value in user_0.items():
#    print("\nkey: " + key)
#    print("value: " + value)

##   要编写用于遍历字典的for循环，可声明两个变量，用于存储键—值对中的键和值。对于这两个变量，可使用任何名称。下面的代码使用了简单的变量名，这完全可行：
##   for k, v in user_0.items()

#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#    }

#for name, language in favorite_languages.items():
#    print(name.title() + "'s favorite language is " + language.title() + ".")


##   在不需要使用字典中的值时，方法keys()很有用。下面来遍历字典favorite_languages，并将每个被调查者的名字都打印出来：

#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#    }

#for name in favorite_languages.keys():
#    print(name.title())

#for name in favorite_languages.keys():
#    print(name.title())


##   遍历字典时，会默认遍历所有的键，因此，如果将上述代码中的for name in favorite_languages.keys():
##   替换为for name in favorite_languages:，输出将不变。如果显式地使用方法keys()可让代码更容易理解，
##   你可以选择这样做，但如果你愿意，也可省略它。



#######################################################################################################################################################################################################
#'''
#        在这种循环中，可使用当前键来访问与之相关联的值。下面来打印两条消息，指出两位朋友
#    喜欢的语言。我们像前面一样遍历字典中的名字，但在名字为指定朋友的名字时，打印一条消息，
#    指出其喜欢的语言：
#'''

#favorite_languages = {
#'jen': 'python',
#'sarah': 'c',
#'edward': 'ruby',
#'phil': 'python',
#}

#friends = ['phil', 'sarah']

#for name in favorite_languages.keys():
#    print(name.title())
#    if name in friends:
#        print(" hi " + name.title() +", i see your favorite language is " +favorite_languages[name].title() + "!")

##   方法keys()并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键.
#######################################################################################################################################################################################################

#print('\n')

#######################################################################################################################################################################################################
#'''
#        字典总是明确地记录键和值之间的关联关系，但获取字典的元素时，获取顺序是不可预测的。
#    这不是问题，因为通常你想要的只是获取与键相关联的正确的值。
#    要以特定的顺序返回元素，一种办法是在for循环中对返回的键进行排序。为此，可使用函
#    数sorted()来获得按特定顺序排列的键列表的副本：
#'''

#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#    }
#for name in sorted(favorite_languages.keys()):
#    print(name.title() + ", thank you for taking the poll.")

#######################################################################################################################################################################################################


##   如果你感兴趣的主要是字典包含的值，可使用方法values()，它返回一个值列表，而不包含任何键。

#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#    }

#print("the following languages have been mentioned:")
#for language in favorite_languages.values():
#    print(language.title())

#'''
#    这条for语句提取字典中的每个值，并将它们依次存储到变量language中。通过打印这些值，
#就获得了一个列表，其中包含被调查者选择的各种语言：
#the following languages have been mentioned:
#python
#c
#python
#ruby
#'''
##   这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不是问题，但如果被调查者很多，
##   最终的列表可能包含大量的重复项。为剔除重复项，可使用集合（set）。集合类似于列表，但每个元素都必须是独一无二的：

#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#    }
#print("the following languages have been mentioned:")
#for language in set(favorite_languages.values()):
#    print(language.title())

a = 3
print(a)
b = 3.1412926
print(math.floor(b))

##   通过对包含重复元素的列表调用set()，可让python找出列表中独一无二的元素，并使用这些元素来创建一个集合。
##   我们使用了set()来提取favorite_languages.values()中不同的语言。结果是一个不重复的列表。

##   有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。

#######################################################################################################################################################################################################
#'''
#        字典alien_0包含一个外星人的各种信息，但无法存储第二个外星人的信息，更别说屏幕上
#    全部外星人的信息了。如何管理成群结队的外星人呢？一种办法是创建一个外星人列表，其中每
#    个外星人都是一个字典，包含有关该外星人的各种信息。例如，下面的代码创建一个包含三个外
#    星人的列表：
#'''

#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'yellow', 'points': 10}
#alien_2 = {'color': 'red', 'points': 15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#    print(alien)

print(favorite_language.strip())          # strip()删除字符串两端的空白

#######################################################################################################################################################################################################


#######################################################################################################################################################################################################
#'''
#        更符合现实的情形是，外星人不止三个，且每个外星人都是使用代码自动生成的。在下面的
#    示例中，我们使用range()生成了30个外星人：
#'''

## 创建一个用于存储外星人的空列表
#aliens = []

## 创建30个绿色的外星人
#for alien_number in range(30):
#    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#    aliens.append(new_alien)

## 显示前五个外星人
#for alien in aliens[:5]:
#    print(alien)
#print("...")

## 显示创建了多少个外星人
#print("total number of aliens: " + str(len(aliens)))


#######################################################################################################################################################################################################

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

#######################################################################################################################################################################################################
#'''
#        可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。例如，如果有多个网站用户，
#    每个都有独特的用户名，可在字典中将用户名作为键，然后将每位用户的信息存储在一个字典中，
#    并将该字典作为与用户名相关联的值。在下面的程序中，对于每位用户，我们都存储了其三项信
#    息：名、姓和居住地；为访问这些信息，我们遍历所有的用户名，并访问与每个用户名相关联的
#    信息字典：
#'''

#users = {
#    'aeinstein': {
#        'first': 'albert',
#        'last': 'einstein',
#        'location': 'princeton',
#        },
#    'mcurie': {
#        'first': 'marie',
#        'last': 'curie',
#        'location': 'paris',
#        },
#}

#for username, user_info in users.items():
#    print("\nusername: " + username)
#    full_name = user_info['first'] + " " + user_info['last']
#    location = user_info['location']
#    print("\tfull name: " + full_name.title())
#    print("\tlocation: " + location.title())


#######################################################################################################################################################################################################

##   请注意，表示每位用户的字典的结构都相同，虽然python并没有这样的要求，但这使得嵌套的字典处理起来更容易。倘若表示每位用户的字典都包含不同的键，for循环内部的代码将更复杂。

######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################
print('\n')
print('\n')
print('\n')


#   大多数程序都旨在解决最终用户的问题，为此通常需要从用户那里获取一些信息。

#   函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。

#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)


#   注意：Sublime Text不能运行提示用户输入的程序。你可以使用Sublime Text来编写提示用户输入的程序，但必须从终端运行它们。
#   每当你使用函数input()时，都应指定清晰而易于明白的提示，准确地指出你希望用户提供什么样的信息——指出用户该输入任何信息的提示都行.
#
#   使用函数input()时，Python将用户输入解读为字符串。
#   将数值输入用于计算和比较前，务必将其转换为数值表示。

#   如果你使用的是Python 2.7，应使用函数raw_input()来提示用户输入。这个函数与Python 3中的input()一样，也将输入解读为字符串。
#   Python 2.7也包含函数input()，但它将用户输入解读为Python代码，并尝试运行它们。因此，最好的结果是出现错误，指出Python不明白输入的代码；
#   而最糟的结果是，将运行你原本无意运行的代码。如果你使用的是Python 2.7，请使用raw_input()而不是input()来获取输入。

#   要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break语句。

#   break语句用于控制程序流程，可使用它来控制哪些代码行将执行，哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。
#   注意：在任何Python循环中都可使用break语句。例如，可使用break语句来退出遍历列表或字典的for循环。

#   要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句，它不像break语句那样不再执行余下的代码并退出整个循环。

#   每个while循环都必须有停止运行的途径，这样才不会没完没了地执行下去。

#   每个程序员都会偶尔因不小心而编写出无限循环，在循环的退出条件比较微妙时尤其如此。如果程序陷入无限循环，可按Ctrl + C，也可关闭显示程序输出的终端窗口。
#   要避免编写无限循环，务必对每个while循环进行测试，确保它按预期那样结束。如果你希望程序在用户输入特定值时结束，可运行程序并输入这样的值；#   如果在这种情况下程序没有结束，请检查程序处理这个值的方式，确认程序至少有一个这样的地方能让循环条件为False或让break语句得以执行。

#   注意：有些编辑器（如Sublime Text）内嵌了输出窗口，这可能导致难以结束无限循环，因此不得不关闭编辑器来结束无限循环。

#   要记录大量的用户和信息，需要在while循环中使用列表和字典。


#   for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素。
#   要在遍历列表的同时对其进行修改，可使用while循环。通过将while循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示。

#   为模拟用户验证过程，我们打印一条验证消息并将用户加入到已验证用户列表中。未验证用户列表越来越短，而已验证用户列表越来越长。未验证用户列表为空后结束循环，再打印已验证用户列表


######################################################################################################################################################################################################
#   删除包含特定值的所有列表元素
#   假设你有一个宠物列表，其中包含多个值为'cat'的元素。要删除所有这些元素，可不断运行一个while循环，直到列表中不再包含值'cat'。
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

######################################################################################################################################################################################################


######################################################################################################################################################################################################
#   可使用while循环提示用户输入任意数量的信息。下面来创建一个调查程序，其中的循环每次执行时都提示输入被调查者的名字和回答。
#   我们将收集的数据存储在一个字典中，以便将回答同被调查者关联起来：

#responses = {}

## 设置一个标志，指出调查是否继续
#polling_active = True

#while polling_active:

#    # 提示输入被调查者的名字和回答
#    name = input("\nWhat is your name? ")
#    response = input("Which mountain would you like to climb someday? ")
    
#    # 将答卷存储在字典中
#    responses[name] = response
    
#    # 看看是否还有人要参与调查
#    repeat = input("Would you like to let another person respond? (yes/ no) ")

#    if repeat == 'no':
#        polling_active = False

## 调查结束，显示结果
#print("\n--- Poll Results ---")

#for name, response in responses.items():
#    print(name + " would like to climb " + response + ".")



#   大家有时候会形参、实参不分，因此如果你看到有人将函数定义中的变量称为实参或将函数调用中的变量称为形参，不要大惊小怪。

#   鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
#   向函数传递实参的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同；
#   也可使用关键字实参，其中每个实参都由变量名和值组成；还可使用列表和字典。


#   你调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
#   为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。
#   为明白其中的工作原理，来看一个显示宠物信息的函数。
#   这个函数指出一个宠物属于哪种动物以及它叫什么名字，如下所示：

def describe_pet(animal_type, pet_name):
    '''显示宠物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

#   你可以根据需要调用函数任意次。要再描述一个宠物，只需再次调用describe_pet()即可：
describe_pet('dog', 'willie')

#   调用函数多次是一种效率极高的工作方式。我们只需在函数中编写描述宠物的代码一次，然后每
#   当需要描述新宠物时，都可调用这个函数，并向它提供新宠物的信息。即便描述宠物的代码增加
#   到了10行，你依然只需使用一行调用函数的代码，就可描述一个新宠物。

#   位置实参的顺序很重要。

#   关键字实参是传递给函数的名称—值对。你直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆（不会得到名为Hamster的harry这样的结果）。
#   关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。

def describe_pet(animal_type, pet_name):
    '''显示宠物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#   关键字实参的顺序无关紧要，因为Python知道各个值该存储到哪个形参中。下面两个函数调用是等效的：
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

#   注意 使用关键字实参时，务必准确地指定函数定义中的形参名。

#   编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用指定的实参值；
#   否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。
#   使用默认值可简化函数调用，还可清楚地指出函数的典型用法。

######################################################################################################################################################################################################
#   例如，如果你发现调用describe_pet()时，描述的大都是小狗，就可将形参animal_type的默认值设置为'dog'。
#   这样，调用describe_pet()来描述小狗时，就可不提供这种信息：

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet(animal_type='hamster', pet_name='harry')

#   这里修改了函数describe_pet()的定义，在其中给形参animal_type指定了默认值'dog'。
#   这样，调用这个函数时，如果没有给animal_type指定值，Python将把这个形参设置为'dog'：

#   请注意，在这个函数的定义中，修改了形参的排列顺序。由于给animal_type指定了默认值，无需通过实参来指定动物类型，
#   因此在函数调用中只包含一个实参——宠物的名字。然而，Python依然将这个实参视为位置实参，因此如果函数调用中只包
#   含宠物的名字，这个实参将关联到函数定义中的第一个形参。这就是需要将pet_name放在形参列表开头的原因所在。

#   现在，使用这个函数的最简单的方式是，在函数调用中只提供小狗的名字：

describe_pet('willie')

#   注意 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参。



######################################################################################################################################################################################################




######################################################################################################################################################################################################
#   等效的函数调用
#   鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


#   基于这种定义，在任何情况下都必须给pet_name提供实参；指定该实参时可以使用位置方式，也可以使用关键字方式。
#   如果要描述的动物不是小狗，还必须在函数调用中给animal_type提供实参；
#   同样，指定该实参时可以使用位置方式，也可以使用关键字方式。下面对这个函数的所有调用都可行：

# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#   注意 使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行。使用对你来说最容易理解的调用方式即可。

######################################################################################################################################################################################################

#   等你开始使用函数后，如果遇到实参不匹配错误，不要大惊小怪。你提供的实参多于或少于函数完成其工作所需的信息时，将出现实参不匹配错误。

#   函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值被称为返回值。
#   在函数中，可使用return语句将值返回到调用函数的代码行。返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


######################################################################################################################################################################################################
#   有时候，需要让实参变成可选的，这样使用函数的人就只需在必要时才提供额外的信息。可使用默认值来让实参变成可选的。
#   例如，假设我们要扩展函数get_formatted_name()，使其还处理中间名。为此，可将其修改成类似于下面这样：

def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

#   只要同时提供名、中间名和姓，这个函数就能正确地运行。它根据这三部分创建一个字符串，在适当的地方加上空格，并将结果转换为首字母大写格式：


#   然而，并非所有的人都有中间名，但如果你调用这个函数时只提供了名和姓，它将不能正确地运行。为让中间名变成可选的，
#   可给实参middle_name指定一个默认值——空字符串，并在用户没有提供中间名时不使用这个实参。为让get_formatted_name()
#   在没有提供中间名时依然可行，可给实参middle_name指定一个默认值——空字符串，并将其移到形参列表的末尾：

def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

######################################################################################################################################################################################################


######################################################################################################################################################################################################
#   函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。

def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

#   这个函数接受简单的文本信息，将其放在一个更合适的数据结构中，让你不仅能打印这些信息，还能以其他方式处理它们。
#   当前，字符串'jimi'和'hendrix'被标记为名和姓。你可以轻松地扩展这个函数，使其接受可选值，如中间名、年龄、职业或你要存储的其他任何信息。

def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)


#   在函数定义中，我们新增了一个可选形参age，并将其默认值设置为空字符串。如果函数调用中包含这个形参的值，这个值将存储到字典中。
#   在任何情况下，这个函数都会存储人的姓名，但可对其进行修改，使其也存储有关人的其他信息。

######################################################################################################################################################################################################


######################################################################################################################################################################################################
'''
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# 这是一个无限循环!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
'''

#   在这个示例中，我们使用的是get_formatted_name()的简单版本，不涉及中间名。其中的while循环让用户输入姓名：依次提示用户输入名和姓。
#   但这个while循环存在一个问题：没有定义退出条件。请用户提供一系列输入时，该在什么地方提供退出条件呢？我们要让用户能够尽可能容易地退出，
#   因此每次提示用户输入时，都应提供退出途径。每次提示用户输入时，都使用break语句提供了退出循环的简单途径：

'''
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")

    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)

print("\nHello, " + formatted_name + "!")
'''

#   我们添加了一条消息来告诉用户如何退出，然后在每次提示用户输入时，都检查他输入的是否是退出值，如果是，就退出循环。现在，这个程序将不断地问候，直到用户输入的姓或名为'q'为止。

######################################################################################################################################################################################################


######################################################################################################################################################################################################
'''
    传递列表
    你经常会发现，向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对
    象（如字典）。将列表传递给函数后，函数就能直接访问其内容。下面使用函数来提高处理列表
    的效率。
'''

'''
    假设有一个用户列表，我们要问候其中的每位用户。下面的示例将一个名字列表传递给一个
    名为greet_users()的函数，这个函数问候列表中的每个人：
'''

def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)



######################################################################################################################################################################################################



######################################################################################################################################################################################################
'''
    在函数中修改列表
    将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永
    久性的，这让你能够高效地处理大量的数据。
'''

'''
    一家为用户提交的设计制作3D打印模型的公司。需要打印的设计存储在一个列表中，
    打印后移到另一个列表中。下面是在不使用函数的情况下模拟这个过程的代码：
'''

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)

    # 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


#   这个程序首先创建一个需要打印的设计列表，还创建一个名为completed_models的空列表，
#   每个设计打印都将移到这个列表中。只要列表unprinted_designs中还有设计，while循环就
#   模拟打印设计的过程：从该列表末尾删除一个设计，将其存储到变量current_design中，并
#   显示一条消息，指出正在打印当前的设计，再将该设计加入到列表completed_models中。

'''
    为重新组织这些代码，我们可编写两个函数，每个都做一件具体的工作。大部分代码都与原来相同，只是效率更高。
'''
def print_models(unprinted_designs, completed_models):

    #   模拟打印每个设计，直到没有未打印的设计为止
    #   打印每个设计后，都将其移到列表completed_models中
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    
    #   显示打印好的所有模型
    print("\nThe following models have been printed:")

    for completed_model in completed_models:
        print(completed_model)
    
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
print(completed_models)

#   首先，我们定义了函数print_models()，它包含两个形参：一个需要打印的设计列表和一个打印好的模型列表。
#   给定这两个列表，这个函数模拟打印每个设计的过程：将设计逐个地从未打印的设计列表中取出， 并加入到打印好的模型列表中。接着， 我们定义了函数
#   show_completed_models() ，它包含一个形参：打印好的模型列表。给定这个列表，函数show_completed_models()显示打印出来的每个模型的名称。
#   这个程序的输出与未使用函数的版本相同，但组织更为有序。完成大部分工作的代码都移到了两个函数中，让主程序更容易理解


'''
        我们创建了一个未打印的设计列表，还创建了一个空列表，用于存储打印好的模型。接下来，
    由于我们已经定义了两个函数，因此只需调用它们并传入正确的实参即可。我们调用
    print_models()并向它传递两个列表；像预期的一样，print_models()模拟打印设计的过程。接
    下来，我们调用show_completed_models()，并将打印好的模型列表传递给它，让其能够指出打印
    了哪些模型。描述性的函数名让别人阅读这些代码时也能明白，虽然其中没有任何注释。
    相比于没有使用函数的版本，这个程序更容易扩展和维护。如果以后需要打印其他设计，
    只需再次调用print_models()即可。如果我们发现需要对打印代码进行修改，只需修改这些代码
    一次，就能影响所有调用该函数的地方；与必须分别修改程序的多个地方相比，这种修改的效
    率更高。
    这个程序还演示了这样一种理念，即每个函数都应只负责一项具体的工作。第一个函数打印
    每个设计，而第二个显示打印好的模型；这优于使用一个函数来完成两项工作。编写函数时，如
    果你发现它执行的任务太多，请尝试将这些代码划分到两个函数中。别忘了，总是可以在一个函
    数中调用另一个函数，这有助于将复杂的任务划分成一系列的步骤。
'''

'''
        # 禁止函数修改列表
        我们创建了一个未打印的设计列表，还创建了一个空列表，用于存储打印好的模型。接下来，
    由于我们已经定义了两个函数，因此只需调用它们并传入正确的实参即可。我们调用
    print_models()并向它传递两个列表；像预期的一样，print_models()模拟打印设计的过程。接
    下来，我们调用show_completed_models()，并将打印好的模型列表传递给它，让其能够指出打印
    了哪些模型。描述性的函数名让别人阅读这些代码时也能明白，虽然其中没有任何注释。
    相比于没有使用函数的版本，这个程序更容易扩展和维护。如果以后需要打印其他设计，
    只需再次调用print_models()即可。如果我们发现需要对打印代码进行修改，只需修改这些代码
    一次，就能影响所有调用该函数的地方；
        function_name(list_name[:])
        切片表示法[:]创建列表的副本。在程序中，如果不想清空未打印的设计列表，可像下面这样
    调用print_models()：
        print_models(unprinted_designs[:], completed_models)
        这样函数print_models()依然能够完成其工作，因为它获得了所有未打印的设计的名称，但
    它使用的是列表unprinted_designs的副本，而不是列表unprinted_designs本身。像以前一样，列
    表completed_models也将包含打印好的模型的名称，但函数所做的修改不会影响到列表
    unprinted_designs。
    虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，否
    则还是应该将原始列表传递给函数，因为让函数使用现成列表可避免花时间和内存创建副本，从
    而提高效率，在处理大型列表时尤其如此。
'''
######################################################################################################################################################################################################

def print_models(unprinted_designs, completed_models):

    #   模拟打印每个设计，直到没有未打印的设计为止
    #   打印每个设计后，都将其移到列表completed_models中
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    
    #   显示打印好的所有模型
    print("\nThe following models have been printed:")

    for completed_model in completed_models:
        print(completed_model)
    
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
print(completed_models)



######################################################################################################################################################################################################

'''
    # 传递任意数量的实参
    有时候，你预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任
意数量的实参。
例如，来看一个制作比萨的函数，它需要接受很多配料，但你无法预先确定顾客要多少种配
料。下面的函数只有一个形参*toppings，但不管调用语句提供了多少实参，这个形参都将它们
统统收入囊中：
'''

def make_pizza(*toppings):

    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

'''
        形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封
    装到这个元组中。函数体内的print语句通过生成输出来证明Python能够处理使用一个值调用函
    数的情形，也能处理使用三个值来调用函数的情形。它以类似的方式处理不同的调用，注意，
    Python将实参封装到一个元组中，即便函数只收到一个值也如此：
'''

def make_pizza(*toppings):
    """概述要制作的比萨""" 
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#   不管函数收到的实参是多少个，这种语法都管用。

######################################################################################################################################################################################################


######################################################################################################################################################################################################

'''
    # 结合使用位置实参和任意数量实参
    如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最
后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

'''
'''
    例如，如果前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在形参*toppings
的前面：
'''
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

'''
        形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封
    装到这个元组中。函数体内的print语句通过生成输出来证明Python能够处理使用一个值调用函
    数的情形，也能处理使用三个值来调用函数的情形。它以类似的方式处理不同的调用，注意，
    Python将实参封装到一个元组中，即便函数只收到一个值也如此：
'''

def make_pizza(*toppings):
    """概述要制作的比萨""" 
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#   不管函数收到的实参是多少个，这种语法都管用。

######################################################################################################################################################################################################


######################################################################################################################################################################################################

'''
    # 结合使用位置实参和任意数量实参
    如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最
后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

'''
'''
    例如，如果前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在形参*toppings
的前面：
'''
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

'''
    基于上述函数定义，Python将收到的第一个值存储在形参size中，并将其他的所有值都存储
在元组toppings中。在函数调用中，首先指定表示比萨尺寸的实参，然后根据需要指定任意数量
的配料。
    现在，每个比萨都有了尺寸和一系列配料，这些信息按正确的顺序打印出来了——首先是尺
寸，然后是配料
'''

######################################################################################################################################################################################################


######################################################################################################################################################################################################

'''
    # 使用任意数量的关键字实参
    有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种
情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。
    一个这样的示例是创建用户简介：你知道你将收到有关用户的信息，但不确定会是什么样的信息。
在下面的示例中，函数build_profile()接受名和姓，同时还接受任意数量的关键字实参。

'''
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)

'''
    函数build_profile()的定义要求提供名和姓，同时允许用户根据需要提供任意数量的名称—
值对。形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的所
有名称—值对都封装到这个字典中。在这个函数中，可以像访问其他字典那样访问user_info中的
名称—值对。
    在build_profile()的函数体内，我们创建了一个名为profile的空字典，用于存储用户简介。
在"profile['last_name'] = last"处，我们将名和姓加入到这个字典中，因为我们总是会从用户
那里收到这两项信息。在"for key, value in user_info.items():"处，我们遍历字典user_info
中的键—值对，并将每个键—值对都加入到字典profile中。最后，我们将字典profile返回给函
数调用行。
    我们调用build_profile()，向它传递名（'albert'）、姓（'einstein'）和两个键—值对
（location='princeton'和field='physics'），并将返回的profile存储在变量user_profile中，
再打印这个变量：
'''

######################################################################################################################################################################################################


'''
    # 将函数存储在模块中
    函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让
主程序容易理解得多。你还可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导
入到主程序中。import语句允许在当前运行的程序文件中使用模块中的代码。
    通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。
这还能让你在众多不同的程序中重用函数。将函数存储在独立文件中后，可与其他程序员共享这
些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。
'''



######################################################################################################################################################################################################

'''
    # 导入整个模块
    要让函数是可导入的，得先创建模块。模块是扩展名为.py的文件，包含要导入到程序中的
代码。下面来创建一个包含函数make_pizza()的模块。为此，我们将文件pizza.py中除函数
make_pizza()之外的其他代码都删除：

'''

'''
    # pizza.py
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
    print("- " + topping)

'''

'''
    接下来，我们在pizza.py所在的目录中创建另一个名为making_pizzas.py的文件，这个文件导
入刚创建的模块，再调用make_pizza()两次。

'''


'''
    # making_pizzas.py
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

'''

'''
    Python读取这个文件时，代码行import pizza让Python打开文件pizza.py，并将其中的所有函
数都复制到这个程序中。你看不到复制的代码，因为这个程序运行时，Python在幕后复制这些代
码。你只需知道，在making_pizzas.py中，可以使用pizza.py中定义的所有函数。
    要调用被导入的模块中的函数，可指定导入的模块的名称pizza和函数名make_pizza()，并用
句点分隔它们。这些代码的输出与没有导入模块的原始程序相同
'''


'''
    这就是一种导入方法：只需编写一条import语句并在其中指定模块名，就可在程序中使用该
模块中的所有函数。如果你使用这种import语句导入了名为module_name.py的整个模块，就可使
用下面的语法来使用其中任何一个函数：
    module_name.function_name()
'''


######################################################################################################################################################################################################


######################################################################################################################################################################################################

'''
    # 导入特定的函数
    你还可以导入模块中的特定函数，这种导入方法的语法如下：
        from module_name import function_name

    通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
        from module_name import function_0, function_1, function_2

    对于前面的making_pizzas.py示例，如果只想导入要使用的函数，代码将类似于下面这样：
        from pizza import make_pizza

        make_pizza(16, 'pepperoni')
        make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
    
    若使用这种语法，调用函数时就无需使用句点。由于我们在import语句中显式地导入了函数
make_pizza()，因此调用它时只需指定其名称。
    
'''


######################################################################################################################################################################################################



######################################################################################################################################################################################################

'''
    # 使用as 给函数指定别名
    如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短
而独一无二的别名——函数的另一个名称，类似于外号。要给函数指定这种特殊外号，需要在导
入它时这样做。
    下面给函数make_pizza()指定了别名mp()。这是在import语句中使用make_pizza as mp实现的，
关键字as将函数重命名为你提供的别名：
        from pizza import make_pizza as mp

        mp(16, 'pepperoni')
        mp(12, 'mushrooms', 'green peppers', 'extra cheese')

    上面的import语句将函数make_pizza()重命名为mp()；在这个程序中，每当需要调用
make_pizza()时，都可简写成mp()，而Python将运行make_pizza()中的代码，这可避免与这个程序
可能包含的函数make_pizza()混淆。
    指定别名的通用语法如下：
       from module_name import function_name as fn


'''

######################################################################################################################################################################################################


######################################################################################################################################################################################################

'''
    # 使用as 给模块指定别名
    你还可以给模块指定别名。通过给模块指定简短的别名（如给模块pizza指定别名p），让你
能够更轻松地调用模块中的函数。相比于pizza.make_pizza()，p.make_pizza()更为简洁：
        
        import pizza as p

        p.make_pizza(16, 'pepperoni')
        p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    上述import语句给模块pizza指定了别名p，但该模块中所有函数的名称都没变。调用函数
make_pizza()时，可编写代码p.make_pizza()而不是pizza.make_pizza()，这样不仅能使代码更简
洁，还可以让你不再关注模块名，而专注于描述性的函数名。这些函数名明确地指出了函数的功
能，对理解代码而言，它们比模块名更重要。
    给模块指定别名的通用语法如下：
        import module_name as mn


'''

######################################################################################################################################################################################################


######################################################################################################################################################################################################

'''
    # 导入模块中的所有函数
    你还可以给模块指定别名。通过给模块指定简短的别名（如给模块pizza指定别名p），让你
能够更轻松地调用模块中的函数。相比于pizza.make_pizza()，p.make_pizza()更为简洁：
        
        import pizza as p

        p.make_pizza(16, 'pepperoni')
        p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    import语句中的星号让Python将模块pizza中的每个函数都复制到这个程序文件中。由于导入
了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。然而，使用并非自己编写的
大型模块时，最好不要采用这种导入方法：如果模块中有函数的名称与你的项目中使用的名称相
同，可能导致意想不到的结果：Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而
不是分别导入所有的函数。
    最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。这能
让代码更清晰，更容易阅读和理解。这里之所以介绍这种导入方法，只是想让你在阅读别人编写
的代码时，如果遇到类似于下面的import语句，能够理解它们：
        from module_name import *

'''

######################################################################################################################################################################################################

######################################################################################################################################################################################################

'''
    # 函数编写指南
    编写函数时，需要牢记几个细节。应给函数指定描述性名称，且只在其中使用小写字母和下
划线。描述性名称可帮助你和别人明白代码想要做什么。给模块命名时也应遵循上述约定。
每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字
符串格式。文档良好的函数让其他程序员只需阅读文档字符串中的描述就能够使用它：他们完全
可以相信代码如描述的那样运行；只要知道函数的名称、需要的实参以及返回值的类型，就能在
自己的程序中使用它。
    给形参指定默认值时，等号两边不要有空格：
        def function_name(parameter_0, parameter_1='default value')
    对于函数调用中的关键字实参，也应遵循这种约定：
        function_name(value_0, parameter_1='value')
    PEP 8（https://www.python.org/dev/peps/pep-0008/）建议代码行的长度不要超过79字符，这样
只要编辑器窗口适中，就能看到整行代码。如果形参很多，导致函数定义的长度超过了79字符，
可在函数定义中输入左括号后按回车键，并在下一行按两次Tab键，从而将形参列表和只缩进一
层的函数体区分开来。
    大多数编辑器都会自动对齐后续参数列表行，使其缩进程度与你给第一个参数列表行指定的
缩进程度相同：
        
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
        function body...

如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开，这样将更容易知道前一
个函数在什么地方结束，下一个函数从什么地方开始。
    所有的import语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整
个程序。

'''

######################################################################################################################################################################################################


'''
    程序员的目标之一是，编写简单的代码来完成任务，而函数有助于你实现这样的目标。它们
让你编写好代码块并确定其能够正确运行后，就可置之不理。确定函数能够正确地完成其工作后，
你就可以接着投身于下一个编码任务。
    函数让你编写代码一次后，想重用它们多少次就重用多少次。需要运行函数中的代码时，只
需编写一行函数调用代码，就可让函数完成其工作。需要修改函数的行为时，只需修改一个代码
块，而所做的修改将影响调用这个函数的每个地方。
    使用函数让程序更容易阅读，而良好的函数名概述了程序各个部分的作用。相对于阅读一系
列的代码块，阅读一系列函数调用让你能够更快地明白程序的作用。
    函数还让代码更容易测试和调试。如果程序使用一系列的函数来完成其任务，而其中的每个
函数都完成一项具体的工作，测试和维护起来将容易得多：你可编写分别调用每个函数的程序，
并测试每个函数是否在它可能遇到的各种情形下都能正确地运行。经过这样的测试后你就能信心
满满，深信你每次调用这些函数时，它们都将正确地运行。
'''



######################################################################################################################################################################################################

'''
    面向对象编程是最有效的软件编写方法之一。在面向对象编程中，
你编写表示现实世界中的事物和情景的类，并基于这些类来创建对象。
编写类时，你定义一大类对象都有的通用行为。基于类创建对象时，
每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独
特的个性。使用面向对象编程可模拟现实情景，其逼真程度达到了令
你惊讶的地步。
    根据类来创建对象被称为实例化，这让你能够使用类的实例。在
本章中，你将编写一些类并创建其实例。你将指定可在实例中存储什
么信息，定义可对这些实例执行哪些操作。你还将编写一些类来扩展
既有类的功能，让相似的类能够高效地共享代码。你将把自己编写的类存储在模块中，并在
自己的程序文件中导入其他程序员编写的类
    # 创建和使用类
    使用类几乎可以模拟任何东西。下面来编写一个表示小狗的简单类Dog——它表示的不是特
定的小狗，而是任何小狗。对于大多数宠物狗，我们都知道些什么呢？它们都有名字和年龄；我
们还知道，大多数小狗还会蹲下和打滚。由于大多数小狗都具备上述两项信息（名字和年龄）和
两种行为（蹲下和打滚），我们的Dog类将包含它们。这个类让Python知道如何创建表示小狗的对
象。编写这个类后，我们将使用它来创建表示特定小狗的实例。
    # 创建Dog 类  
    根据Dog类创建的每个实例都将存储名字和年龄。我们赋予了每条小狗蹲下（sit()）和打滚
（roll_over()）的能力：
    
    dog.py

   class Dog():

       """一次模拟小狗的简单尝试"""

       def __init__(self, name, age):
            """初始化属性name和age"""
          self.name = name
            self.age = age

       def sit(self):
            """模拟小狗被命令时蹲下"""
            print(self.name.title() + " is now sitting.")

        def roll_over(self):
            """模拟小狗被命令时打滚"""
            print(self.name.title() + " rolled over!")


    在“class Dog():”处，我们定义了一个名为Dog的类。根据约定，在Python中，首字母大写的名称指的是类。
这个类定义中的括号是空的，因为我们要从空白创建这个类。在“"""一次模拟小狗的简单尝试"""”处，我们编写了一个文档字符
串，对这个类的功能作了描述。
    1. 方法__init__()
    类中的函数称为方法；你前面学到的有关函数的一切都适用于方法，就目前而言，唯一重要
的差别是调用方法的方式。“def __init__(self, name, age):”处的方法__init__()是一个特殊的方法，每当你根据Dog类创建新实
例时，Python都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，这是一种约
定，旨在避免Python默认方法与普通方法发生名称冲突。
    “def sit(self):”处定义的两个变量都有前缀self。以self为前缀的变量都可供类中的所有方法使用，我们
还可以通过类的任何实例来访问这些变量。self.name = name获取存储在形参name中的值，并将
其存储到变量name中，然后该变量被关联到当前创建的实例。self.age = age的作用与此类似。 
像这样可通过实例访问的变量称为属性。
    Dog类还定义了另外两个方法：sit()和roll_over()。由于这些方法不需要额外的信
息，如名字或年龄，因此它们只有一个形参self。我们后面将创建的实例能够访问这些方法，换
句话说，它们都会蹲下和打滚。当前，sit()和roll_over()所做的有限，它们只是打印一条消息，
指出小狗正蹲下或打滚。但可以扩展这些方法以模拟实际情况：如果这个类包含在一个计算机游
戏中，这些方法将包含创建小狗蹲下和打滚动画效果的代码。如果这个类是用于控制机器狗的，
这些方法将引导机器狗做出蹲下和打滚的动作。    
    2. 在Python 2.7中创建类
    在Python 2.7中创建类时，需要做细微的修改——在括号内包含单词object：
    
    class ClassName(object):
        --snip--
    这让Python 2.7类的行为更像Python 3类，从而简化了你的工作。
    在Python 2.7中定义Dog类时，代码类似于下面这样：
    
    class Dog(object):
        --snip--
    



'''

######################################################################################################################################################################################################


































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

#如果你不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：如果你要从列表
#中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续
#使用它，就使用方法pop()。

