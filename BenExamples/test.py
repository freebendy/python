# -*- coding: cp936 -*-

"""
�ص㣨�ű����ԣ���
1.����ִ��
2.�������
3.�ڽ��߼����ݽṹ
4.֧��ģ��Ͱ�
5.֧�ֶ�ƽ̨
6.����չ

���ǳ��ʺ��ڽ�ѧ����ѧϰPython�Ĺ����У�������ʹѧ��רע����
���������ԵĻ��������������ִ��������Եľ��裬�����������
Щϸ֦ĩ�ڡ�����ͷʹ����ϸ�ڣ���Щϸ�����ⲻ�����ڽ��⣬Ҳ������
�⣬���һ���ʹѧ�������ᷳ�����������ڼ�����������Ե�ѧϰ��

introspection --- ��ʡ��ָ������Բ鿴�ڴ����Զ�����ʽ���ڵ�����ģ��ͺ�����
��ȡ���ǵ���Ϣ���������ǽ��в����������ַ���������Զ���û�����Ƶ�
�������������������Ĳ���˳����ú����������������Ȳ���֪�����Ƶĺ�
����
"""

'''
�ο�����淶��http://wiki.woodpecker.org.cn/moinPython%E5%BC%80%E5%8F%91%E7%BC%96%E7%A0%81%E8%A7%84%E8%8C%83
'''

print "hello,world!"

#��ȡ�����в���
import sys
print "arguments' length:",len(sys.argv)
for arg in sys.argv:
    print arg


#�����ַ���
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

# ע��ð�ŵ�ʹ�� *****
# ���������������
# Python ʹ��Ӳ�س����ָ���䣬ð�ź��������ָ����顣
if c>3:
    print "More than 3."
else:
    print "Less than 3."

# Ļ����
print 3**2
print 3**4
print pow(3,4)

#ÿ��ֵ���������һ��Ψһid��idֵ�������ֵ���ڴ��е�λ����ء�������idҲ��������ָ��ֵ��id��
print '111.id =',id(111)
print '"111".id =',id("111")
print '"dsad".id =',id("dsad")

# ����module�ķ�ʽ
# 1.Ŀ¼��ӵ�PYTHONPATH������������Ŀ¼���__init__.py�ļ�
# 2.��Ŀ¼���__init__.py�ļ������µ���
from lib.functions import add
print "add result = ", add(a,b)

# �����ǰ�ֵ����
def modify(p):
    p = 3

print "a before modify: ",a
modify(a)
print "a after modify: ",a

# û�з���ֵ����None
print modify(b) #None

print type(None) #NoneType

import math #����mathģ��
print "pi = ",math.pi

#����ת��

print int("111")
print int(2.111)
print float(2)
print str(32321)

#lambda ����С����,ֻ��һ�����ʽ��������������Կ���lambda��������def��Ȳ�������
lam = lambda x,y: x*y
print lam(a,b)

print (lambda x,y: x+y)(a,b)

# ��ֵΪ1����ֵΪ0, ����ֵ��Ϊ�档
#���ַ���Ϊ�٣��ǿ��ַ���Ϊ��
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

#and������ ֻҪ������ʽΪ�棬����������ʽ�����򷵻�������ʽ
#or������ ����Ϊ�淵�����棬һ��һ�ٷ����棬����Ϊ�ٷ�������

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

#���뺯��
import sys
print sys.path
sys.path.append('D:\\Work\\Ben\'s Notes\\Python\\BenExamples\\lib')
print sys.path

from lib.helloworld import hello
hello(2)

from lib.helloworld import minus
minus()

# ��������
#name = raw_input("please input your name:") #����ʱ���ȵ������
#print "your name is:",name

#���������
strings="hello,python"
for ch in strings:
    print ch
    
print "len(strings):",len(strings)
print "strings[0]:",strings[0]
#print "strings[12]:",strings[12]
#��ȡ�ִ�
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

#�б� ?����javascript����json
list1=[1,2,3,4,5,4,56,6,1,1,]
print list1

list2=["hello", 2.0, 5, [10,20]]
print list2
print list2[0]
print list2[3][1]

list3=[a,b,2134]
print list3

#����Ϊ����
print list3[-2]
print strings[-1]

print range(1,5)
print range(5)
print range(1,11,2)

#����
list3.append([1,2])
list3.insert(2,"abc")
print list3
list3.extend(list1) 
print list3
print list3.index([1,2])
#print list3.index(13213) #error
list3.remove(1) #remove��һ��1
print list3
list3.pop()
print list3

print len(list3)
print 'abc' in list3 #in������

print list1+list2
print list2*2

#Ƭ�Σ����ַ���һ��������ֻҪ[]����:����ȥƬ����Ȼ���б�,�����б��ǿ���ͨ��[]���޸ģ��ַ��������ԣ�
print list1[0:0],type(list1[0:0])
list4=range(5)
list4[3:4]=[1]
list4[0:0]=[11] #��һ��Ԫ��ǰ����
print list4
del list4[1:3]
print list4

# COW
print "#"
i1=123
i2=123
print id(i1),id(i2) #��ַһ��
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
#��һ��
l1=[1,2]
l2=[1,2]
print id(l1),id(l2)
l2=[2,3,4]
print id(l1),id(l2)

#����
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
#�����˸��Ʋ����Ͳ����Ǳ�����

#clone
lc=la[:]
lc.append(123)
print la

#�б�������ݣ����ô��� ****
from lib.list import listPop
listToPop=[1,2,3,444]
listPop(listToPop)
print "listToPop:",listToPop
#�������ı䣬clone�б�

#�ַ������б��ת��
#split��join
ss="I am a student. Are you?"
ll=string.split(ss)
llDot=string.split(ss,".")
print ll,llDot
print string.join(ll), "\n" ,string.join(llDot,".")
#Ҳ����������
print "------",".".join(llDot)
print "------"," ".join(ll)

#�б�ӳ��
fruits=["apple","orange","pear","banana"]
print [fruit+'s' for fruit in fruits]
print [fruit+'s' for fruit in fruits if len(fruit) != 6]


#���У����б�Ƚ����ƣ�����Ԫ�ص�ֵ�ǹ̶���
tuple1=1,2,3,4,5,6,7
tuple2=(1,2,546,7,8,78,7,)
print type(tuple1),type(tuple2),
print type(('a')),type(('a',)) #һ�����ŵ�����

#һ���ô�:����ֵ
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
#��ֵ�������ߵ�����Ԫ��Ҫһ�£��������������

def swap(a,b):
    return b,a

    
# 0-1�������
import random
print random.random()

#�ֵ�
dict1={"name": "Ben", "age":"28"}
print dict1["name"]
dict1["name"]="guan"
print dict1["name"]


dict={"M":111,"U": 2}
print dict

dictAlias=dict1 #����
dictAlias["name"]="BK"
print dict1["name"]

dict2=dict1.copy() #����

#ɾ�� del dict[key]
#��� dict.clear()
#���� len(dict)

#ϡ�����
matrix = [ [0,0,0,1,0],
            [0,0,0,0,0],
            [0,2,0,0,0],
            [0,0,0,0,0],
            [0,0,0,3,0] ]
print type(matrix) #list

matrixDict = {(0,3): 1, (2, 1): 2, (4, 3): 3}
print matrixDict[2,1]
#print matrixDict[2,3] #error
print matrixDict.get((2,3),0) #�Ҳ�������0

#from fibonacci import fibonacci
#print fibonacci(30) #����

#from fibonacci_improve import fibonacci_improve
#print fibonacci_improve(40) #�ܿ�
#print fibonacci_improve(100) #���ɺܿ�

#�ļ�����
#import os
#print os.getcwd() #����Ŀ¼
#print sys.path[0] #��ǰ�ű���Ŀ¼
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

#��д������ݱ���ԭ����
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
        
    #����
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
���ٰ˳�
�Զ���ʵ��Ϊ�� , ��ֻ������Ϊ��;
�Դ�ӡ��־Ϊ�� , �Ե�������Ϊ��;
�Կո�����Ϊ�� , ���Ʊ�����Ϊ��;
�Ե�Ԫ����Ϊ�� , ���˹�����Ϊ��;

��ģ�鸴��Ϊ�� , �Ը���ճ��Ϊ��;
�Զ�̬Ӧ��Ϊ�� , �Է�֧�ж�Ϊ��;
��PythonicΪ�� , ���������Ϊ��;
���ܽ����Ϊ�� , �Թ������Ϊ��;


Pythonic: 
    http://blog.csdn.net/lanphaday/archive/2008/08/03/2762251.aspx 
    http://faassen.n--tree.net/blog/view/weblog/2005/08/06/0
'''