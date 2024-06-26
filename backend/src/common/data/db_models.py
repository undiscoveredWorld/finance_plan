import datetime

from sqlalchemy import (
    Column,
    String,
    Integer,
    Date,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    relationship,
    mapped_column,
)

from common.data.db import Base, engine


class Category(Base):
    __tablename__ = "categories"

    id = mapped_column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String(40), unique=True, nullable=False)

    subcategories = relationship("Subcategory", back_populates="category")
    buys = relationship("Buy", back_populates="category")


class Subcategory(Base):
    __tablename__ = "subcategories"

    id = mapped_column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String(40), nullable=False)
    category_id = mapped_column(ForeignKey("categories.id"))

    category = relationship("Category", back_populates="subcategories")
    buys = relationship("Buy", back_populates="subcategory")

    __table_args__ = (UniqueConstraint("category_id", "name", name="_subcategory_name_uc"),)


class Buy(Base):
    __tablename__ = "buys"

    id = mapped_column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    date = Column(Date, nullable=False, index=True)
    sum = Column(Integer, nullable=False)
    product = Column(String, nullable=False)
    category_id = mapped_column(ForeignKey("categories.id"), index=True)
    subcategory_id = mapped_column(ForeignKey("subcategories.id"), index=True)

    category = relationship("Category", back_populates="buys")
    subcategory = relationship("Subcategory", back_populates="buys")


class ReportsConfig(Base):
    __tablename__ = "report_configs"

    id = mapped_column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    start_day = Column(Date, nullable=False, default=datetime.date.today())
    expected_expenses_per_day = Column(Integer, unique=False, nullable=False, default=290)


Base.metadata.create_all(bind=engine)
