__author__ = 'github.com/wardsimon'
__version__ = '0.0.1'

try:
    from Example1.Interfaces.interface1 import Interface1  # noqa: F401
except ImportError:
    # TODO make this a proper message (use logging?)
    print('interface1 is not installed')
try:
    from Example1.Interfaces.interface2 import Interface2  # noqa: F401
except ImportError:
    # TODO make this a proper message (use logging?)
    print('interface2 is not installed')

from Example1.Interfaces.interfaceTemplate import InterfaceTemplate

#interfaces = InterfaceTemplate._interfaces
