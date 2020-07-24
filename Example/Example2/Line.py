__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

from Example1.interface import InterfaceFactory
from easyCore.Objects.Base import Parameter, BaseObj


class Line(BaseObj):
    """
    Simple descriptor of a line.
    """
    _defaults = [Parameter('m', 1),
                 Parameter('c', 0)]

    def __init__(self, interface_factory: InterfaceFactory = None):
        """
        Create a line and add an interface if requested

        :param interface_factory: interface controller object
        :type interface_factory: InterfaceFactory
        """
        self.interface = interface_factory
        super().__init__(self.__class__.__name__,
                         *self._defaults)
        self._set_interface()

    def _set_interface(self):
        if self.interface:
            # If an interface is given, generate bindings
            for parameter in self.get_parameters():
                name = parameter.name
                self.set_binding(name, self.interface.generate_bindings)

    @property
    def gradient(self):
        if self.interface:
            return self.interface().get_value('m')
        else:
            return self.m.raw_value

    @property
    def intercept(self):
        if self.interface:
            return self.interface().get_value('c')
        else:
            return self.c.raw_value

    def __repr__(self):
        return f'Line: m={self.m}, c={self.c}'