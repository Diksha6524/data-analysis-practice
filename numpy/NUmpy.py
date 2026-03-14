 #numpy: working with array
# storing arrays and matrices, along with a collection of mathematical functions to operate on these data structures.
# 1D ARRAY,2D,3D,4D ETC
#  numpy vs lists
#  fastspeed-numpy
#  as  numpy uses fixed types-
#  stored at one continuous place in memory 
# unlike lists,
# so processes can access and manipulate
# data more efficiently.    
# in numpy array the data stored using less space 
 
# 1d array
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a) # Output: [1 2 3 4 5] 

# 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)    # Output: [[1 2 3]
            #          [4 5 6]]
# DIMENSIONS
print(a.ndim)  # Output: 1      
print(b.ndim)  # Op: 2

# SHAPE
print(a.shape)  # Op: (5,)   (ROWS , COLUMNS)  
print(b.shape)  # Op: (2, 3)

# DATA TYPE
print(a.dtype)  # Op: int64 
print(b.dtype)  # Op: int64

# SPECIFYING DATA TYPE
c= np.array([1, 2, 3, 4, 5], dtype='float32')
print(c)        #Op: [1. 2. 3. 4. 5.]
print(c.dtype)  # Output: float32

# size
print(a.size)  # Op: 5
print(b.size)  # Op: 6
# itemsize
print(a.itemsize)  # Op: 8 
print(b.itemsize)  # Op: 8, each element 8 bytes as int64

# total bytes
print(a.nbytes)  # Op: 40 (5 elements * 8 bytes each)
print(b.nbytes)  # Op: 48 (6 elements * 8 bytes each
# or
print(a.itemsize*a.size) # Op: 40


# accessing or modifying elements
print(a[2])  # Op: 3
b[0, 1] = 10  # [r,c]  
print(b)    # Op: [[ 1 10  3]
            #       [ 4  5  6]]
b[0,-2] = 20
print(b)    # Op: [[ 1 20  3]   
            #       [ 4  5  6]]
# slicing [start:stop:stepsize]
print(a[1:4])  # Op: [2 3 4]
print(b[0, :])  # Op: [20  3] row
print(b[:, 1]) # Op: [20  5] column


# 3D array  
d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(d)    # Op: [[[1 2]               
            #        [3 4]]
            #       [[5 6]
            #        [7 8]]]
# get specific element
print(d[1, 0, 1])  # Op: 6
# modify specific element
d[0, 1, 1] = 10 
print(d)    # Op: [[[ 1  2]
            #        [ 3 10]]
            #       [[ 5  6]
            #        [ 7  8]]]
# slicing
print(d[:, 1, :])  # Op: [[ 3 10]
                  #       [ 7  8]]
d[:, 1, :] = [[2, 3], [4, 5]]
print(d)    # Op: [[[1 2]
            #        [2 3]]
            #       [[5 6]
            #        [4 5]]]




# creating arrays with specific values
# zeros array
z = np.zeros((2, 3,3))  # 2 rows ,3 columns ,3 depth    
print(z)   # Op: [[[0. 0. 0.]       
            #        [0. 0. 0.]
            #        [0. 0. 0.]]
            #       [[0. 0. 0.]
            #        [0. 0. 0.]
            #        [0. 0. 0.]]]

# ones array
o = np.ones((3, 2),dtype='int16')  
print(o)  # Op: [[1 1]      
            #    [1 1]
             #   [1 1]]
# full array
f = np.full((2, 4), 10)      
print(f)    # Op: [[10 10 10 10]
            #        [10 10 10 10]]    
# full like
f = np.full_like(o, 7) 
print(f)   # Op: [[7 7]
            #        [7 7]
            #        [7 7]]
# random array
r = np.random.rand(2, 3)        
print(r)    # Op: [[0.5488135  0.71518937 0.60276338]
            #        [0.54488318 0.4236548  0.64589411]] 
i = np.random.randint(4, size=(3, 4))       # random integers between 0-4 ie0,1,2,3             can aslo write 4,10 to get between 4-9
print(i)   # Op: [[3 0 3 3] 
              #       [2 0 1 0]
                #       [3 3 0 1]]
# identity matrix
iden = np.eye(3)        
print(iden)   # Op: [[1. 0.]    
                #       [0. 1.]
                #       [0. 0.]]    
# repeat array
arr = np.array([[1, 2, 3]])
rep = np.repeat(arr, 3, axis=0)  # (array, number of times, axis), axis in the sense repetitions should be in rows or columns
print(rep)   # Op: [[1 2 3] 
            #       [1 2 3]
            #       [1 2 3]]
# axis=0 for rows, axis=1 for columns
r = np.repeat(arr, 3, axis=1)
print(r)  # Op: [[1 1 1 2 2 2 3 3 3]]  
 

# lets mke matrix

mat=np.ones((5,5))
# print(mat) 
mat[1:4,1:4]=0
# print(mat)
mat[2:3,2:3]=9
print(mat) 
# or
mat=np.ones((5,5))
print(mat)

z=np.zeros((3,3))
z[1,1]=9
print(z)

mat[1:4,1:4]=z
print(mat)  

# when copying one array into other ,the changes made in one array will also reflect in other array
arr1 = np.array([1, 2, 3])
arr2 = arr1  # Both arr1 and arr2 point to the same array in memory
arr2[0] = 10  
print(arr1)  # Output: [10  2  3]
print(arr2)  # Output: [10  2  3]
# aviod this ,use .copy()
arr3 = arr1.copy()  # Creates a new array in memory
arr3[0] = 20  
print(arr1)  # Output: [10  2  3] 
print(arr3)  # Output: [20  2  3]


# MATHEMATICAL OPERATIONS
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# element-wise addition
addition=arr1+10
print(addition)  # Op: [11 12 13]
add = arr1 + arr2
print(add)  # Op: [5 7 9]
add2 = np.add(arr1, arr2)
print(add2)  # Op: [5 7 9]
# element-wise subtraction  
sub = arr2 - arr1
print(sub)  # Op: [3 3 3]
sub2 = np.subtract(arr2, arr1)
print(sub2)  # Op: [3 3 3]
# element-wise multiplication
mul = arr1 * arr2
print(mul)  # Op: [ 4 10 18]
mul2 = np.multiply(arr1, arr2)
print(mul2)  # Op: [ 4 10 18]
# element-wise division
div = arr2 / arr1
print(div)  # Op: [4.  2.5 2. ]
div2 = np.divide(arr2, arr1)
print(div2)  # Op: [4.  2.5 2. ]
# element-wise square root
sqrt = np.sqrt(arr1)
print(sqrt)  # Op: [1. 1.41421356 1.73205081]
#  exponentiation
expo=arr1**2
print(expo)  # Op: [1 4 9]  

expo2 = np.power(arr1, 2)
print(expo2)  # Op: [1 4 9] 
# dot product
dot = np.dot(arr1, arr2)
print(dot)  # Op: 32 (1*4 + 2*5 + 3*6)
# or  
dot2 = arr1.dot(arr2)
print(dot2)  # Op: 32
# sin
sinA = np.sin(arr1)
print(sinA)  # Op: [0.84147098 0.90929743 0.14112001]
# cos
cosA = np.cos(arr1)
print(cosA)  # Op: [0.54030231 -0.41614684 -0.9899925 ]

# linear algebra-no element wise operations
A = np.ones((2, 2))
B = np.array([[5, 6], [7, 8]])
c=np.ones((2,4))
# matrix multiplication
mat_mul = A @ B
print(mat_mul)  # Op: [[12. 14.]
                #       [12. 14.]]
mat_mul2 = A@c
print(mat_mul2)  # Op: [[4. 4. 4. 4.]
                #       [4. 4. 4. 4.]]  2 BY 4 MATRIX
mat_mul3 = np.matmul(A, B)
print(mat_mul3)  # Op: [[12. 14.]
                #       [12. 14.]]
# matrix determinant
D=np.identity(3)
det_D = np.linalg.det(D) 
print(det_D)  # Op: 1.0

#statistics
S=np.random.randint(1, 10, size=(3, 4))
print(S)
# op [[8 4 9 2]
#  [1 9 1 9]
#  [1 8 9 5]]
# Max
MAx = np.max(S)
print(MAx)  # Op: 9
mAx=np.max(S,axis=0) #column wise
print(mAx)  # Op: [8 9 9 9]
mAx2=np.max(S,axis=1) #row wise
print(mAx2)  # Op: [9 9 9]

# Min
Min = np.min(S)
print(Min)  # Op: 1
# Sum
Sum = np.sum(S)
print(Sum)  # Op: 65

# Mean
Mean = np.mean(S)
print(Mean)  # Op: 5.416666666666667

# reorganizing arrays
Before = np.array([[1, 2, 3], [4, 5, 6]])
print(Before)  # Op: [[1 2 3] 
                #       [4 5 6]]
print(Before.shape)  # Op: (2, 3)
# Reshaping
After = Before.reshape((3, 2))
print(After)  # Op: [[1 2] 
             #       [3 4]
             #       [5 6]]


# vertical stacking
V = np.array([[1, 2, 3], [4, 5, 6]])
v=np.ones((1,3))
v_stack = np.vstack((V, v))
print(v_stack)  # Op: [[1. 2. 3.]
                #       [4. 5. 6.]
                #       [1. 1. 1.]] 
# horizontal stacking
H = np.array([[1, 2, 3], [4, 5, 6]])
h=np.random.rand(2,1)
print(h)
# Op: [[0.5488135 ] 
#       [0.71518937]]
h_stack = np.hstack((H, h,H))
print(h_stack)  # Op: [[1.         2.         3.         0.5488135  1.         2.         3.        ]
                #       [4.         5.         6.         0.71518937 4.         5.         6.        ]]




# loading files without pandas
# data in text file
d1=np.genfromtxt('num.txt', delimiter=',')  #  we can adjust delimiter as needed
print(d1)
# or
data1 = np.loadtxt('num.txt', delimiter=',')  # we can adjust delimiter as needed
print(data1)
D1=data1.astype('int32')
print(D1)              


# advanced indexing and slicing and boolean masking
d1>5 # returns boolean array
bool_arr=d1>5
print(bool_arr) # Op: [False False False False  True  True  True False  True  True False False etc
# or
d1[d1>5] # returns elements greater than 5
print(d1[d1>5]) # Op: [6. 7. 9. 7. 6. 7. 9. 6. 9.]
# multiple conditions 
d1[(d1>2) & (d1<7)] # element gtr then 2 n lesser then 7
    #  in tgis we can use axis also
np.any(d1>8, axis=0) # axis=0 c, axis=1  r
    # we can use boolean expressions too 


# we can index with a list in numpy
Ar=np.array([10,20,30,40,50])
indices=[0,2,4]
print(Ar[indices]) # Op: [10 30 50] or we can type Ar[0,2,4]



# slicing
#lets consider matrix
# [[1 2 3 4 5]
  #  [6 7 8 9 10]
  #  [11 12 13 14 15]
  # [16 17 18 19 20]
  # [21 22 23 24 25]
  #  [26 27 28 29 30]]
   
  #  we hv to  find 11 12
  #                  16 17 block

mat=np.arange(1,31).reshape(6,5)
print(mat)
Slice=mat[2:4,0:2]
print(Slice) # Op: [[11 12]
             #       [16 17]]

# now for  2,8,14,20
Sl=mat[[0,1,2,3],[1,2,3,4]]     
# [0,1,2,3] row indices   0TH ROW FOR 2,1ST ROW FOR 8 N SO ON
# [1,2,3,4] column indices 1ST C FOR 2 N SO ON
print(Sl)  # Op: [ 2  8 14 20]

# FOR 4,5
#     24,25
#     29,30
SL1=mat[0:1,3:5]
SL2=mat[4:6,3:5]  
print(SL1)
print(SL2)
#  now we can use vstack
Final=np.vstack((SL1,SL2))
print(Final) 
# Op: [[ 4  5]
            #       [24 25]
            #       [29 30]]


# practice question
# create a 5x5 matrix with values ranging from 1 to 25
matrix = np.arange(1, 26).reshape(5, 5)
# create numpy array 1 to 20
A1to20=np.array(np.arange(1,21))
print(A1to20)
# reshape it to 4 into 5
A1to20=A1to20.reshape(4,5)
print(A1to20)
# op :[[ 1  2  3  4  5]
        # [ 6  7  8  9 10]  
        # [11 12 13 14 15]
        # [16 17 18 19 20]]

# slice
 # first 2 rows
# last 2 columns
new=A1to20[0:2,3:]
print(new)

