import datetime
from fastapi import APIRouter

import domain.data.reports as reports

reports_router = APIRouter()


@reports_router.get("/expenses_by_category_by_month/{category_id}/{year}/{month}")
def get_expenses_by_category_by_month(category_id: int, year: int, month: int):
    return reports.get_expenses_by_category_by_month(category_id, year, month)


@reports_router.get("/expenses_by_subcategory_by_month/{subcategory_id}/{year}/{month}")
def get_expenses_by_category_by_month(subcategory_id: int, year: int, month: int):
    return reports.get_expenses_by_subcategory_by_month(subcategory_id, year, month)


@reports_router.get("/expenses_by_day/{year}/{month}/{day}")
def get_expenses_by_day(year: int, month: int, day: int):
    return reports.get_expenses_by_day(datetime.date(year, month, day))


@reports_router.get("/get_average_expenses_report")
def get_expenses_by_day():
    return reports.get_average_expenses_report()
