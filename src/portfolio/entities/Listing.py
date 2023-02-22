#!/usr/bin/false

from __future__ import annotations
import logging
from . import AbstractStock


class Stock(AbstractStock):
    """ Represents a common stock. """

    def __init__(self, isin: str, tick: str, price: float):
        super()
        self.isin = isin
        self.tick = tick
        self.price = price


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

