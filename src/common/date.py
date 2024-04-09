from pydantic import BaseModel


class Date(BaseModel):
    day: int
    month: int
    year: int

    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"{self.month}/{self.day}/{self.year}"
