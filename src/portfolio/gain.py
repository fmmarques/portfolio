
class gain:

    def __init__(self):
        self.present_rate = 0
        self.future_rate = 0
        self.rate = 0

    def _calculate_rate(self):
        assert self.present_value > 0, "Present value is 0, which yields a div by 0 error."
        self.rate = (self.future_rate - self.present_rate) / self.present_rate

    def set_present_value(self, present_value):
        self.present_value = present_value
        self._calculate_rate()

    def set_future_value(self, future_value):
        self.future_value = future_value
        self._calculate_rate()

