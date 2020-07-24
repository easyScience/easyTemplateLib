__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

import numpy as np


class Calculator1:
    """
    Generic calculator in the style of crysPy
    """
    def __init__(self, m: float = 1, c: float = 0):
        """
        Create a calculator object with m and c

        :param m: gradient
        :type m: float
        :param c: intercept
        :type c: float
        """
        self.m = m
        self.c = c

    def calculate(self, x_array: np.ndarray) -> np.ndarray:
        """
        For a given x calculate the corresponding y

        :param x_array: array of data points to be calculated
        :type x_array: np.ndarray
        :return: points calculated at `x`
        :rtype: np.ndarray
        """
        return self.m * x_array + self.c
