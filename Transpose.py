
import numpy as np

def create_matrix(mc):
    while True:
        try:
            print(f"\nEnter number of rows and columns for ARRAY {mc}:")
            row, column = map(int, input().split())
            print(f"\nEnter {row * column} elements for ARRAY {mc} (space-separated):")
            array_1 = list(map(int, input().split()))
            if len(array_1) != row * column:
                print(f"\n Row x Column size ({row}x{column}={row*column}) does not match number of elements ({len(array_1)}). Please retry.\n")
                continue
            matrix = np.array(array_1).reshape(row, column)
            print(f"\n ARRAY {mc}:")
            print(matrix)
            print("\n🔁 Transpose:")
            print(matrix.transpose())
            return matrix
        except ValueError:
            print("\n Invalid input. Please enter integers only.\n")

if __name__ == "__main__":
    create_matrix(1)
