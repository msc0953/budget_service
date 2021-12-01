import unittest

from typing import List


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

    def query(self, start, end):
        budgets = self.get_all_budgets()
        if not budgets:
            return 0

        if start > end:
            return 0
        return budgets[0].amount


if __name__ == '__main__':
    unittest.main()
