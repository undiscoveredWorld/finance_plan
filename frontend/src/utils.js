import axios from "axios";

export const is_array_equal_array = (array1, array2) => {
    if (array1 === array2) return true
    if (array1 == null || array2 == null) return false
    if (array1.length !== array2.length) return false

    for (let i = 0; i < array1.length; i++) {
        if (array1[i] !== array2[i])
            return false
    }

    return true
}

export const get_and_refresh_buys = (refreshRows) => {
    axios.get("http://31.128.37.252:8080/buys").then((response) => {
        const new_rows = response.data
        refreshRows(new_rows)
    })
}

export const get_and_refresh_categories = (refreshCategories) => {
    axios.get("http://31.128.37.252:8080/categories").then((response) => {
        const new_rows = response.data
        refreshCategories(new_rows)
    })
}

export const create_new_category = (new_category) => {
    axios.post("http://31.128.37.252:8080/category", {"name": new_category.name})
        .catch(e => console.log(e))
}

export class CategoriesSelectCursor {
    #selectedCategory
    #selectedSubcategory
    #selectionMode

    constructor(
        selectedCategory,
        selectedSubcategory,
        selectionMode
    ) {
        this.#selectedCategory = selectedCategory
        this.#selectedSubcategory = selectedSubcategory
        this.#selectionMode = selectionMode
    }

    get selectedCategory() {
        return this.#selectedCategory
    }

    get selectedSubcategory() {
        return this.#selectedSubcategory
    }

    get selectionMode() {
        return this.#selectionMode
    }
}

/**
 * Get value or default.
 * Uses for nullable props
 * @param value will be returned if not undefined and not null
 * @param default_ will be returned if value is undefined or null
 * @returns {*}
 */
export const get_value_or_default = (value, default_) => {
    // Uses for nullable props
    if (value === undefined || value === null) {
        return default_
    }
    return value
}

/**
 * Just empty func abbreviation. Equal () => {}
 */
export const empty_func = () => {
}


export class MenuManager {
    #setOpenedMenu

    constructor(setOpenedMenu) {
        this.#setOpenedMenu = setOpenedMenu
    }

    openBuys = () => {
        this.#setOpenedMenu("Buys")
    }
    openMainMenu = () => {
        this.#setOpenedMenu("Main menu")
    }
    openCategories = () => {
        this.#setOpenedMenu("Categories")
    }
}