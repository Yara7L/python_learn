from pandas import DataFrame
# df=DataFrame()
# df['t']=[x for x in range(10)]
# df['t-1']=df['t'].shift(1)
# df['t+1']=df['t'].shift(-1)
# print(df)
'''
# start,end,delta
a={1,2,3,4,5,6}
b=[1,2,3,4,5,6]
c=[[1,2,3],[4,5,6]]
print(b[::2])
print(b[::-2])
# [from:to],to=max(from+1,to)  
b[2:0]=[100]
print(b)
b=[1,2,3,4,5,6]
b[2:1]=[100]
print(b)


import numpy as np  
  
# sigmoid function  
def nonlin(x,deriv=False):  
    if(deriv==True):  
        return x*(1-x)  
    return 1/(1+np.exp(-x))  
      
# input dataset  
X = np.array([  [0,0,1],  
                [0,1,1],  
                [1,0,1],  
                [1,1,1] ])  
      
# output dataset              
y = np.array([[0,0,1,1]]).T  
  
# seed random numbers to make calculation  
# deterministic (just a good practice)  
np.random.seed(1)  
  
# initialize weights randomly with mean 0  
syn0 = 2*np.random.random((3,1)) - 1  
  
for iter in range(10000):  
    # forward propagation  
    l0 = X  
    l1 = nonlin(np.dot(l0,syn0))  
  
    # how much did we miss?  
    l1_error = y - l1  
  
    # multiply how much we missed by the   
    # slope of the sigmoid at the values in l1  
    l1_delta = l1_error * nonlin(l1,True)  
  
    # update weights  
    syn0 += np.dot(l0.T,l1_delta)  
  
print ("Output After Training:"  )
print (l1)  
'''





'''
import numpy as np  
  
def nonlin(x,deriv=False):  
    if(deriv==True):  
        return x*(1-x)  
  
    return 1/(1+np.exp(-x))  
      
X = np.array([[0,0,1],  
            [0,1,1],  
            [1,0,1],  
            [1,1,1]])  
                  
y = np.array([[0],  
            [1],  
            [1],  
            [0]])  
  
np.random.seed(1)  
  
# randomly initialize our weights with mean 0  
syn0 = 2*np.random.random((3,4)) - 1  
syn1 = 2*np.random.random((4,1)) - 1  
  
for j in range(60000):  
  
    # Feed forward through layers 0, 1, and 2  
    l0 = X  
    l1 = nonlin(np.dot(l0,syn0))  
    l2 = nonlin(np.dot(l1,syn1))  
  
    # how much did we miss the target value?  
    l2_error = y - l2  
      
    if (j% 10000) == 0:  
        print ("Error:" + str(np.mean(np.abs(l2_error))))  
          
    # in what direction is the target value?  
    # were we really sure? if so, don't change too much.  
    l2_delta = l2_error*nonlin(l2,deriv=True)  
  
    # how much did each l1 value contribute to the l2 error (according to the weights)?  
    l1_error = l2_delta.dot(syn1.T)  
      
    # in what direction is the target l1?  
    # were we really sure? if so, don't change too much.  
    l1_delta = l1_error * nonlin(l1,deriv=True)  
  
    syn1 += l1.T.dot(l2_delta)  
    syn0 += l0.T.dot(l1_delta)  
'''

'''
import numpy as np 
arr=np.arange(12).reshape((3,4))
print(arr)
print(arr[:,0])
print(arr[:,1])

X=np.array([[0,0,0],[1,0,1],[1,0,0],[1,1,0]]).T
print(X)

X_mean=np.mean(X,1)
print(X_mean)

E=np.zeros([len(X),len(X)])

for i in range(len(X)):
    for j in range(i,len(X)):
        E[j,i]=E[i,j]=(X[i]-X_mean[i]).dot(X[j]-X_mean[j])/len(X[i])
print(E)

print(np.cov(X, bias=1))
print(np.cov(X))
'''

# import multiprocessing
# import time

# def func(msg):
#     for i in range(3):
#         print(msg)
#         time.sleep(1)

# def func_2(msg):
#     for i in range(3):
#         print(msg)
#         time.sleep(1)
#     return "done"+msg

# if __name__=="__main__":

#     # p = multiprocessing.Process(target=func, args=("hello", ))
#     # p.start()
#     # p.join()
#     # print("Sub-process done")

#     pool = multiprocessing.Pool(processes=4)
#     for i in range(10):
#         msg = "hello %d" %(i)
#         pool.apply_async(func, (msg, ))
#     pool.close()
#     pool.join()
#     print ("Sub-process(es) done.")


    # pool = multiprocessing.Pool(processes=4)
    # result = []
    # for i in range(10):
    #     msg = "hello %d" %(i)
    #     result.append(pool.apply_async(func, (msg, )))
    # pool.close()
    # pool.join()
    # for res in result:
    #     print(res.get())
    # print("Sub-process(es) done.")



import tensorflow as tf 
x=tf.Variable([[1.,2.],[3.,4.]])
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(tf.reduce_mean(x).eval())
    print(tf.reduce_mean(x,0).eval())
    print(tf.reduce_mean(x,1).eval())