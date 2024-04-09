from pydantic import BaseModel

from common.date import Date


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    ...


class Category(CategoryBase):
    id: int


class SubCategoryBase(BaseModel):
    name: str


class SubCategoryCreate(SubCategoryBase):
    ...


class SubCategory(SubCategoryBase):
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
    subcategory: SubCategoryBase
    product: ProductBase


class BuyCreate(BuyBase):
    ...


class Buy(BuyBase):
    id: int
