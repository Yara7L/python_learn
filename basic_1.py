import math

def quadratic(a, b, c):
    x = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    y = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x, y
print(quadratic(1, 2, 1))


def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person('Yara', 24, city='CD', addr='TF')

# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
fib(6)

# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
g = triangles()
n = 0
for t in g:
    print(t)
    n = n + 1
    if n == 10:
        break

from functools import reduce
def add(x,y):
    return x*10+y
print(reduce(add,[1,3,5,7,9]))


#map 和 reduce一起使用
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6}[s]
print(reduce(add,map(char2num,'135')))


#lambda函数进一步简化
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
str2int('135')


def prod(x,y):
    return(x*y)
print(reduce(prod,[3,4,5,6]))

#求素数
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
for n in primes():
    if n<1000:
        print(n)
    else:
        break


#回数，切片
def is_palindrome(n):
    return str(n)==str(n)[::-1]
ooutput=filter(is_palindrome,range(1,1000))
print(list(ooutput))

print(sorted(['bob','about','Zoo'],key=str.lower,reverse=True))

L=[('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_scores(t):
    return t[1]
L2=sorted(L,key=by_name)
L3=sorted(L,key=by_scores,reverse=True)
print(L2)
print(L3)

def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quicksort(left)+middle+quicksort(right)
print(quicksort([3,6,8,10,1,2,1]))

nums=[0,1,2,3,4]
squares=[]
for x in nums:
    squares.append(x**2)
squares_2=[x**3 for x in nums]
print(squares,squares_2)
