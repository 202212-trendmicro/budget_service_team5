import calendar
from datetime import datetime, date

from period import Period


class Budget:
    def __init__(self, year_month, amount):
        self.year_month = year_month
        self.amount = amount

    def first_day(self):
        return datetime.strptime(self.year_month, '%Y%m').date()

    def last_day(self):
        days_in_month = calendar.monthrange(self.first_day().year, self.first_day().month)[1]
        return date(self.first_day().year, self.first_day().month, days_in_month)

    def days(self):
        return calendar.monthrange(self.first_day().year, self.first_day().month)[1]

    def daily_amount(self):
        return self.amount / self.days()
    def create_period(self):
        return Period(self.first_day(), self.last_day())
