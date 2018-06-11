import numpy as np 

# shape的使用
def shape():
    a = np.array([1, 2, 3, 4])
    print(a.shape)
    print(a)

    b=a.reshape((2,2))
    print(b)
    print(b.shape)

    c=a.reshape((1,-1))
    print(c)
    print(c.shape)

    d=a.reshape((-1,1))
    print(d)
    print(d.shape)