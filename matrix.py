import numpy as np 

# create the matrix
def get_matrix():
    A=np.random.rand(4,4)
    print(A)
    return A

def get_special_matrix(A):

    # determinant
    det=np.linalg.det(A)
    print("\ndeterminant is:%f \n"%det)

    # transpose
    trans=A.transpose()   #  trans=A.T
    print("transpose is:")
    print(trans)

    # inverse
    inv=np.linalg.inv(A)
    print("\ninverse is:")
    print(trans)

    # eigen values, eigen vectors
    values,vectors=np.linalg.eig(A)
    print("\neigen values is:")
    print(values)
    print("\neigen vectors is:")
    print(vectors)

if __name__=='__main__':
    A=get_matrix()
    get_special_matrix(A)