class Period:

    def __init__(self, start, end) -> None:
        super().__init__()
        self.end = end
        self.start = start

    def get_overlapping_days(self, budget):
        another = Period(budget.first_day(), budget.last_day())
        first_day = budget.first_day()
        last_day = budget.last_day()
        overlapping_start = self.start if self.start > first_day else first_day
        overlapping_end = self.end if self.end < last_day else last_day
        return (overlapping_end - overlapping_start).days + 1
