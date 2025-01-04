import numpy as np # type: ignore

row=int(input("Enter number of rows:"))
col=int(input("Enter number of cols:"))
shape_mat=(row,col)

arr1=np.empty(shape_mat,dtype=int)
arr2=np.empty(shape_mat,dtype=int)
print(arr1.shape)

print("Enter values for first Matrix :")
for x in range(row):
    for y in range(col):
        val=int(input("Enter a number :"))
        arr1[x,y]=val
print("First Matrix is :\n",arr1)

print("Enter values for Second Matrix :")
for x in range(row):
    for y in range(col):
        val=int(input("Enter a number :"))
        arr2[x,y]=val
print("Second Matrix is :\n",arr2)

add=arr1+arr2
print("Matrix Addition :\n",add)

mul=np.matmul(arr1,arr2)
print("Matrix Multiplication :\n",mul)
