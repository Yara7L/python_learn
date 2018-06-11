# -*- coding: utf-8 -*-

'a test modle'
__author__='LJ'

import sys
#系统中的元素
def test():
    args=sys.argv
    if len(args)==1:
        print('Hello,world!')
    elif len(args)==2:
        print('Hello,$s!' % args[1])
    else:
        print('Too many arguments')
if __name__=='__main__':
    test()

test()

#变量public,private
def _private_1(name):
    return 'Hello,%s' % name
def _private_2(name):
    return 'Hi,%s' % name
def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)
print(greeting('ABC'))

class Student(object):
    age=22
    # __变为私有变量，只能内部访问，（_Student__name来访问__name，不建议）
    def __init__(self,name,score):
        self.__name=name
        self.score=score
    def get_name(self):
        return self.__name
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
#bart=Student('A',10)
#bart.print_score()
s=Student('A',100)
s.city='CD'
print(s.age,s.city)


class Teacher_1(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be interge')
        if value<0 or value>100:
            raise ValueError('score must between 0~100')
        self._score=value
class Teacher_2(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be interge')
        if value<0 or value>100:
            raise ValueError('score must be between 0~100')
        self._score=value


# 继承，多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    pass
dog=Dog()
dog.run()
cat=Cat()
cat.run()


# 给实例绑定方法，给类绑定方法
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
s.set_age = MethodType(set_age, s, Student) #实例
Student.set_score = MethodType(set_score, None, Student) #类

# 来限制该class能添加的属性，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
class Student(object):
    __slots__ = ('name', 'age') 


# @property装饰器把一个方法变成属性调用。只定义getter方法，不定义setter方法就是一个只读属性
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
        return self._height*self._width
s=Screen()
s.width=1048
s.height=768
print(s.resolution)


# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。Mixin是给一个类增加多个功能，


# 定制类
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100:
            raise StopIteration()
        return self.a
class Fib_1(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                 a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L    
f=Fib_1()
print(f[10])
print(f[:10:2])


# type()函数既可以返回一个对象的类型，又可以创建出新的类型。
# 先定义metaclass，就可以创建类，最后创建实例


class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
print(Chain().status.user.timeline.list)



class Tree(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('My name is %s' % self.name)
s=Tree('High')
s()

from enum import Enum,unique
Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6


# 处理异常
try:
    print('try..')
    r=10/2
    print('result:',r)
except ZeroDivisionError as e :
    print('except:',e)
finally:
    print('finally...')
print('END')

# 单元测试
'''
class Dict(dict):
    # Simple dict but also support access as x.y style.
    # >>> d1 = Dict()
    # >>> d1['x'] = 100
    # >>> d1.x
    # 100
    # >>> d1.y = 200
    # >>> d1['y']
    # 200
    # >>> d2 = Dict(a=1, b=2, c='3')
    # >>> d2.c
    # '3'
    # >>> d2['empty']
    # Traceback (most recent call last):
    #     ...
    # KeyError: 'empty'
    # >>> d2.empty
    # Traceback (most recent call last):
    #     ...
    # AttributeError: 'Dict' object has no attribute 'empty'
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()
'''