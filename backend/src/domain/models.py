import datetime

from pydantic import BaseModel


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


class SubcategoryCreate(SubcategoryBase):
    name: str
    category_id: int


class SubcategoryUpdate(SubcategoryBase):
    name: str | None = None


class Subcategory(SubcategoryBase):
    id: int
    name: str
    category_id: int

    class Config:
        from_attributes = True


class BuyBase(BaseModel):
    product: str | None = None
    date: datetime.date | None = None
    sum: int | None = None
    category_id: int | None = None
    subcategory_id: int | None = None


class BuyCreate(BuyBase):
    product: str
    date: datetime.date
    category_id: int
    subcategory_id: int
    sum: int

    def __init__(self,
                 date: datetime.date,
                 category_id: int,
                 subcategory_id: int,
                 product: str,
                 sum: int,
                 ) -> None:
        super().__init__(
            product=product,
            date=date,
            category_id=category_id,
            subcategory_id=subcategory_id,
            sum=sum,
        )


class BuyUpdate(BuyBase):
    ...


class Buy(BuyBase):
    id: int
    product: str
    date: datetime.date
    category_id: int
    subcategory_id: int
    sum: int

    category: Category
    subcategory: Subcategory

    class Config:
        from_attributes = True


class ReportsConfigBase(BaseModel):
    start_day: datetime.date | None
    expected_expenses_per_day: int | None


class ReportsConfigCreate(ReportsConfigBase):
    start_day: datetime.date
    expected_expenses_per_day: int


class ReportsConfigUpdate(ReportsConfigBase):
    ...


class ReportsConfig(ReportsConfigBase):
    id: int
    start_day: datetime.date
    expected_expenses_per_day: int
