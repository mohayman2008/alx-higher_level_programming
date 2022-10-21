#!/usr/bin/python3
"""This module contains the definition of lazy_matrix_mul()
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using NumPy"""

    m_a, m_b = (np.array(m_a), np.array(m_b))

    result = np.matmul(m_a, m_b)
    return result
