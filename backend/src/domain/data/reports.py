import datetime
import calendar

from sqlalchemy import select
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import Session

from common.data.db import get_session
from common.data.db_models import Buy
from domain.data.config import list_reports_configs
from domain.data.category import list_categories


def get_expenses_by_category_by_month(category_id: int, year: int, month: int) -> int | None:
    session: Session = get_session()
    query = (select(func.sum(Buy.sum).label("expenses"))
             .where(category_id == Buy.category_id)
             .where(Buy.date >= datetime.date(day=1, month=month, year=year))
             .where(Buy.date <= datetime.date(day=calendar.monthrange(year, month)[1], month=month, year=year)))
    return session.execute(query).scalar_one()


def get_expenses_by_subcategory_by_month(category_id: int, subcategory_id: int, year: int, month: int) -> int | None:
    session: Session = get_session()
    query = (select(func.sum(Buy.sum).label("expenses"))
             .where(category_id == Buy.category_id)
             .where(subcategory_id == Buy.subcategory_id)
             .where(Buy.date >= datetime.date(day=1, month=month, year=year))
             .where(Buy.date <= datetime.date(day=calendar.monthrange(year, month)[1], month=month, year=year)))
    return session.execute(query).scalar_one()


def get_expenses_by_all_categories_and_subcategories_by_month(year: int, month: int) -> dict:
    """Get expenses by all categories and subcategories by month.

    Structure of returned dictionary is as follows:
    {
        <category names>: {
            "Expenses": <amount of expenses in category>
            "Subcategories": {
                <subcategory names>: <amount of expenses in subcategory>
            }
        }
    }

    Returns:
        JSON-like dictionary with next structure
    """
    categories = list_categories()
    result = {}
    for category in categories:
        category_expenses = get_expenses_by_category_by_month(category.id, year, month)
        result[category.name] = {
            "Expenses": category_expenses,
            "Subcategories": {}
        }
        all_subcategories_expenses = result[category.name]["Subcategories"]
        for subcategory in category.subcategories:
            subcategory_expenses = get_expenses_by_subcategory_by_month(category.id, subcategory.id, year, month)
            all_subcategories_expenses[subcategory.name] = subcategory_expenses

    return result


def get_expenses_by_day(date: datetime.date) -> int | None:
    session: Session = get_session()
    query = (select(func.sum(Buy.sum).label("expenses"))
             .where(Buy.date == date))
    return session.execute(query).scalar_one()


def get_expenses_by_all_days_in_month(year: int, month: int):
    session: Session = get_session()
    query = (session.query(Buy.date, func.sum(Buy.sum).label("expenses"))
             .group_by(Buy.date)
             .order_by(Buy.date)
             .where(Buy.date >= datetime.date(day=1, month=month, year=year))
             .where(Buy.date <= datetime.date(day=calendar.monthrange(year, month)[1], month=month, year=year)))
    query_result: list[tuple[datetime.date, int]] = query.all()
    result = {}
    for i in range(1, calendar.monthrange(year, month)[1] + 1):
        result[str(datetime.date(year, month, i))] = 0

    for r in query_result:
        result[str(r[0])] = r[1]

    return result


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
    # TODO: fix report
    session: Session = get_session()
    food_expenses_query = (select(func.sum(Buy.sum)).where(Buy.category_id == 1).where(Buy.date >= start_day))
    food_expenses = session.execute(food_expenses_query).scalar_one() or 0
    transport_expenses_query = (select(func.sum(Buy.sum)).where(Buy.subcategory_id == 3).where(Buy.date >= start_day))
    transport_expenses = session.execute(transport_expenses_query).scalar_one() or 0
    sum_of_expenses = (food_expenses + transport_expenses) or 0
    return sum_of_expenses


get_average_expenses_report()
