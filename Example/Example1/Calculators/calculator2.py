__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

import json
import numpy as np


class Calculator2:
    """
    Isolated calculator. This calculator can't have values set, it can
    only load/save data and calculate from it. i.e in the style of crysfml
    """
    def __init__(self):
        """
        """
        self._data = {'m': 0,
                      'c': 0}

    def calculate(self, x_array: np.ndarray) -> np.ndarray:
        """
        For a given x calculate the corresponding y

        :param x_array: array of data points to be calculated
        :type x_array: np.ndarray
        :return: points calculated at `x`
        :rtype: np.ndarray
        """
        return self._data['m'] * x_array + self._data['c']

    def export_data(self) -> str:
        return json.dumps(self._data)

    def import_data(self, input_str: str):
        self._data = json.loads(input_str)
