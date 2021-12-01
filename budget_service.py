# Spec 
# 202004 的預算是 30萬  查詢4月1號 會回傳1萬
# by天的預算 金額是int
# 假設一個月 三十萬 查詢一天 回傳一萬
# 輸入查詢日期(date) 回傳預算
from datetime import date
from typing import List

from monthdelta import monthdelta

from budget import Budget
from period import Period


class BudgetService:
    def __init__(self) -> None:
        self.current_v = 0

    def query(self, start, end) -> float:
        budgets = self.get_all()
        if end < start:
            return 0

        cur_date = start
        total_amount = 0
        period = Period(start, end)
        while cur_date < date(end.year, end.month, 1) + monthdelta(1):
            current_year_month = str(cur_date)[0:4] + str(cur_date)[5:7]
            matched_budgets = list(filter(lambda x: x.year_month == current_year_month, budgets))
            if len(matched_budgets) > 0:
                budget = matched_budgets[0]
                total_amount += budget.overlapping_amount(period)
            cur_date = cur_date + monthdelta(1)

        return total_amount

    def get_all(self) -> List[Budget]:
        pass


if __name__ == "__main__":
    pass
