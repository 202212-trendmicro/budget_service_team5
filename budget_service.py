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
        if end < start:
            return 0

        total_amount = 0
        period = Period(start, end)
        budgets = self.get_all()
        for budget in budgets:
            total_amount += budget.overlapping_amount(period)

        return total_amount

    def get_all(self) -> List[Budget]:
        pass


if __name__ == "__main__":
    pass
