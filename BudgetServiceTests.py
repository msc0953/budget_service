import unittest
from datetime import date

from buget_service import Budget, BudgetService


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = BudgetService()

    def fake_budgets(self):
        return self.fake_data

    def test_no_data(self):
        start = date(2022, 12, 31)
        end = date(2022, 12, 31)
        self.fake_data = []
        self.s.get_all_budgets = self.fake_budgets
        amount = self.s.query(start, end)
        assert amount == 0

    def test_invalid_start_day(self):
        start = date(2022, 1, 1)
        end = date(2021, 12, 31)
        expected_amount = 0
        amount = self.s.query(start, end)
        assert amount == expected_amount

    def test_no_budget(self):
        self.fake_data = [Budget("202112", 0)]
        self.s.get_all_budgets = self.fake_budgets
        result = self.s.query(date(2021, 12, 31), date(2021, 12, 31))
        self.assertEqual(0, result)  # add assertion here

    def test_in_same_month(self):
        self.fake_data = [Budget("202112", 31)]
        self.s.get_all_budgets = self.fake_budgets
        result = self.s.query(date(2021, 12, 1), date(2021, 12, 3))
        self.assertEqual(3, result)

    def test_cross_2_month(self):
        self.fake_data = [Budget("202112", 31), Budget("202201", 62)]
        self.s.get_all_budgets = self.fake_budgets
        result = self.s.query(date(2021, 12, 31), date(2022, 1, 3))
        self.assertEqual(7, result)

    def test_cross_month(self):
        self.fake_data = [Budget("202112", 31), Budget("202201", 62), Budget("202202", 0), Budget("202203", 93)]
        self.s.get_all_budgets = self.fake_budgets
        result = self.s.query(date(2021, 12, 31), date(2022, 3, 1))
        self.assertEqual(66, result)

    def test_cross_month_with_no_data(self):
        self.fake_data = [Budget("202112", 31), Budget("202201", 62), Budget("202202", 0), Budget("202203", 93), Budget("202205", 31)]
        self.s.get_all_budgets = self.fake_budgets
        result = self.s.query(date(2022, 3, 1), date(2022, 5, 1))
        self.assertEqual(94, result)



if __name__ == '__main__':
    unittest.main()
