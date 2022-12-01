#!/usr/bin/false

import logging
from stock_exchange import StockExchange


class Company(object):

    def __init__(name: str, isin: str, shares_outstanding: int,
                 shares_floating: int):
        self._name = name
        self._isin = isin
        self._shares_outstanding = shares_outstanding
        self._shares_floating = shares_floating

        self.__recalculate_internal_values()

    def __recalculate_internal_values(self):
        logging.debug("Called Company(%s).__recalculate_internal_values")
        self._shares_restricted_or_closely_held = self._shares_oustanding - \
                                                  self._shares_floating

    @property
    def name(self) -> str:
        logging.debug("Called Company(%s).name getter", self._name)
        return self._name

    @name.setter
    def name(self, new_name) -> object:
        logging.debug("Called Company(%s).name setter", self._name)
        self._name = new_name
        return self

    @name.deleter
    def name(self) -> object:
        logging.debug("Called Company(%s).name deleter", self._name)
        del self._name
        return self

    @property
    def isin(self) -> str:
        logging.debug("Called Company(%s).isin getter.", self._name)
        return self._isin

    @isin.setter
    def isin(self, new_isin: str) -> object:
        logging.debug("Called Company(%s).isin setter.", self._name)
        self._isin = new_isin
        return self

    @isin.deleter
    def isin(self) -> object:
        logging.debug("Called Company(%s).isin deleter.", self._name)
        del self._isin
        return self

    @property
    def total_issued_shares(self) -> int:
        logging.debug("Called Company(%s).total_issued_shares.", self._name)
        return self._total_issued_shares

    def create_share(self, ) -> object:
        """ Factory method for generating a stock. """
        pass

    def create_bond(self) -> object:
        """ Factory method for generating a bond. """
        pass

