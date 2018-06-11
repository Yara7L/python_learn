import numpy as np 


a=[[1,2,3],[4,5,6]]
print(type(a))
print(a)

# stack()函数会先把参数arrays中的每个元素变成numpy的数组

print("增加一个维度，新维度的下标为0")
c_0=np.stack(a,axis=0)
print(type(c_0))
print(c_0)

print("增加一个维度，新维度的下标为1")
c_1=np.stack(a,axis=1)
print(type(c_1))
print(c_1)

# a=[1,2,3,4]
# b=[5,6,7,8]
# c=[9,10,11,12]
# print(type(a))
# print("a=",a)
# print("b=",b)
# print("c=",c)

# print("增加一维，新维度的下标为0")
# d=np.stack((a,b,c),axis=0)
# print(d)

# print("增加一维，新维度的下标为1")
# d=np.stack((a,b,c),axis=1)
# print(d)

a=[[1,2,3],
   [1,2,3]]
b=[[1,2,3],
   [4,5,6]]
c=[[1,2,3],
   [7,8,9]]
print("a=",a)
print("b=",b)
print("c=",c)

print("增加一维，新维度的下标为0")
d=np.stack((a,b,c),axis=0)
print(d.shape,d)

print("增加一维，新维度的下标为1")
d=np.stack((a,b,c),axis=1)
print(d.shape,d)
print("增加一维，新维度的下标为2")
d=np.stack((a,b,c),axis=2)
print(d.shape,d)

# 水平堆叠
a=[1,2,3]
b=[4,5,6]
h=np.hstack((a,b))
v=np.vstack((a,b))
print(h.shape,h)
print(v.shape,v)

# 垂直堆叠
a=[[1],[2],[3]]
b=[[1],[2],[3]]
c=[[1],[2],[3]]
d=[[1],[2],[3]]
h_=np.hstack((a,b,c,d))
v_=np.vstack((a,b,c,d))
print(h_.shape,h_)
print(v_.shape,v_)


