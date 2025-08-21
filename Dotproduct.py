import numpy as np

def create_matrix(mc):
    print("\nArray" + str(mc) + " Elements:")
    array_1 = map(int, input().split())
    array_1 = np.array(list(array_1))
    
    print("\nArray" + str(mc) + " Row and Column:")
    row, column = map(int, input().split())

    if len(array_1) != (row * column):
        print("\nRow and column size not matching with total elements!! Retry")
        return create_matrix(mc)
    
    array_1 = array_1.reshape(row, column)
    print("\nARRAY" + str(mc))
    print(array_1)
    return array_1

arr1 = create_matrix(1)
arr2 = create_matrix(2)

if arr1.shape == arr2.shape:
    print("\nDot Product")
    print(np.dot(arr1, arr2.T)) 
else:
    print("\nDimensions not matching!")
