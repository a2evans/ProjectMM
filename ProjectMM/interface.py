import MatrixC
# main interface file for Project MM matrix multiplier

matrixColumnSize = int(input("how many rows(x) for the first matrix: "))
matrixRowSize = int(input("how many columns(y) for the first matrix: "))

matrix1 = MatrixC.MatrixC(matrixRowSize, matrixColumnSize)

for p in range(0, matrixRowSize):
    for q in range(0, matrixColumnSize):
        matrix1[p][q] += q

matrix1.print_mc()
# print(matrix1)

for p in range(0, matrixRowSize):
    for q in range(0, matrixColumnSize):
        print("please enter the values for row ", p, "column ", q)
        matrix1[p][q] = int(input(""))


matrix1.print_mc()