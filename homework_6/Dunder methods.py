class Price:
    CURRENCY_RATES = [
        {"from": "USD", "to": "UAH", "rate": 36.92},
        {"from": "UAH", "to": "USD", "rate": 0.027},
        {"from": "USD", "to": "GBP", "rate": 0.8},
        {"from": "GBP", "to": "USD", "rate": 1.26},
        {"from": "USD", "to": "EUR", "rate": 0.91},
        {"from": "EUR", "to": "USD", "rate": 1.1},
    ]

    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def conversion(self, amount_of_money, currency_from, currency_to):
        for i in Price.CURRENCY_RATES:
            if i["from"] == currency_from and i["to"] == currency_to:
                return round(amount_of_money * i["rate"], 2)

    def __add__(self, other):
        if self.currency == other.currency:
            return self.amount + other.amount, self.currency

        if self.currency == "USD" or other.currency == "USD":
            amount = self.conversion(
                amount_of_money=other.amount,
                currency_from=other.currency,
                currency_to=self.currency,
            )
            return self.amount + amount, self.currency

        amount_1 = self.conversion(
            amount_of_money=other.amount,
            currency_from=other.currency,
            currency_to="USD",
        )
        amount_2 = self.conversion(
            amount_of_money=self.amount,
            currency_from=self.currency,
            currency_to="USD"
            )
        after_conversion = self.conversion(
            amount_of_money=amount_1 + amount_2,
            currency_from="USD",
            currency_to=self.currency,
            )
        return (after_conversion, self.currency)

    def __sub__(self, other):
        if self.currency == other.currency:
            amount = self.amount - other.amount
            if amount >= 0:
                return amount, self.currency
            raise BaseException("less than zero")

        if other.currency == "USD" or self.currency == "USD":
            amount = self.conversion(
                                    other.amount,
                                    other.currency,
                                    self.currency
                                    )
            after_conversion = self.amount - amount
            if after_conversion >= 0:
                return after_conversion, self.currency
            raise BaseException("less than zero")

        amount_1 = self.conversion(
            amount_of_money=self.amount,
            currency_from=self.currency,
            currency_to="USD"
        )
        amount_2 = self.conversion(
            amount_of_money=other.amount,
            currency_from=other.currency,
            currency_to="USD",
        )
        after_conversion = self.conversion(
            amount_of_money=amount_1 - amount_2,
            currency_from="USD",
            currency_to=self.currency,
        )
        if after_conversion >= 0:
            return after_conversion, self.currency
        raise BaseException("less than zero")
