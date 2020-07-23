__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

import numpy as np

from easyTemplateLib.Example.Interfaces.interfaceTemplate import InterfaceTemplate
from easyTemplateLib.Example.Calculators.calculator2 import Calculator2


class Interface2(InterfaceTemplate):
    """
    This is a more complex template. Here we need to export_data data,
    transfer it to the calculator (get and calculate) and import data
    from the calculator (set)
    """
    def __init__(self):
        """
        Set up a calculator and a local dict
        """
        self.calculator = Calculator2()
        self._data: dict = {}

    def get_value(self, value_label: str) -> float:
        """
        Method to get a value from the calculator

        :param value_label: parameter name to get
        :type value_label: str
        :return: associated value
        :rtype: float
        """
        self._data = json.loads(self.calculator.export_data())
        return getattr(self._data, value_label, None)

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
            print(f'Interface2: Value of {value_label} set to {value}')
        self._data = json.loads(self.calculator.export_data())
        if value_label in self._data.keys():
            self._data[value_label] = value
        self.calculator.import_data(json.dumps(self._data))

    def fit_func(self, x_array: np.ndarray) -> np.ndarray:
        """
        Function to perform a fit

        :param x_array: points to be calculated at
        :type x_array: np.ndarray
        :return: calculated points
        :rtype: np.ndarray
        """
        return self.calculator.calculate(x_array)
