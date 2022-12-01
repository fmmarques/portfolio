#!/usr/bin/false

import logging
from __future__ import annotations
from abc import ABC, abstractmethod

from . import AbstractCompany

class AbstractListing(ABC):
    """ Represents a listing in a stock exchange. """
    """ Any Company can have multiple stock types, in multiple stock """
    """ exchanges, thus yielding multiple listings. """

    @abstractmethod
    @property
    def price(self) -> float:
        logging.debug("AbstractListing.price: %f", self._price)
        return self._price

    @abstractmethod
    @property
    def price(self, price: float) -> AbstractListing:
        logging.debug("AbstractListing.price: %f -> %f", self._price, price)
        self._price = price
        return self


