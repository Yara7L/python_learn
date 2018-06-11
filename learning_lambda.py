from functools import reduce
# lambda,匿名函数，可以省去定义函数的过程，让代码更加精简,lambda 参数：返回函数值，传给函数的处理的变量值
print('========map one params========')
li=[1,2,3]
new_list=map(lambda a: a+1, li)
for i in new_list:
    print(i)

print('========map two params========')
li_2=[1,2,3]
new_list=map(lambda a, b: a+b, li, li_2)
for i in new_list:
    print(i)

print('=========filter=========')
new_list=filter(lambda arg: arg>1, li)
for i in new_list:
    print(i)

print('==========reduce=========')
li_3=[2,3,4]
result=reduce(lambda arg1, arg2: arg1+arg2, li_3)
print(result)


