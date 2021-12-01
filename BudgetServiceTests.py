import unittest
from datetime import date

from buget_service import Budget, BudgetService


class MyTestCase(unittest.TestCase):

    def test_no_data(self):
        start = date(2022, 12, 31)
        end = date(2022, 12, 31)
        s = BudgetService()
        self.fake_data = []
        s.get_all_budgets = self.fake_budgets
        amount = s.query(start, end)
        assert amount == 0

    def test_invalid_start_day(self):
        start = date(2022, 1, 1)
        end = date(2021, 12, 31)
        expected_amount = 0
        s = BudgetService()
        amount = s.query(start, end)
        assert amount == expected_amount

    def test_no_budget(self):
        self.fake_data = [Budget("202112", 0)]
        budget_service = BudgetService()
        budget_service.get_all_budgets = self.fake_budgets
        result = budget_service.query(date(2021, 12, 31), date(2021, 12, 31))
        self.assertEqual(0, result)  # add assertion here

    def fake_budgets(self):
        return self.fake_data


if __name__ == '__main__':
    unittest.main()
