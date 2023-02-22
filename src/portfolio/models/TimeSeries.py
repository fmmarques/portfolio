#!/usr/bin/env python3

import logging
from datetime import timedelta # for data-point indexing


class DataPoint(object):
    """ Represents data point to save in a time series. """

    def __init__(self, value) -> DataPoint:
        self._logger = logging.getLogger(name=__name__)
        self.reset()
        self._value = value
    
    @value.deleter
    @frequency.deleter
    def reset(self) -> None:
        self._logger.debug(f"Reset {self}")
        del self._value 
        self._freq = 0
        self._delta = 0

    @property
    def value(self) -> type(self._value):
        self._logger.debug(f"Get {self}._value ({self._value})")
        self._freq = self._freq + 1
        return self._value
    
    @value.setter
    def value(self, value) -> None:
        self._logger.debug(f"Set {self}._value to {value}")
        self._delta = self._value - value
        self._value = value

    @property
    def frequency(self) -> float:
        self._logger.debug(f"Get {self}._freq ({self._freq})")
        return self._freq

    @property
    def delta(self):
        self._logger.debug(f"Get {self}._delta ({self._delta}")
        return self._delta


class TimeSeries(object):
    """ Represents a time series """

    def __init__(self):
        pass

    def add(domain, image):
        pass
