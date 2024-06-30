import {useEffect, useState} from "react";
import {is_array_equal_array} from "../../utils";
import {get_and_refresh_categories} from "../../utils";

import CategoryList from "./CategoryList"
import CreateCategory from "./CreateCategory"
import {CategoriesSelectCursor} from "../../utils";

const Categories = () => {
    const [categories, setCategories] = useState([])
    const [selectCursor, setSelectCursor] = useState(new CategoriesSelectCursor(
        -1, -1, "default"
    ))
    const refreshCategories = (new_categories) => {
        if (!Array.isArray(new_categories)) return undefined
        if (is_array_equal_array(new_categories, categories)) return undefined
        setCategories(new_categories)
    }

    useEffect(() => {
        get_and_refresh_categories(refreshCategories)
    }, []);

    return (
        <div className="categories">
            <CreateCategory selectCursor={selectCursor} setSelectCursor={setSelectCursor}
                            refreshCategories={refreshCategories}/>
            <CategoryList categories={categories}
                          selectCursor={selectCursor} setSelectCursor={setSelectCursor}/>
        </div>
    )
}

export default Categories