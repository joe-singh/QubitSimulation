# test file

import Qubit as q
import Gate as g
import numpy as np

plus = q.Qubit([1,0])
minus = q.Qubit([0,1])

def phase_shift(phase):
    return g.Gate([[1,0],[0, complex(np.cos(phase), np.sin(phase))]])

H = (2**(-.5))*g.Gate([[1,1],[1,-1]])
I = g.Gate([[1,0], [0,1]])
R_PI = phase_shift(np.pi)

# Computation 1, acting on |000>,  second qubit Hadamard'd

ket = plus % plus % plus
gate = H % H % H

ket = gate * ket

# Computation 2, acting |000> third qubit
ket = plus % plus % plus

gate_1 = I % I % H
gate_2 = I % I % R_PI
gate_3 = gate_1

ket = gate_3 * gate_2 * gate_1 * ket
print(ket == plus % plus % minus)