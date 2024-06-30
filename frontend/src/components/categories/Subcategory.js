import CategoriesMenuElement from "./CategoriesMenuElement";
import {CategoriesSelectCursor} from "../../utils";
import InputCreateCategory from "./InputCreateCategory";
import SelectedSubcategory from "./SelectedSubcategory";
import DeleteSubcategory from "./DeleteSubcategory";

const Subcategory = (props) => {
    const selectCursor = props.selectCursor
    const setSelectCursor = props.setSelectCursor
    const category_id = props.category_id
    const subcategory_id = props.subcategory_id
    const name = props.name

    const selectSubcategory = () => {
        setSelectCursor(
            new CategoriesSelectCursor(category_id, subcategory_id, "select")
        )
    }

    const isSelected = () => {
        return (selectCursor.selectedCategory === category_id
            && selectCursor.selectedSubcategory === subcategory_id)
    }

    const getComponentBySelectionMode = () => {
        if (selectCursor.selectionMode === "edit") {
            return <InputCreateCategory setSelectCursor={setSelectCursor}/>
        } else if (selectCursor.selectionMode === "select") {
            return <SelectedSubcategory setSelectCursor={setSelectCursor} name={name}
                                        category_id={category_id} subcategory_id={subcategory_id}/>
        } else if (selectCursor.selectionMode === "delete") {
            return <DeleteSubcategory category_id={category_id} subcategory_id={subcategory_id} name={name}
                                      setSelectCursor={setSelectCursor}/>
        }
    }

    const checkSelectedCategoryAndReturnElement = () => {
        if (isSelected()) {
            return getComponentBySelectionMode()
        } else {
            return (
                <div className="subcategory">
                    <CategoriesMenuElement name={name} onClick={selectSubcategory}/>
                </div>
            )
        }
    }

    return <>{checkSelectedCategoryAndReturnElement()}</>
}

export default Subcategory