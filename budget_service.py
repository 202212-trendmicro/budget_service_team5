# Spec 
# 202004 的預算是 30萬  查詢4月1號 會回傳1萬
# by天的預算 金額是int
# 假設一個月 三十萬 查詢一天 回傳一萬
# 輸入查詢日期(date) 回傳預算
import datetime
from datetime import date
from typing import List

from monthdelta import monthdelta
# from datetime import date
# import datetime
from calendar import monthrange

from budget import Budget


class Period:

    def __init__(self, start, end) -> None:
        super().__init__()
        self.end = end
        self.start = start


class BudgetService:
    def __init__(self) -> None:
        self.current_v = 0

    def query(self, start, end) -> float:
        budgets = self.get_all()
        if end < start:
            return 0
        start_end_date = date(start.year, start.month + 1, 1) - datetime.timedelta(days=1)
        end_start_date = date(end.year, end.month, 1)

        if start.year == end.year and start.month == end.month:
            return self.query_same_month_range(start, end, budgets)

        cur_date = start
        total_amount = 0
        while cur_date < date(end.year, end.month, 1) + monthdelta(1):
            current_year_month = str(cur_date)[0:4] + str(cur_date)[5:7]
            matched_budgets = list(filter(lambda x: x.year_month == current_year_month, budgets))
            if len(matched_budgets) > 0:
                budget = matched_budgets[0]
                overlapping_days = self.get_overlapping_days(budget, start, end)
                overlapping_amount = budget.daily_amount() * overlapping_days
                total_amount += overlapping_amount
            cur_date = cur_date + monthdelta(1)

        return total_amount

    def get_overlapping_days(self, budget, start, end):
        period = Period(start, end)
        temp_start = period.start
        temp_end = period.end
        overlapping_start = temp_start if temp_start > budget.first_day() else budget.first_day()
        overlapping_end = temp_end if temp_end < budget.last_day() else budget.last_day()
        overlapping_days = ((overlapping_end - overlapping_start).days + 1)
        return overlapping_days

    def query_same_month_range(self, start_date, end_date, budgets):
        days = -1
        for budget in budgets:
            year = str(start_date)[:4]
            month = str(start_date)[5:7]
            days = monthrange(int(year), int(month))[1]
            if year == budget.year_month[:4] and month == budget.year_month[4:6]:
                self.current_v = budget.amount
            # get month budget
        diff = (end_date - start_date).days
        if days < 0 or diff < 0:
            return 0
        result = (diff + 1) * self.current_v // days
        return result

    def get_all(self) -> List[Budget]:
        pass


if __name__ == "__main__":
    pass
