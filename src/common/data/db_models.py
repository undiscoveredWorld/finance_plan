from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
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


class Subcategory(Base):
    __tablename__ = "subcategories"

    id = mapped_column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String(40), unique=True, nullable=False)
    category_id = mapped_column(ForeignKey("categories.id"))

    category = relationship("Category", back_populates="subcategories")


Base.metadata.create_all(bind=engine)
