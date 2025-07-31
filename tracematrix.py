import numpy as np

def create_matrix(mc):
    while True:
        print("\nArray" + str(mc) + " Elements:")
        try:
            array_1 = list(map(int, input().split()))
            print("\nARRAY " + str(mc) + " ROW COLUMN :")
            row, column = map(int, input().split())

            if len(array_1) != row * column:
                print("\nRow and Column size not matching with total elements! Retry.\n")
                continue

            matrix = np.array(array_1).reshape(row, column)
            print("\nARRAY " + str(mc))
            print(matrix)

            if row == column:
                print("\nTrace:")
                print(np.trace(matrix))  # or matrix.trace()
            else:
                print("\nMatrix is not square. Trace not available.")
            return matrix

        except Exception as e:
            print("Error:", e)
            continue

# Example usage
create_matrix(1)