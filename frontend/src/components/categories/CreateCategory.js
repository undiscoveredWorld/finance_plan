import CategoriesMenuElement from "./CategoriesMenuElement";
import InputCreateCategory from "./InputCreateCategory";
import {CategoriesSelectCursor} from "../../utils";

const CreateCategory = (props) => {
    const selectCursor = props.selectCursor
    const setSelectCursor = props.setSelectCursor
    const refreshCategories = props.refreshCategories

    const selectCategory = () => {
        setSelectCursor(
            new CategoriesSelectCursor(0, -1, "edit")
        )
    }

    const isSelected = () => {
        return (selectCursor.selectedCategory === 0
            && selectCursor.selectedSubcategory === -1)
    }

    const checkSelectedCategoryAndReturnElement = () => {
        if (isSelected() && selectCursor.selectionMode === "edit") {
            return <InputCreateCategory setSelectCursor={setSelectCursor} refreshCategories={refreshCategories}/>
        } else {
            return (
                <div className="create-category">
                    <CategoriesMenuElement name={"Create"} onClick={selectCategory}/>
                </div>
            )
        }
    }
    return <>{checkSelectedCategoryAndReturnElement()}</>

}

export default CreateCategory