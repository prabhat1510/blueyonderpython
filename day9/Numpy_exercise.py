import numpy as np

print("****************1. Create 3x4 array, ex1, with values (2,3,5,7),(1,9,24,15),(5,12,19,21).*****")

ex1=np.array([ [2,3,5,7],[1,9,24,15],[5,12,19,21]  ])
print(ex1)
print("****************2. Find the number of values in the array.************")
print(ex1.size)
print("****************3. Create a 3X4 array,ex2, with values 0,  Add 5 to ex2.**************")
ex2 = np.zeros((3,4))
print(ex2)
ex2 = ex2+5
print(ex2)
print("****************4. Change ex1 to 4X3 array************")
ex1.resize(4,3)
print(ex1)
print("***********5. Extract the 3rd element in the 2nd row, first element in second row, third element in first row from ex1.*********")
print(ex1[1, 2]) #3rd element in the 2nd row,
print(ex1[1, 0]) #first element in second row
print(ex1[0, 2]) #third element in first row
print("********6. Find the row-wise and column-wise sum of ex1*************")
#column  wise
print(np.sum(ex1, axis=0))
#row wise 
print(np.sum(ex1, axis=1))

print("****************7. convert the 2D array ex1 to 1D array and store in ex3.******************")
print(ex1.ravel())
print(ex1)


print("*****************8. Find the min, max and sum of ex3.*******************")
print("Min: ", np.min(ex1))
print("Max: ", np.max(ex1))
print("Sum: ", np.sum(ex1))

print("****************9. Create an array ex4 with values 2,25 with a step of 2.********************")
ex4 = np.arange(2, 25, 2)
print(ex4)

print("**************10. Create 3x4 array, ar1, with values (1,2,3,5),(19,24,15,10),(15,22,9,21), Stack ex1 and ar1 horizontally and vertically. *************")
ar1 = np.array([[1,2,3,5],[19,24,15,10],[15,22,9,21]])
print(ar1)
ex1=np.array([ [2,3,5,7],[1,9,24,15],[5,12,19,21]  ])
print("Horizontally  Concatenated:",np.hstack((ar1,ex1)))
print("Vertically Concatenated:",np.vstack((ar1,ex1)))

