import CategoriesMenuElement from "./CategoriesMenuElement";
import InputCreateCategory from "./InputCreateCategory";
import {CategoriesSelectCursor} from "../../utils";

const CreateSubcategory = (props) => {
    const setSelectCursor = props.setSelectCursor
    const selectCursor = props.selectCursor
    const category_id = props.category_id

    const selectSubcategory = () => {
        setSelectCursor(new CategoriesSelectCursor(category_id, 0, "edit"))
    }

    const isSelected = () => {
        return (category_id === selectCursor.selectedCategory && selectCursor.selectedSubcategory === 0)
    }

    const checkSelectedCategoryAndReturnElement = () => {
        if (isSelected() && selectCursor.selectionMode === "edit") {
            return <InputCreateCategory setSelectCursor={setSelectCursor}/>
        } else {
            return (
                <div className="create-subcategory">
                    <CategoriesMenuElement name={"Create"} onClick={selectSubcategory}/>
                </div>
            )
        }
    }

    return <>{checkSelectedCategoryAndReturnElement()}</>
}

export default CreateSubcategory