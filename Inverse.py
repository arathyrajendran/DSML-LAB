import numpy as np

def create_matrix(mc):
    while True:
        print("\nArray" + str(mc) + " Elements:")
        try:
            array_1 = list(map(int, input().split()))
            print("\nARRAY " + str(mc) + " ROW COLUMN :")
            row, column = map(int, input().split())

            if len(array_1) != row * column:
                print("\nRow and Column size not matching with total elements! Retry.")
                continue

            matrix = np.array(array_1).reshape(row, column)
            print("\nARRAY " + str(mc))
            print(matrix)

            if row == column:
                try:
                    inverse = np.linalg.inv(matrix)
                    print("\nInverse:")
                    print(inverse)
                except np.linalg.LinAlgError:
                    print("\nMatrix is singular and cannot be inverted.")
            else:
                print("\nMatrix is not square, so inverse can't be computed.")
            return matrix

        except Exception as e:
            print("Error:", e)
            continue
  
