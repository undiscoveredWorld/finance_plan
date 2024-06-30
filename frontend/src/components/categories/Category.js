import CategoriesMenuElement from "./CategoriesMenuElement";
import {CategoriesSelectCursor} from "../../utils";
import InputCreateCategory from "./InputCreateCategory";
import SelectedCategory from "./SelectedCategory";
import DeleteCategory from "./DeleteCategory";

const Category = (props) => {
    const selectCursor = props.selectCursor
    const setSelectCursor = props.setSelectCursor
    const category_id = props.category_id
    const name = props.name

    const selectCategory = () => {
        setSelectCursor(
            new CategoriesSelectCursor(category_id, -1, "select")
        )
    }

    const isSelected = () => {
        return (selectCursor.selectedCategory === category_id
            && selectCursor.selectedSubcategory === -1)
    }

    const getComponentBySelectionMode = () => {
        if (selectCursor.selectionMode === "edit") {
            return <InputCreateCategory setSelectCursor={setSelectCursor}/>
        } else if (selectCursor.selectionMode === "select") {
            return <SelectedCategory setSelectCursor={setSelectCursor} category_id={category_id} name={name}/>
        } else if (selectCursor.selectionMode === "delete") {
            return <DeleteCategory setSelectCursor={setSelectCursor} category_id={category_id} name={name}/>
        }
    }

    const checkSelectedCategoryAndReturnElement = () => {
        if (isSelected()) {
            return getComponentBySelectionMode()
        } else {
            return <CategoriesMenuElement name={name} onClick={selectCategory}/>
        }
    }

    return <>{checkSelectedCategoryAndReturnElement()}</>
}

export default Category