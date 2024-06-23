from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from common.data.utils import check_object_is_subclass_of_model
from common.data.db import get_session
from common.data.db_models import ReportsConfig as DB_ReportsConfig
from domain.models import (
    ReportsConfigCreate,
    ReportsConfigUpdate,
    ReportsConfig,
)


def add_reports_config(reports_config: ReportsConfigCreate) -> int:
    """Add reports_config to db.

    Raises:
        TypeError: if object is not subclass of model
    """
    check_object_is_subclass_of_model(reports_config, ReportsConfigCreate)
    db_session: Session = get_session()

    new_reports_config = DB_ReportsConfig(**reports_config.model_dump())
    db_session.add(new_reports_config)
    db_session.commit()

    return new_reports_config.id


def list_reports_configs() -> list[ReportsConfig]:
    db_session: Session = get_session()
    db_reports_configs = db_session.query(DB_ReportsConfig).all()
    return _convert_db_configs_to_pydantic_configs(db_reports_configs)


def _convert_db_configs_to_pydantic_configs(db_reports_configs):
    reports_configs = []
    for reports_config in db_reports_configs:
        reports_configs.append(ReportsConfig.model_validate(reports_config.__dict__))
    return reports_configs


def update_reports_config(id_: int, new_reports_config: ReportsConfigUpdate) -> None:
    """Update reports_config in db.

    Raises:
        TypeError: if object is not subclass of model
        NoResultFound: if id_ was not found in the db
    """
    check_object_is_subclass_of_model(new_reports_config, ReportsConfigUpdate)

    db_session: Session = get_session()
    reports_config = db_session.execute(select(DB_ReportsConfig).filter_by(id=id_)).scalar_one()
    if reports_config is None:
        raise NoResultFound(f"ReportsConfig with id_ {id_} does not found")

    for key, value in new_reports_config.model_dump().items():
        if value is not None:
            reports_config.__setattr__(key, value)

    db_session.commit()


def delete_reports_config(id_: int) -> None:
    """Delete reports_config."""
    db_session: Session = get_session()
    db_session.query(DB_ReportsConfig).filter_by(id=id_).delete()
    db_session.commit()


def clear_reports_configs() -> None:
    db_session: Session = get_session()
    db_session.query(DB_ReportsConfig).delete()
    db_session.commit()
