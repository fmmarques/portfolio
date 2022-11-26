import logging

from exceptions import CompanyAlreadyListed

class StockExchange(object):
    """ Represents a stock exchange where one or more companies are listed """
    """ and commercialised. """

    def __init__(name: str) -> object:
        self._name = name
        self._companies_listed = dict()

    @property
    def name(self) -> str:
        return self._name

    def list_company(company: object) -> object:
        if company.tick in self._companies_listed.keys():
            raise CompanyAlreadyListed(self, company, "The company \"{}\" is "
                                       "already listed on {}", company.name, self.name)
        self._companies_listed[ company.tick ] = company
        return self

    def delist_company(company: object) -> object:
        if company.tick not in self._companies_listed.keys()
            raise CompanyNotListed(self, company, "The company \"{}\" is "
                                   "not listed on \"{}\"", company.name, self.name)
        del self._companies_listed[ company.tick ]
        return self

    def __getitem__(self, tick) -> object:
        if tick is not str:
            raise TypeError("Company identifiers (ticks) must be strings.")
        if tick not in self._companies_listed.keys():
            raise ValueError(f"There isn't a company listed under \"{tick}\".")
        return self._companies_listed[tick]


