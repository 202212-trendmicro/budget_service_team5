# Spec 
# 202004 的預算是 30萬  查詢4月1號 會回傳1萬
# by天的預算 金額是int
# 假設一個月 三十萬 查詢一天 回傳一萬
# 輸入查詢日期(date) 回傳預算
from typing import List

from budget import Budget
from period import Period


class BudgetService:
    def query(self, start, end) -> float:
        period = Period(start, end)
        return sum(budget.overlapping_amount(period) for budget in (self.get_all()))

    def get_all(self) -> List[Budget]:
        pass


if __name__ == "__main__":
    pass
