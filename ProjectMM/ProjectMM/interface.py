import MatrixC
# main interface file for Project MM matrix multiplier

matrixRowSize = int(input("how many rows(x) for the first matrix: "))
matrixColumnSize = int(input("how many columns(y) for the first matrix: "))

matrixRowSize2 = int(input("how many rows(x) for the second matrix: "))
matrixColumnSize2 = int(input("how many columns(y) for the second matrix: "))

matrix1 = MatrixC.MatrixC(matrixRowSize, matrixColumnSize)
matrix2 = MatrixC.MatrixC(matrixRowSize2, matrixColumnSize2)

"""
for p in range(0, matrixRowSize):
    for q in range(0, matrixColumnSize):
        matrix1[p][q] += q
"""
matrix1.print_mc()
# print(matrix1)

for p in range(0, matrixRowSize):
    for q in range(0, matrixColumnSize):
        print("[Matrix 1]: please enter the values for row ", p, "column ", q)
        matrix1[p][q] = int(input(""))

for p in range(0, matrixRowSize2):
    for q in range(0, matrixColumnSize2):
        print("[Matrix 2]: please enter the values for row ", p, "column ", q)
        matrix2[p][q] = int(input(""))

a = matrix1 * matrix2
a.print_mc()