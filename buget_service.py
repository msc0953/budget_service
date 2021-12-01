import unittest
from datetime import date

from typing import List
from calendar import monthrange, calendar


class Budget:
    def __init__(self, year_month, amount) -> None:
        super().__init__()
        self.year_month = year_month
        self.amount = amount


class BudgetService:
    def __init__(self):
        pass

    def get_all_budgets(self) -> List[Budget]:
        pass

    def ratio(self, start, end, amount):
        delta = (end - start).days + 1
        num_days = monthrange(start.year, start.month)[1]
        return delta * (amount // num_days)

    def query(self, start, end):
        budgets = self.get_all_budgets()
        if start > end:
            return 0

        if not budgets:
            return 0

        if (start.year == end.year) and (start.month == end.month):
            return self.ratio(start, end, budgets[0].amount)

        if self.get_months(start, end)==1:
            front_month = date(start.year, start.month, monthrange(start.year, start.month)[1])
            last_month = date(end.year, end.month, 1)
            return self.ratio(start, front_month, budgets[0].amount) + self.ratio(last_month, end, budgets[1].amount)

        if self.get_months(start, end)>1:
            front_month = date(start.year, start.month, monthrange(start.year, start.month)[1])
            last_month = date(end.year, end.month, 1)

            total = self.ratio(start, front_month, budgets[0].amount) + self.ratio(last_month, end, budgets[-1].amount)
            for b in budgets[1:-1]:
                total = total + b.amount
            return total

        return budgets[0].amount

    def get_months(self, start, end):
        # month_delta = end.month - start.month + 12 * (end.year - start.year)
        # month_list = pd.date_range(start.year, freq='M', period=month_delta)
        return end.month - start.month + 12 * (end.year - start.year)

if __name__ == '__main__':
    unittest.main()
