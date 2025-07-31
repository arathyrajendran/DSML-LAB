import numpy as np

def create_matrix(mc):
    print("\nArray" + str(mc) + " Elements:")
    array_1 = list(map(int, input().split()))

    print("\nArray" + str(mc) + " ROW COLUMN:")
    row, column = map(int, input().split())

    if len(array_1) != (row * column):
        print("\nRow and column size not matching with total elements!! Retry")
        return create_matrix(mc)

    array_1 = np.array(array_1).reshape(row, column)
    print("\nARRAY" + str(mc))
    print(array_1)
    return array_1

# Main execution
matrix = create_matrix(1)
eigen_values, eigen_vectors = np.linalg.eig(matrix)

print("\nE-values:")
print(eigen_values)

print("\nE-vectors:")
print(eigen_vectors)
