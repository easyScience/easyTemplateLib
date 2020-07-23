__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

import numpy as np

from easyTemplateLib.Example.Interfaces.interfaceTemplate import InterfaceTemplate
from easyTemplateLib.Example.Calculators.calculator1 import Calculator1


class Interface1(InterfaceTemplate):
    """
    A simple example interface using Calculator1
    """
    def __init__(self):
        # This interface will use calculator1
        self.calculator = Calculator1()

    def get_value(self, value_label: str) -> float:
        """
        Method to get a value from the calculator

        :param value_label: parameter name to get
        :type value_label: str
        :return: associated value
        :rtype: float
        """
        return getattr(self.calculator, value_label, None)

    def set_value(self, value_label: str, value: float):
        """
        Method to set a value from the calculator

        :param value_label: parameter name to get
        :type value_label: str
        :param value: new numeric value
        :type value: float
        :return: None
        :rtype: noneType
        """
        if self._borg.debug:
            print(f'Interface1: Value of {value_label} set to {value}')
        setattr(self.calculator, value_label, value)

    def fit_func(self, x_array: np.ndarray) -> np.ndarray:
        """
        Function to perform a fit

        :param x_array: points to be calculated at
        :type x_array: np.ndarray
        :return: calculated points
        :rtype: np.ndarray
        """
        return self.calculator.calculate(x_array)
