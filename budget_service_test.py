import unittest

from datetime import date

from budget import Budget
from budget_service import BudgetService


class BudgetServiceTests(unittest.TestCase):
    def setUp(self):
        self.b = BudgetService()

    def test_query_one_day(self):
        self.mock_budget = [Budget('202006', 30)]
        self.b.get_all = self.fake_budgets
        start_date = date(2020, 6, 1)
        end_date = date(2020, 6, 1)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 1)

    def test_query_one_day_without_db_data(self):
        self.mock_budget = []
        self.b.get_all = self.fake_budgets
        start_date = date(2020, 6, 1)
        end_date = date(2020, 6, 1)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 0)

    def test_query_one_day_when_year_month_budget_is_zero(self):
        self.mock_budget = [Budget('202006', 0)]
        self.b.get_all = self.fake_budgets
        start_date = date(2020, 6, 1)
        end_date = date(2020, 6, 1)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 0)

    def test_query_cross_days_same_month(self):
        self.mock_budget = [Budget('202006', 30)]
        self.b.get_all = self.fake_budgets
        start_date = date(2020, 6, 1)
        end_date = date(2020, 6, 30)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 30)

    def test_query_invalid_cross_days(self):
        self.mock_budget = [Budget('202006', 30)]
        self.b.get_all = self.fake_budgets
        start_date = date(2020, 6, 30)
        end_date = date(2020, 6, 1)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 0)

    def test_query_cross_month(self):
        self.mock_budget = [Budget('202005', 31), Budget('202006', 60)]
        self.b.get_all = self.fake_budgets
        start_date = date(2020, 5, 31)
        end_date = date(2020, 6, 2)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 5)

    def test_query_cross_multiple_month(self):
        self.mock_budget = [Budget('202005', 31), Budget('202006', 60), Budget('202007', 93)]
        self.b.get_all = self.fake_budgets
        start_date = date(2020, 5, 31)
        end_date = date(2020, 7, 2)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 67)

    def test_query_cross_multiple_month_with_empty_middle_budget(self):
        self.mock_budget = [Budget('202005', 31), Budget('202007', 93)]
        self.b.get_all = self.fake_budgets
        start_date = date(2020, 5, 31)
        end_date = date(2020, 7, 2)
        result = self.b.query(start_date, end_date)
        self.assertEqual(result, 1 + 2 * 3)

    def fake_budgets(self):
        return self.mock_budget
