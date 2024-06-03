from pydantic import BaseModel
from typing import Optional

from common.date import Date


class CategoryBase(BaseModel):
    name: Optional[str] = None


class CategoryCreate(CategoryBase):
    name: str


class CategoryUpdate(CategoryBase):
    ...


class Category(CategoryBase):
    id: int
    name: str


class SubcategoryBase(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None


class SubcategoryCreate(SubcategoryBase):
    name: str
    category_id: int


class SubcategoryUpdate(SubcategoryBase):
    ...


class Subcategory(SubcategoryBase):
    id: int
    name: str
    category_id: int


class ProductBase(BaseModel):
    name: str


class ProductCreate(ProductBase):
    ...


class Product(ProductBase):
    id: int


class BuyBase(BaseModel):
    date: Date
    category: CategoryBase
    subcategory: SubcategoryBase
    product: ProductBase


class BuyCreate(BuyBase):
    ...


class Buy(BuyBase):
    id: int
