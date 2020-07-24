__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

import numpy as np
from typing import Callable, List
from abc import ABCMeta, abstractmethod

from easyCore import borg
from easyCore.Utils.json import MSONable
from easyCore.Objects.Inferface import InterfaceFactoryTemplate

from Example1.Interfaces import InterfaceTemplate

class InterfaceFactory(InterfaceFactoryTemplate):
    def __init__(self):
        super(InterfaceFactory, self).__init__(InterfaceTemplate._interfaces)

