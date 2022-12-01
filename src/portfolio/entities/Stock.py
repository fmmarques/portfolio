#!/usr/bin/false

from __future__ import annotations
from abc import ABC, abstractmethod

from . import AbstractCompany

class AbstractStock(ABC):
    """ Represents a stock concept. A stock has a unique isin, a shared tick, a price """

    @property
    @abstractmethod
    def currency(self) -> str:
        logging.debug("AbstractStock.currency: %s", self._currency)
        return self._currency

    @property
    @abstractmethod
    def currency(self, currency) -> AbstractStock:
        logging.debug("AbstractStock.currency: %s -> %s", self._currency, currency)
        self._currency = currency
        return self

    @property
    @abstractmethod
    def isin(self) -> str:
        logging.debug("AbstractStock.isin: %s", self._isin)
        return self._isin

    @property
    @abstractmethod
    def isin(self, isin: str) -> AbstractStock:
        logging.debug("AbstractStock.isin: %s -> %s", self._isin, isin)
        self._isin = isin
        return self

    @property
    @abstractmethod
    def price(self) -> float:
        logging.debug("AbstractStock.price: %f", self._price)
        return self._price

    @property
    @abstractmethod
    def price(self, price: float) -> AbstractStock
        logging.debug("AbstractStock.price: %f -> %f", self._price, price)
        self._price = price
        return self

    @property
    @abstractmethod
    def tick(self) -> str:
        logging.debug("AbstractStock.tick: %s", self._tick)
        return self._tick

    @property
    @abstractmethod
    def tick(self, tick) -> AbstractStock:
        logging.debug("AbstractStock.tick: %s -> %s", self._tick, tick)
        self._tick = _tick
        return self


class CommonStock(ABC):
    """ Represents a common stock. """


    def __init__(self, isin: str, price: float):
        super()
        self.isin = isin
        self.price = price
        self.tick = tick


        self.initial_cost = initial_cost
        self.current_value = current_value
        self.annual_dividends = annual_dividends

        # calculate and set dividend yield.
        self.set_known_dividends(self.annual_dividends)

        # calculate and set capital gain.
        capital_gain = (self.current_value - self.initial_cost) / self.initial_cost
        self.set_capital_gain(capital_gain)


    def set_known_dividends(self, all_dividends):
        self.all_dividends = all_dividends
        self.accrued_dividend = 0
        for dividend in self.all_dividends:
            self.accrued_dividend += dividend

        self.dividend_yield = self.accrued_dividend / self.initial_cost

    def set_annual_dividend(self, annual_dividend):
        self.set_known_dividends([annual_dividend])

    def get_annual_dividend(self):
        return self.annual_dividend

    def set_capital_gain(self, calculated_capital_gain):
        self.capital_gain = calculated_capital_gain

    def get_capital_gain(self):
        return self.capital_gain

    def set_dividend_yield(self, dividend_yield):
        accrued_dividend = dividend_yield * self.initial_cost
        self.set_known_dividends([accrued_dividend])

    def get_dividend_yield(self):
        return self.dividend_yield

    def get_return_rate(self):
        return self.get_capital_gain() + self.get_dividend_yield()

