from pydantic import BaseModel

from common.date import Date


class CategoryBase(BaseModel):
    name: str | None = None


class CategoryCreate(CategoryBase):
    name: str


class CategoryUpdate(CategoryBase):
    ...


class Category(CategoryBase):
    id: int
    name: str
    subcategories: list["Subcategory"]

    class Config:
        from_attributes = True


class SubcategoryBase(BaseModel):
    name: str | None = None
    category_id: int | None = None


class SubcategoryCreate(SubcategoryBase):
    name: str
    category_id: int


class SubcategoryUpdate(SubcategoryBase):
    ...


class Subcategory(SubcategoryBase):
    id: int
    name: str
    category_id: int
    category: Category

    class Config:
        from_attributes = True


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
