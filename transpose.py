import numpy as np

def create_matrix(mc):
    print(f"\nEnter elements for ARRAY {mc} (space-separated):")
    array_1 = list(map(int, input().split()))
    
    print(f"\nEnter number of rows and columns for ARRAY {mc}:")
    row, column = map(int, input().split())
    
    if len(array_1) != row * column:
        print("\n Row and Column size does not match total elements! Retry.\n")
        return create_matrix(mc)
    
    matrix = np.array(array_1).reshape(row, column)
    
    print(f"\n ARRAY {mc}:")
    print(matrix)
    
    print("\n🔁 Transpose:")
    print(matrix.transpose())
    
    return matrix

create_matrix(1)