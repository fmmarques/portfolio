
class bond:

    def __init__(self, isin, face_value,
                 annual_coupon_rate, years_to_maturity):
        self.isin = isin
        self.face_value = face_value
        self.annual_coupon_rate = annual_coupon_rate
        self.years_to_maturity = years_to_maturity
        self._calculate_expected_cash_flow()

    def _calculate_expected_cash_flow(self):

        self.future_cash_flow = self.annual_coupon_rate * self.face_value
        self.discount_rate = self.future_cash_flow
        # self.present_value = self.future_cash_flow / (1 + self.discount_rate)
        self.net_present_value = 0
        for year in range(1, self.years_to_maturity):
            self.net_present_value = self.future_cash_flow % (1 + self.discount_rate)**year

