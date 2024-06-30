import Accept from "../buttons/Accept";
import Cancel from "../buttons/Cancel";
import {CategoriesSelectCursor} from "../../utils";
import {useState} from "react";
import {create_new_category, get_and_refresh_categories} from "../../utils";

const InputCreateCategory = (props) => {
    const [value, setValue] = useState("")
    const refreshCategories = props.refreshCategories
    const setSelectCursor = props.setSelectCursor

    const cancelOnClick = () => {
        setSelectCursor(new CategoriesSelectCursor(-1, -1, "default"))
    }
    const acceptOnClick = () => {
        setSelectCursor(new CategoriesSelectCursor(-1, -1, "default"))
        create_new_category({"name": value})
        get_and_refresh_categories(refreshCategories)
    }
    const inputOnChange = (e) => {
        setValue(e.target.value)
    }

    return (
        <div className="flex-container">
            <input type="text" value={value} onChange={inputOnChange}/>
            <Accept width={86} height={86} onClick={acceptOnClick}/>
            <Cancel width={86} height={86} onClick={cancelOnClick}/>
        </div>
    )
}

export default InputCreateCategory