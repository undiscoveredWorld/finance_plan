from pydantic import BaseModel

from common.date import Date


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    ...


class CategoryUpdate(CategoryBase):
    ...


class Category(CategoryBase):
    id: int


class SubcategoryBase(BaseModel):
    name: str


class SubcategoryCreate(SubcategoryBase):
    ...


class SubcategoryUpdate(SubcategoryBase):
    ...


class Subcategory(SubcategoryBase):
    id: int


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
