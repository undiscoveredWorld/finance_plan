from pydantic import BaseModel


class Date(BaseModel):
    day: int
    month: int
    year: int

    def __init__(self, day: int, month: int, year: int) -> None:
        super().__init__(
            day=day,
            month=month,
            year=year
        )

    def __str__(self) -> str:
        return f"{self.month}/{self.day}/{self.year}"
