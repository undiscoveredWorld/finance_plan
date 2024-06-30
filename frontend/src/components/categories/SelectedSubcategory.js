import Edit from "../buttons/Edit";
import Delete from "../buttons/Delete";
import {CategoriesSelectCursor} from "../../utils";
import CategoriesMenuElement from "./CategoriesMenuElement";

const SelectedSubcategory = (props) => {
    const setSelectCursor = props.setSelectCursor
    const category_id = props.category_id
    const subcategory_id = props.subcategory_id
    const name = props.name

    const editOnClick = () => {
        setSelectCursor(new CategoriesSelectCursor(category_id, subcategory_id, "edit"))
    }
    const deleteOnClick = () => {
        setSelectCursor(new CategoriesSelectCursor(category_id, subcategory_id, "delete"))
    }

    return <div className="flex-container">
        <CategoriesMenuElement name={name} />
        <Edit width={86} height={86} onClick={editOnClick}/>
        <Delete width={86} height={86} onClick={deleteOnClick}/>
    </div>
}

export default SelectedSubcategory