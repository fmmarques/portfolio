#!/usr/bin/false

import logging
from stock_exchange import StockExchange


class Company(object):

    def __init__(name: str, tick: str, stock_exchange: StockExchange):
        self._name = name
        self._tick = name
        self._stock_exchange = stock_exchange
        self._stock_exchange.add_company(self)

    @property
    def name(self) -> str:
        logging.debug("Called Company.name getter")
        return self._name

    @name.setter
    def name(self, new_name) -> object:
        logging.debug("Called Company.name setter")
        self._name = new_name
        return self

    @name.deleter
    def name(self) -> object:
        logging.debug("Called Company.name deleter")
        del self._name
        return self

    @property
    def tick(self) -> str:
        logging.debug("Called Company.tick getter")
        return self._tick

    @tick.setter
    def tick(self, new_tick: str) -> object:
        logging.debug("Called Company.tick setter")
        self._tick = new_tick
        return self

    @tick.deleter
    def tick(self) -> object:
        logging.debug("Called Company.tick deleter")
        del self._tick
        return self

    @property
    def stock_exchange(self) -> object:
        logging.debug("Called Company.stock_exchange getter")
        return self._stock_exchange

    @stock_exchange.setter
    def stock_exchange(self, stock_exchange: object) -> object:
        logging.debug("Called Company.stock_exchange setter")
        self._stock_exchange = stock_exchange
        return self

    @stock_exchange.deleter
    def stock_exchange(self) -> object:
        logging.debug("Called Company.stock_exchange deleter")
        del self._stock_exchange
        return self



