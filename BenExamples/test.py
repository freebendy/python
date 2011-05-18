# -*- coding: cp936 -*-

"""
特点（脚本语言）：
1.解释执行
2.面向对象
3.内建高级数据结构
4.支持模块和包
5.支持多平台
6.可扩展

它非常适合于教学。在学习Python的过程中，它可以使学生专注计算
机程序语言的基本概念，着中理解现代程序语言的精髓，而不必理会那
些细枝末节、令人头痛技术细节，这些细节问题不但难于讲解，也很难理
解，而且还会使学生产生厌烦情绪，无助于计算机程序语言的学习。

introspection --- 自省是指代码可以查看内存中以对象形式存在的其它模块和函数，
获取它们的信息，并对它们进行操作。用这种方法，你可以定义没有名称的
函数，不按函数声明的参数顺序调用函数，甚至引用事先并不知道名称的函
数。
"""

'''
参考编码规范：http://wiki.woodpecker.org.cn/moinPython%E5%BC%80%E5%8F%91%E7%BC%96%E7%A0%81%E8%A7%84%E8%8C%83
'''

print "hello,world!"

#获取命令行参数
import sys
print "arguments' length:",len(sys.argv)
for arg in sys.argv:
    print arg


#换行字符串
s="""
dsadd
sa
d"""
print s #"\ndsadd\nsa\nd"

print type(111) #int
print type(111L) #long

a=11
b=-9
c=a+b

# 注意冒号的使用 *****
# 代码块用缩进定义
# Python 使用硬回车来分割语句，冒号和缩进来分割代码块。
if c>3:
    print "More than 3."
else:
    print "Less than 3."

# 幕操作
print 3**2
print 3**4
print pow(3,4)

#每个值或变量都有一个唯一id，id值与变量或值在内存中的位置相关。变量的id也就是它所指向值的id。
print '111.id =',id(111)
print '"111".id =',id("111")
print '"dsad".id =',id("dsad")

# 导入module的方式
# 1.目录添加到PYTHONPATH环境变量，子目录添加__init__.py文件
# 2.子目录添加__init__.py文件，如下调用
from lib.functions import add
print "add result = ", add(a,b)

# 参数是按值传递
def modify(p):
    p = 3

print "a before modify: ",a
modify(a)
print "a after modify: ",a

# 没有返回值返回None
print modify(b) #None

print type(None) #NoneType

import math #导入math模块
print "pi = ",math.pi

#类型转换

print int("111")
print int(2.111)
print float(2)
print str(32321)

#lambda 单行小函数,只有一个表达式，不包含命令，可以考虑lambda函数（与def相比不够灵活）。
lam = lambda x,y: x*y
print lam(a,b)

print (lambda x,y: x+y)(a,b)

# 真值为1，假值为0, 非零值均为真。
#空字符串为假，非空字符串为真
print a==b,a!=b
print a and 0 # return 0
print 0 and b # return 0
print a and b # return b

print a or b # return a
print 0 or a # return a
print "" or 0
print 0 or ""
print 0 or a==b

print not a
print not b

#and操作符 只要左面表达式为真，返回右面表达式，否则返回左面表达式
#or操作符 两边为真返回左面，一真一假返回真，两边为假返回右面

if a:
    print "a is true"
else:
    print "a is false"
    
if b:
    print "b is true"
else:
    print "b is false"
    
tmp=0

if tmp:
    print "tmp is true"
else:
    print "tmp is false"

if "":
    print "empty is true"
else:
    print "empty is false"
    
print a and "hello"
print a or "hello"
print not "hello"

#引入函数
import sys
print sys.path
sys.path.append('D:\\Work\\Ben\'s Notes\\Python\\BenExamples\\lib')
print sys.path

from lib.helloworld import hello
hello(2)

from lib.helloworld import minus
minus()

# 键盘输入
#name = raw_input("please input your name:") #运行时会先调用这个
#print "your name is:",name

#组合型数据
strings="hello,python"
for ch in strings:
    print ch
    
print "len(strings):",len(strings)
print "strings[0]:",strings[0]
#print "strings[12]:",strings[12]
#获取字串
print "strings[0:5]:",strings[0:5]
print "strings[6:12]:",strings[6:12]
print "strings[:]:",strings[:]
#[n:m] means [n,0), [,m] begin with 0, [n,] end with last char.[:]
newStr= '1' + strings[1:]
print "newStr:",newStr
#strings[0]='1' #error, can't modify

import string
print string.find(strings,',')
print string.uppercase

#列表 ?类似javascript里面json
list1=[1,2,3,4,5,4,56,6,1,1,]
print list1

list2=["hello", 2.0, 5, [10,20]]
print list2
print list2[0]
print list2[3][1]

list3=[a,b,2134]
print list3

#索引为负数
print list3[-2]
print strings[-1]

print range(1,5)
print range(5)
print range(1,11,2)

#方法
list3.append([1,2])
list3.insert(2,"abc")
print list3
list3.extend(list1) 
print list3
print list3.index([1,2])
#print list3.index(13213) #error
list3.remove(1) #remove第一个1
print list3
list3.pop()
print list3

print len(list3)
print 'abc' in list3 #in操作符

print list1+list2
print list2*2

#片段：和字符串一样，但是只要[]包含:，所去片段依然是列表,此外列表是可以通过[]来修改（字符串不可以）
print list1[0:0],type(list1[0:0])
list4=range(5)
list4[3:4]=[1]
list4[0:0]=[11] #第一个元素前插入
print list4
del list4[1:3]
print list4

# COW
print "#"
i1=123
i2=123
print id(i1),id(i2) #地址一样
i2=321
print id(i1),id(i2)

print "#"
s1="abc"
s2="abc"
print id(s1),id(s2)
s2="cba"
print id(s1),id(s2)

print "#"
f1=1.11
f2=1.11
print id(f1),id(f2)
f2=2.1111
print id(f1),id(f2)

print "#"
#不一样
l1=[1,2]
l2=[1,2]
print id(l1),id(l2)
l2=[2,3,4]
print id(l1),id(l2)

#别名
print "\n\n"
la=[1,23,4]
lb=la;
print id(la),id(lb)
lb[0]=88
print la
lb=[-1,2,99]
print la

ia=10
ib=ia
ib=1111
print ia #10
#调用了复制操作就不再是别名？

#clone
lc=la[:]
lc.append(123)
print la

#列表参数传递：引用传递 ****
from lib.list import listPop
listToPop=[1,2,3,444]
listPop(listToPop)
print "listToPop:",listToPop
#如果不想改变，clone列表

#字符串和列表的转换
#split和join
ss="I am a student. Are you?"
ll=string.split(ss)
llDot=string.split(ss,".")
print ll,llDot
print string.join(ll), "\n" ,string.join(llDot,".")
#也可以这样用
print "------",".".join(llDot)
print "------"," ".join(ll)

#列表映射
fruits=["apple","orange","pear","banana"]
print [fruit+'s' for fruit in fruits]
print [fruit+'s' for fruit in fruits if len(fruit) != 6]


#序列：与列表比较相似，但是元素的值是固定的
tuple1=1,2,3,4,5,6,7
tuple2=(1,2,546,7,8,78,7,)
print type(tuple1),type(tuple2),
print type(('a')),type(('a',)) #一个逗号的区别

#一个好处:交换值
#a=1
#b=2
#temp=a
#a=b
#b=temp

a=1
b=2
c=3
a,b,c = c,b,a
print a,b,c
#赋值操作两边的序列元素要一致，否则解析器报错

def swap(a,b):
    return b,a

    
# 0-1的随机数
import random
print random.random()

#字典
dict1={"name": "Ben", "age":"28"}
print dict1["name"]
dict1["name"]="guan"
print dict1["name"]


dict={"M":111,"U": 2}
print dict

dictAlias=dict1 #别名
dictAlias["name"]="BK"
print dict1["name"]

dict2=dict1.copy() #拷贝

#删除 del dict[key]
#清空 dict.clear()
#长度 len(dict)

#稀疏矩阵
matrix = [ [0,0,0,1,0],
            [0,0,0,0,0],
            [0,2,0,0,0],
            [0,0,0,0,0],
            [0,0,0,3,0] ]
print type(matrix) #list

matrixDict = {(0,3): 1, (2, 1): 2, (4, 3): 3}
print matrixDict[2,1]
#print matrixDict[2,3] #error
print matrixDict.get((2,3),0) #找不到返回0

#from fibonacci import fibonacci
#print fibonacci(30) #很慢

#from fibonacci_improve import fibonacci_improve
#print fibonacci_improve(40) #很快
#print fibonacci_improve(100) #依旧很快

#文件操作
#import os
#print os.getcwd() #工作目录
#print sys.path[0] #当前脚本的目录
#print sys.argv[0]
#print os.path.abspath(sys.argv[0])

from lib.path import cur_file_dir

#print cur_file_dir()
#print file.__doc__ # help()->file
name="Ben"
corp="Tieto"
f=open(cur_file_dir() + "\\test.txt","w")
try:
    print f
    f.write("hello")
    f.write(",")
    f.write("python.")
    f.write("\nMy name is %s." % name)
    f.write("\nI am in%s" % corp)
    f.write("\nEnd of the file.")
    f.close()
except:
    print "exception"
    f.close()

f=open(cur_file_dir() + "\\test.txt","r")
print f.tell()
print f.read()
print f.tell()
print "---------------"
f.seek(0)
print f.readline()
print "---------------"
f.seek(0)
lines=f.readlines()
for line in lines:
    print line,
f.close()
print "\n---------------"

#让写入的数据保持原类型
import pickle
f1=open(cur_file_dir() + "\\ben.txt","w")
try:
    pickle.dump("I was born in",f1)
    pickle.dump(1983,f1)
    f1.close()
except:
    print "exception"
    f1.close()

f1=open(cur_file_dir() + "\\ben.txt","r")
str=pickle.load(f1)
print str,type(str)
i=pickle.load(f1)
print i,type(i)
f1.close()

try:
    raise  IOError, 'just a joke.'
except IOError, e:
    print e
    

    
class Point:
    pass

p=Point()

print type(Point),type(p)

p0 = p
print p,p0

import copy
p1=copy.copy(p)
print p,p1

p2=copy.deepcopy(p)
print p,p2


class Time:
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        
    #重载
    def __sub__(self,other):
        h=self.hours-other.hours
        m=self.minutes-other.minutes
        s=self.seconds-other.seconds
        return h*3600+m*60+s
        
    def printTime(self):
        print self.hours,":",self.minutes,":",self.seconds
        

t=Time(14,20,30)
t.printTime()
t1=Time(15,30,11)
print t-t1


class Person:
    def __init__(self,name,age=1,sex='male'):
        self.name=name
        self.age=age
        self.sex=sex
    
    def displayInfo(self):
        print "name  :   %20s" % self.name
        print "age   :   %20d" % self.age
        print "sex   :   %20s" % self.sex

class Student(Person):
    def __init__(self,name,age,sex='male',id=0):
        Person.__init__(self,name,age,sex)
        self.id=id

    def displayInfo(self):
        Person.displayInfo(self)
        print "id    :   %20d" % self.id

p=Person("ben",28)
p.displayInfo()

s=Student("Guan",21,"female",2)
s.displayInfo()

from apihelper import info
#info(dict)

def foo():
	l = range(10)
	l.sort()
	return l
import profile
profile.run('foo()')
        
'''
八荣八耻
以动手实践为荣 , 以只看不练为耻;
以打印日志为荣 , 以单步跟踪为耻;
以空格缩进为荣 , 以制表缩进为耻;
以单元测试为荣 , 以人工测试为耻;

以模块复用为荣 , 以复制粘贴为耻;
以多态应用为荣 , 以分支判断为耻;
以Pythonic为荣 , 以冗余拖沓为耻;
以总结分享为荣 , 以跪求其解为耻;


Pythonic: 
    http://blog.csdn.net/lanphaday/archive/2008/08/03/2762251.aspx 
    http://faassen.n--tree.net/blog/view/weblog/2005/08/06/0
'''