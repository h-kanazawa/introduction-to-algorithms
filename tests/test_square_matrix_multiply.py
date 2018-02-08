# -*- coding: utf-8 -*-

import numpy as np
from src.square_matrix_multiply import genSquareMatrix, strassen


def test_strassen():
    for n in [2, 4, 8, 16]:
        for k in range(0, 4):
            A = genSquareMatrix(n)
            B = genSquareMatrix(n)

            Cst = strassen(A, B)
            Cnp = np.dot(A, B)

            assert np.allclose(Cst, Cnp)
