
class CompanyAlreadyListed(Exception):

    def __init__(self, stock_exchange: object, company: object, message: str,
                 message_args: tuple = ()):
        super().__init__(message % message_args)
        self._message = message % message_args
        self._company = company
        self._stock_exchange = stock_exchange

    @property
    def message(self):
        return self._message

    @property
    def company(self):
        return self._company

    @property
    def stock_exchange(self):
        return self._stock_exchange
