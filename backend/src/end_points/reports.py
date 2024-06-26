import datetime
from fastapi import APIRouter

import domain.data.reports as reports

reports_router = APIRouter(tags=["Reports"])


@reports_router.get("/expenses_by_all_categories_by_month/{year}/{month}")
def get_expenses_by_all_categories_by_month(year: int, month: int):
    return reports.get_expenses_by_all_categories_and_subcategories_by_month(year, month)


@reports_router.get("/expenses_by_all_days_in_month/{year}/{month}")
def get_expenses_by_all_days_in_month(year: int, month: int):
    return reports.get_expenses_by_all_days_in_month(year, month)
