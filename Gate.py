# Gate class

import numpy as np
import Qubit as q

class Gate:

    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def __add__(self, other):
        return Gate(self.matrix + other.matrix)

    def __sub__(self, other):
        return Gate(self.matrix - other.matrix)

    # Tensor Product
    def __mod__(self, other):
        return Gate(np.kron(self.matrix, other.matrix))

    # Applying Operator via Matrix Multiplication
    def __mul__(self, other):
        if isinstance(other, q.Qubit):
            return q.Qubit(self.matrix.dot(other.components))
        return Gate(np.matmul(self.matrix, other.matrix))

    # Scalar Multiplication
    def __rmul__(self, other):
        return Gate(other * self.matrix)

    def __repr__(self):
        return repr(self.matrix)
