import Accept from "../buttons/Accept";
import Cancel from "../buttons/Cancel";
import {CategoriesSelectCursor} from "../../utils";
import CategoriesMenuElement from "./CategoriesMenuElement";

const DeleteCategory = (props) => {
    const category_id = props.category_id
    const setSelectCursor = props.setSelectCursor
    const name = props.name

    const cancelOnClick = () => {
        setSelectCursor(new CategoriesSelectCursor(-1, -1, "default"))
    }
    const acceptOnClick = () => {
        setSelectCursor(new CategoriesSelectCursor(-1, -1, "default"))
    }

    return (
        <div className="flex-container">
            <CategoriesMenuElement name={name}/>
            <Accept width={86} height={86} onClick={acceptOnClick}/>
            <Cancel width={86} height={86} onClick={cancelOnClick}/>
        </div>
    )
}

export default DeleteCategory