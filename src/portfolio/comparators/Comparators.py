#!/usr/bin/false

import logging
from __future__ import annotations
from abc import ABC, abstractmethod

from . import AbstractCommand
from . import Series

class AbstractComparator(ABC):
    """ Defines an abstract comparator between a baseline evaluation and """
    """ an alternative """

    @abstractmethod
    @property
    def control(self) -> object:
        """ Returns the descriptor of the control object. """
        """ The control object can be seen as set of control variables """
        """ in such a way that they serve as a baseline. """
        return self._control

    @abstractmethod
    @property
    def control(self, control) -> AbstractComparator:
        """ Modifies the control descriptor and returns self """
        self._control = control
        return self

    def variable(self) -> object:
        """ Returns the descriptor of the variable object. """
        """ The variable object is a descriptor of a possible worthwhile """
        """ investment opportunity, which is to be evaluated against the """
        """ baseline. """
        return self._variable

    def variable(self, variable) -> AbstractComparator:
        """ Modifies the variable descriptor and returns self """
        self._variable = variable
        return self


class EvaluateSecurityCommand(AbstractCommand):
    """

    """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def evaluate(security: AbstractSecurity,
                 time_period: AbstractTimePeriod) -> AbstractTimeSeries:
        """ Evaluates the per """
        pass
