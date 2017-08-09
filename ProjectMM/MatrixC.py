# file for the matrix class


class MatrixC:
    # initialization
    def __init__(self, r, c):
        self.data = [[0 for q in range(0, c)]for p in range(0, r)]

    # accessor
    def __getitem__(self, r):
        return self.data[r]

    # setter
    def __setitem__(self, key, value):
        self.data[[key[0]][key[1]]] = value

    # print function
    def print_mc(self):
        for i in range(0, len(self.data)):
            print(self.data[i])