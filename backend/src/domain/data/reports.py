import datetime
import calendar

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from common.data.db import get_session
from common.data.db_models import Buy
from domain.data.config import list_reports_configs


def get_expenses_by_category_by_month(category_id: int, year: int, month: int) -> int | None:
    session: Session = get_session()
    query = (select(func.sum(Buy.sum).label("expenses"))
             .where(category_id == Buy.category_id)
             .where(Buy.date >= datetime.date(day=1, month=month, year=year))
             .where(Buy.date <= datetime.date(day=calendar.monthrange(year, month)[1], month=month, year=year)))
    return session.execute(query).scalar_one()


def get_expenses_by_subcategory_by_month(subcategory_id: int, year: int, month: int) -> int | None:
    session: Session = get_session()
    query = (select(func.sum(Buy.sum).label("expenses"))
             .where(subcategory_id == Buy.subcategory_id)
             .where(Buy.date >= datetime.date(day=1, month=month, year=year))
             .where(Buy.date <= datetime.date(day=calendar.monthrange(year, month)[1], month=month, year=year)))
    return session.execute(query).scalar_one()


def get_expenses_by_day(date: datetime.date) -> int | None:
    session: Session = get_session()
    query = (select(func.sum(Buy.sum).label("expenses"))
             .where(Buy.date == date))
    return session.execute(query).scalar_one()


def get_average_expenses_report() -> dict:
    expected_expenses_per_day, start_day = _get_config()
    sum_of_expenses = _get_sum_of_expenses(start_day)
    day_past = _get_day_past(start_day)
    actual_expenses_per_day = sum_of_expenses / day_past
    actual_remainder = expected_expenses_per_day * day_past - sum_of_expenses
    future_remainders = _get_future_remainders(expected_expenses_per_day, start_day, sum_of_expenses)

    return {
        "config": {
            "start day": start_day,
            "expected expenses per day": expected_expenses_per_day,
        },
        "sum of expenses": sum_of_expenses,
        "day past": day_past,
        "actual expenses per day": actual_expenses_per_day,
        "actual expenses pey month": actual_expenses_per_day * 30,
        "expected expenses per month": expected_expenses_per_day * 30,
        "actual remainder": actual_remainder,
        "future remainder": future_remainders
    }


def _get_future_remainders(expected_expenses_per_day, start_day, sum_of_expenses):
    future_remainders = []
    for i in range(1, 11):
        date = datetime.date.today() + datetime.timedelta(days=i)
        future_day_past = _get_day_past(start_day, offset_days=1)
        future_remainders.append(
            {
                "date": date,
                #Todo: fix remainder
                "remainder": future_day_past * expected_expenses_per_day - sum_of_expenses,
                "expenses per day": sum_of_expenses / future_day_past
            }
        )
    return future_remainders


def _get_config():
    reports_configs = list_reports_configs()
    if len(reports_configs) != 0:
        config = reports_configs[0]
        start_day = config.start_day
        expected_expenses_per_day = config.expected_expenses_per_day
    else:
        start_day = datetime.date(year=2024, month=6, day=1)
        expected_expenses_per_day = 290
    return expected_expenses_per_day, start_day


def _get_day_past(start_day, offset_days=0):
    day_past = (datetime.date.today() - start_day).days + 1 + offset_days
    return day_past


def _get_sum_of_expenses(start_day):
    session: Session = get_session()
    food_expenses_query = (select(func.sum(Buy.sum)).where(Buy.category_id == 598).where(Buy.date >= start_day))
    food_expenses = session.execute(food_expenses_query).scalar_one()
    transport_expenses_query = (select(func.sum(Buy.sum)).where(Buy.subcategory_id == 369).where(Buy.date >= start_day))
    transport_expenses = session.execute(transport_expenses_query).scalar_one()
    #sum_of_expenses = (food_expenses + transport_expenses) or 0
    return 1000


get_average_expenses_report()
