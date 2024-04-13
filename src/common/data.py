import ast

from domain.models import CategoryCreate, Category
from settings import PATH_TO_DATA_FILE


class DataFactory:
    __data: dict = {
        "categories": []
    }

    def add_category(self, category: CategoryCreate) -> Category:
        category_dict = category.model_dump()
        category_dict["id"] = len(self.__data["categories"])
        self.__data["categories"].append(category_dict)
        return Category.model_validate(category_dict)

    def list_categories(self) -> list[Category]:
        return self.__data["categories"]

    def save_data(self) -> None:
        with open(PATH_TO_DATA_FILE, 'w') as file:
            file.write(
                str(self.__data)
            )

    def load_data(self) -> dict:
        with open(PATH_TO_DATA_FILE, 'r') as file:
            data = file.read()
            data_dict = ast.literal_eval(data)
            self.__data = data_dict
