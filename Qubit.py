# Qubit class

import numpy as np


class Qubit:

    def __init__(self, components):
        self.components = np.array(components)

    # Qubit norm
    @property
    def norm(self):
        return np.linalg.norm(self.components)

    # Normalise Qubit
    def normalise(self):
        normalised_components = (1/self.norm)*self.components
        return Qubit(normalised_components)

    # Adding Qubits
    def __add__(self, other):
        return Qubit(self.components + other.components)

    # Subtracting Qubits
    def __sub__(self, other):
        return Qubit(self.components - other.components)

    # Inner Product of Qubits
    def __mul__(self, other):
        return np.inner(self.components.conj(), other.components)

    # Scaling Qubit by Scalar
    def __rmul__(self, other):
        return Qubit(self.components * other)

    # Tensor Product of Qubits
    def __mod__(self, other):
        new_components = np.kron(self.components, other.components)
        return Qubit(new_components)

    # String representation of Qubit
    def __repr__(self):
        return repr(self.components.tolist())

    # Equality between qubits. Compensates for floating point error
    def __eq__(self, other):
        assert isinstance(other, Qubit)
        comparison = (self.components - other.components).tolist()
        for num in comparison:
            if np.abs(num.imag) > 0.000001 or np.abs(num.real) > 0.000001:
                return False
        return True

    # Measurement of Qubit, enforces state vector collapse into
    # basis state
    def measure(self):
        num_of_components = self.components.shape[0]
        probability = np.array([np.absolute(self.components[i])**2 for i in range(num_of_components)])
        index = np.random.choice(np.arange(0, num_of_components), p=probability)

        new_components = np.zeros(num_of_components)
        new_components[index] = 1
        self.components = new_components