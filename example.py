__author__ = 'github.com/wardsimon'
__version__ = '0.0.1'

import numpy as np

from easyCore.Fitting.Fitting import Fitter

from easyTemplateLib.Example.interface import InterfaceFactory
from easyTemplateLib.Example.interface import Line

# This is a much more complex case where we have calculators, interfaces, interface factory and an
# inherited object (from `BaseObj`). In this case the Line class is available with/without an interface
# With an interface it connects to one of the calculator interfaces. This calculator interface then translates
# interface commands to calculator specific commands


interface = InterfaceFactory()
line = Line(interface_factory=interface)
f = Fitter(line, interface.fit_func)

x = np.array([1, 2, 3])
y = 2*x - 1

f_res = f.fit(x, y)

print('\n######### Interface 1 #########\n')
print(f_res)
print(line)

# Now lets change fitting engine
f.switch_engine('bumps')

# Reset the values so we don't cheat
line.m = 1
line.c = 0

f_res = f.fit(x, y, weights=0.1*np.ones_like(x))

print('\n######### bumps fitting #########\n')
print(f_res)
print(line)
