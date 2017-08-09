# file for the matrix class


class MatrixC:
    # initialization
    def __init__(self, r, c):
        self.data = [[0 for q in range(0, c)]for p in range(0, r)]
        self.r = r
        self.c = c

    # accessor
    def __getitem__(self, r):
        return self.data[r]

    # setter
    def __setitem__(self, key, value):
        self.data[[key[0]][key[1]]] = value

    # multiply two matrices together
    def __mul__(self, other):
        if self.c != other.r: return print("Error: incompatible size of matrices output not defined.")
        matrixA = MatrixC(self.r, other.c)
        # grab the row of self and column
        for i in range(0, self.r):
            # for every element in the row
            for j in range(0, other.c):
                sum = 0
                for k in range(0, self.c):
                    sum += self.data[i][k] * other.data[k][j]
                matrixA[i][j] = sum
        return matrixA

    # print function
    def print_mc(self):
        for i in range(0, len(self.data)):
            print(self.data[i])