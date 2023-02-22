#!/usr/bin/false

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractComparator(ABC):
    """ Defines an abstract comparator between a baseline evaluation and """
    """ an alternative """

    @abstractmethod
    @property
    def control_descriptor(self) -> object:
        """ Returns the descriptor of the control object. """
        """ The control object can be seen as set of control variables """
        """ in such a way that they serve as a baseline. """
        return self._control

    @abstractmethod
    @control_descriptor.setter
    def control_descriptor(self, control) -> AbstractComparator:
        """ Modifies the control descriptor and returns self """
        self._control = control
        return self

    @abstractmethod
    @property
    def test_descriptor(self) -> object:
        """ Returns the descriptor of the variable object. """
        """ The variable object is a descriptor of a possible worthwhile """
        """ investment opportunity, which is to be evaluated against the """
        """ baseline. """
        return self._test

    @abstractmethod
    @test_descriptor.setter
    def test_descriptor(self, test) -> AbstractComparator:
        """ Modifies the variable descriptor and returns self """
        self._test = test
        return self
