import numpy as np

def create_matrix(mc):
    print("\nArray" + str(mc) + " Elements (space-separated):")
    array_1 = list(map(int, input().split()))

    print("\nArray" + str(mc) + " ROW COLUMN:")
    row, column = map(int, input().split())

    if len(array_1) != (row * column):
        print("\nRow and column size not matching with total elements!! Retry")
        return create_matrix(mc)

    array_1 = np.array(array_1).reshape(row, column)
    print("\nMatrix:")
    print(array_1)

    if row == column:
        print("\nDeterminant:")
        print(np.linalg.det(array_1))
    else:
        print("\nDeterminant is not defined for non-square matrices.")

    return array_1

# Example usage
create_matrix(1)