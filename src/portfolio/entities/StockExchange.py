#!/usr/bin/false

import logging
from __future__ import annotations
from abc import ABC, abstractmethod

from . import (AbstractCompany, Company,
               AbstractStock, Stock)

from exceptions import CompanyAlreadyListed

class AbstractStockExchange(ABC):
    """ Represents an abstract stock exchange where one or more companies are listed """
    """ and commercialised. """
    """ Also acts as a stock factory, following the factory method design pattern """

    @abstractmethod
    def list_common_stock(company: AbstractCompany) -> AbstractStock:
        """ Lists a company's common stock on this stock exchange """
        """ Acts as a factory method yielding an AbstractStock """
        pass

    @abstractmethod
    def delist_common_stock(company: AbstractCompany) -> AbstractStockExchange:
        """ Delists a company's common stock of this stock exchange. """
        """ Returns self """
        pass


class StockExchange(AbstractStockExchange):
    """ Represents a concrete Stock Exchange """

    def __init__(name: str) -> object:
        self._name = name
        self._common_stocks = dict[str, AbstractStock]()
        self._preferred_stocks = dict()

    def list_common_stock(company: AbstractCompany) -> AbstractStock:
        """ Lists a Company on this Stock Exchange, yielding a stock. """

        if company.tick in self._common_stocks.keys():
            raise CommonStockAlreadyListed(self, company, "The common stock of "
                                           "\"{}\" is already listed on {}",
                                           company.name, self.name)

        self._common_stock[company.tick] = CommonStock()
        return

    def delist_company(company: Company) -> object:
        if company.tick not in self._companies_listed.keys()
            raise CompanyNotListed(self, company, "The company \"{}\" is "
                                   "not listed on \"{}\"", company.name, self.name)
        del self._companies_listed[ company.tick ]
        return self

    @property
    def name(self) -> str:
        return self._name

    def __getitem__(self, tick) -> object:
        if tick is not str:
            raise TypeError("Company identifiers (ticks) must be strings.")
        if tick not in self._companies_listed.keys():
            raise ValueError(f"There isn't a company listed under \"{tick}\".")
        return self._companies_listed[tick]


