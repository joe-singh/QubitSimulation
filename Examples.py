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
#print(ket == plus % plus % minus)

# 3 Qubit Grover Algorithm, correct answer is |110>

O = g.Gate([
    [1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,-1,0],
    [0,0,0,0,0,0,0,1],
])

J = g.Gate([
    [-1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,1],
])

answer = q.Qubit([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])

def grover(Ket):

    Had = H % H % H
    Ket = Had * Ket
    Ket = O * Ket
    Ket = Had * Ket
    Ket = J * Ket
    Ket = Had * Ket

    Ket.measure()
    return Ket

answer = q.Qubit([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])

counter = 0
for i in range(1000):
    ket = plus % plus % plus
    result = grover(ket)
    if result != answer:
        counter += 1

print(counter)

# Gives wrong answer 0 times for 3 tries, 23 times for 100 tries, and 226 times for 1000 tries. 

